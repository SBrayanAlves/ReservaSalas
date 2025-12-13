from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from io import BytesIO
from salas.models import Bloco, Sala
from reservas.models import ReservaSala

class PDFMapaSalas:
    def __init__(self):
        self.buffer = BytesIO()
        self.doc = SimpleDocTemplate(
            self.buffer, 
            pagesize=landscape(A4),
            rightMargin=1*cm, leftMargin=1*cm, 
            topMargin=1*cm, bottomMargin=1*cm
        )
        self.elements = []
        self.styles = getSampleStyleSheet()

    def _criar_intervalo_dias(self, lista_dias_idxs):
        """
        Transforma [1, 2, 3, 4] em 'TER A SEX'
        Ou [0, 2, 4] em 'SEG, QUA, SEX'
        """
        mapa_dias = {0: 'SEG', 1: 'TER', 2: 'QUA', 3: 'QUI', 4: 'SEX', 5: 'SAB', 6: 'DOM'}
        
        if not lista_dias_idxs:
            return ""
            
        lista_dias_idxs.sort()
        
        # Verifica se são consecutivos (para usar "A")
        # Exige pelo menos 3 dias para usar o "A" (ex: TER A QUI)
        if len(lista_dias_idxs) >= 3:
            consecutivos = True
            for i in range(len(lista_dias_idxs) - 1):
                if lista_dias_idxs[i+1] != lista_dias_idxs[i] + 1:
                    consecutivos = False
                    break
            
            if consecutivos:
                return f"{mapa_dias[lista_dias_idxs[0]]} A {mapa_dias[lista_dias_idxs[-1]]}"

        # Se não forem consecutivos ou forem poucos, lista com vírgula
        return ", ".join([mapa_dias[d] for d in lista_dias_idxs])

    def _formatar_frequencia(self, reserva_sala):
        """
        Gera a string ex: 'TER A SEX' ou 'TER 2ºH'
        """
        # Busca os horários ordenados
        horarios = reserva_sala.horarios.all().order_by('dia_semana', 'periodo')
        
        if not horarios.exists():
            return ""

        # 1. Agrupa períodos por dia
        # Ex: {1: {1,2,3,4}} -> Terça Integral
        dias_periodos = {}
        for h in horarios:
            dias_periodos.setdefault(h.dia_semana, set()).add(h.periodo)

        # 2. Inverte para agrupar dias com os mesmos períodos
        # Ex: { (1,2,3,4): [1, 2, 3, 4] } -> Terça a Sexta têm todos os horários
        periodos_para_dias = {}
        for dia, periodos_set in dias_periodos.items():
            # frozenset permite usar o conjunto como chave de dicionário
            chave_periodos = frozenset(periodos_set)
            periodos_para_dias.setdefault(chave_periodos, []).append(dia)

        linhas = []
        for periodos_set, lista_dias in periodos_para_dias.items():
            # Formata os dias (ex: "TER A SEX")
            texto_dias = self._criar_intervalo_dias(lista_dias)
            
            # Verifica se é o turno todo (1, 2, 3, 4) ou parcial
            if {1, 2, 3, 4}.issubset(periodos_set):
                # Se for integral, mostra só os dias
                linhas.append(texto_dias)
            else:
                # Se for parcial, mostra os dias + períodos (Ex: "TER 2ºH")
                lista_p = sorted(list(periodos_set))
                texto_p = ",".join([f"{p}ºH" for p in lista_p])
                linhas.append(f"{texto_dias} {texto_p}")

        return "\n".join(linhas)

    def _get_reserva_info(self, sala, turno):
        # Adicionei 'prefetch_related' para carregar os horários de forma eficiente
        reservas = ReservaSala.objects.filter(
            id_sala=sala,
            turno=turno,
            status_reserva=True,
            is_deleted=False
        ).select_related('id_reserva', 'id_reserva__id_turma').prefetch_related('horarios')

        if not reservas.exists():
            return "LIVRE"
        
        textos = []
        for r in reservas:
            turma = r.id_reserva.codigo_turma
            responsavel = r.responsavel
            
            # Chama a nova função de formatação
            dias_horarios = self._formatar_frequencia(r)
            
            # Monta o bloco de texto da célula
            # Ex: 
            # FAR03M1
            # TER A SEX
            # (Prof. Silva)
            item = f"{turma}\n{dias_horarios}\n({responsavel})"
            textos.append(item)
        
        return "\n\n".join(textos)

    def gerar_pdf(self):
        # ... (O restante do método gerar_pdf permanece igual ao anterior) ...
        # Apenas certifique-se de que está chamando self._get_reserva_info corretamente
        
        title_style = self.styles['Heading1']
        title_style.alignment = 1
        self.elements.append(Paragraph("Mapa de Distribuição de Salas - Unieuro", title_style))
        self.elements.append(Spacer(1, 0.5*cm))

        blocos = Bloco.objects.filter(ativo=True).order_by('bloco')

        for bloco in blocos:
            self.elements.append(Paragraph(f"BLOCO {bloco.bloco}", self.styles['Heading2']))
            
            data = [['Sala / Andar', 'Matutino', 'Vespertino', 'Noturno', 'Capacidade', 'Recursos']]
            salas = Sala.objects.filter(id_bloco=bloco, is_deleted=False).order_by('andar', 'numero_sala')

            if not salas.exists():
                self.elements.append(Paragraph("Nenhuma sala cadastrada.", self.styles['Normal']))
                self.elements.append(Spacer(1, 0.5*cm))
                continue

            for sala in salas:
                matutino = self._get_reserva_info(sala, 'Matutino')
                vespertino = self._get_reserva_info(sala, 'Vespertino')
                noturno = self._get_reserva_info(sala, 'Noturno')
                
                recursos = []
                if sala.tv_tamanho: recursos.append(f"TV {sala.tv_tamanho}")
                if sala.data_show: recursos.append("DataShow")
                str_recursos = "\n".join(recursos) if recursos else "-"

                data.append([
                    f"{sala.numero_sala}\n({sala.andar})",
                    matutino,
                    vespertino,
                    noturno,
                    str(sala.capacidade),
                    str_recursos
                ])

            tabela = Table(data, colWidths=[2.5*cm, 7*cm, 7*cm, 7*cm, 2.5*cm, 3*cm])
            
            estilo_tabela = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.navy),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
            ])
            
            tabela.setStyle(estilo_tabela)
            self.elements.append(tabela)
            self.elements.append(Spacer(1, 1*cm))

        self.doc.build(self.elements)
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf