from django.contrib import messages
from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from salas.models import Bloco, Sala, Curso, Turma
from .models import Reserva, ReservaSala, DiaSemana, Periodo
from .forms import VerificacaoReserva
from django.db import transaction



def validar_conflito(sala, data_ini, data_fim, turno, dias_selecionados, periodos_selecionados):
    """
    Verifica se já existe uma reserva conflitante no banco de dados.
    Levanta um ValidationError se um conflito for encontrado.
    """
    
    # 1. Filtro Macro: Busca reservas na mesma sala, turno e que se sobrepõem nas datas
    conflitos_potenciais = ReservaSala.objects.filter(
        id_sala=sala,
        turno=turno,
        status_reserva=True,
        is_deleted=False,
        id_reserva__data_inicial__lte=data_fim, # Data de início da reserva existente é <= nova data final
        id_reserva__data_final__gte=data_ini   # Data final da reserva existente é >= nova data inicial
    ).select_related('id_reserva') # Otimiza a busca

    if not conflitos_potenciais.exists():
        return True # Ótimo! Nenhum conflito de data/sala/turno.

    # 2. Filtro Fino: Iterar sobre os conflitos potenciais e checar dias/períodos
    for reserva_sala_existente in conflitos_potenciais:
        
        # Busca os dias e períodos da reserva existente
        dias_existentes = DiaSemana.objects.filter(id_reservasala=reserva_sala_existente).first()
        periodos_existentes = Periodo.objects.filter(id_reservasala=reserva_sala_existente).first()

        if not dias_existentes or not periodos_existentes:
            continue # Ignora dados inconsistentes no banco

        # 3. Checagem de colisão de DIAS
        colisao_dias = False
        if (dias_selecionados.get('segunda') and dias_existentes.segunda) or \
           (dias_selecionados.get('terca') and dias_existentes.terca) or \
           (dias_selecionados.get('quarta') and dias_existentes.quarta) or \
           (dias_selecionados.get('quinta') and dias_existentes.quinta) or \
           (dias_selecionados.get('sexta') and dias_existentes.sexta) or \
           (dias_selecionados.get('sabado') and dias_existentes.sabado) or \
           (dias_selecionados.get('domingo') and dias_existentes.domingo):
            colisao_dias = True
        
        if not colisao_dias:
            continue # Conflito de data, mas não no mesmo dia. Próximo!

        # 4. Checagem de colisão de PERÍODOS (se colidiu o dia)
        colisao_periodos = False
        if (periodos_selecionados.get('primeiro') and periodos_existentes.primeiro) or \
           (periodos_selecionados.get('segundo') and periodos_existentes.segundo) or \
           (periodos_selecionados.get('terceiro') and periodos_existentes.terceiro) or \
           (periodos_selecionados.get('quarto') and periodos_existentes.quarto) or \
           (periodos_selecionados.get('integral') and periodos_existentes.integral):
            colisao_periodos = True

        # 5. CONFLITO ENCONTRADO!
        if colisao_periodos:
            turma_conflito = reserva_sala_existente.id_reserva.codigo_turma
            raise ValidationError(
                f"CONFLITO: Esta sala já está reservada para a turma {turma_conflito} "
                f"em um dia/período sobreposto dentro desse intervalo de datas."
            )

    return True # Passou por todas as checagens


class ReservarSala(LoginRequiredMixin, View):

    def get(self, request: HttpRequest, bloco_nome: str, sala_id: int) -> HttpResponse:
        # Busca por ID (PK), que é mais confiável que 'numero_sala'
        sala = get_object_or_404(Sala, id=sala_id) 
        bloco = sala.id_bloco # Pega o bloco a partir da sala
        
        # Validar se o bloco_nome da URL bate (segurança extra)
        if bloco.bloco != bloco_nome:
             return HttpResponse("URL inválida", status=404)

        cursos = Curso.objects.all().order_by('nome_curso')
        turmas = Turma.objects.all().order_by('codigo_turma')

        # --- CORREÇÃO 2: Inicializar o formulário no GET ---
        # Pré-popula o formulário com os dados da sala e bloco
        form = VerificacaoReserva(initial={
            'id_sala': sala.id, 
            'id_bloco': bloco.id
        })

        context = {
            'form': form, # Passa o formulário para o template
            'bloco': bloco,
            'sala': sala,
            'cursos': cursos,
            'turmas': turmas,
        }
        return render(request, "reservas/reservarsala.html", context)


    def post(self, request: HttpRequest, bloco_nome: str, sala_id: int) -> HttpResponse:
        # Re-buscar os dados é necessário para renderizar o contexto se o form falhar
        sala = get_object_or_404(Sala, id=sala_id)
        bloco = sala.id_bloco
        cursos = Curso.objects.all().order_by('nome_curso')
        turmas = Turma.objects.all().order_by('codigo_turma')

        form = VerificacaoReserva(request.POST)
        
        if form.is_valid():
            dados = form.cleaned_data
            
            # ... (Lógica de validação e salvamento) ...
            # ... (Seu código de 'dias_selecionados', 'try/except', 'transaction.atomic' está PERFEITO) ...
            
            dias_selecionados = {dia: True for dia in dados['dias_semana']}
            periodos_selecionados = {p: True for p in dados['periodos']}

            try:
                validar_conflito(
                    sala=dados['id_sala'],
                    data_ini=dados['data_inicial'],
                    data_fim=dados['data_final'],
                    turno=dados['turno'],
                    dias_selecionados=dias_selecionados,
                    periodos_selecionados=periodos_selecionados
                )

                with transaction.atomic():
                    turma_selecionada = dados['id_turma']
                    
                    nova_reserva = Reserva.objects.create(
                        criador_por=request.user,
                        id_curso=dados['id_curso'],
                        id_turma=turma_selecionada,
                        codigo_turma=turma_selecionada.codigo_turma,
                        data_inicial=dados['data_inicial'],
                        data_final=dados['data_final']
                    )
                    
                    nova_reserva_sala = ReservaSala.objects.create(
                        id_reserva=nova_reserva,
                        id_sala=dados['id_sala'],
                        turno=dados['turno'],
                        responsavel=dados['professor'],
                        descricao_reserva=dados['descricao']
                    )
                    
                    periodo_obj = Periodo.objects.create(
                        id_reservasala=nova_reserva_sala,
                        primeiro='primeiro' in dados['periodos'],
                        segundo='segundo' in dados['periodos'],
                        terceiro='terceiro' in dados['periodos'],
                        quarto='quarto' in dados['periodos'],
                        integral='integral' in dados['periodos']
                    )
                    
                    DiaSemana.objects.create(
                        id_reservasala=nova_reserva_sala,
                        id_periodo=periodo_obj,
                        segunda='segunda' in dados['dias_semana'],
                        terca='terca' in dados['dias_semana'],
                        quarta='quarta' in dados['dias_semana'],
                        quinta='quinta' in dados['dias_semana'],
                        sexta='sexta' in dados['dias_semana'],
                        sabado='sabado' in dados['dias_semana'],
                        domingo='domingo' in dados['dias_semana']
                    )
                
                messages.success(request, 'Reserva criada com sucesso!')
                return redirect('listarsalas')

            except ValidationError as e:
                form.add_error(None, e)
        
        # --- CORREÇÃO 3: Lógica movida ---
        # Se o form NÃO for válido (ou se 'validar_conflito' falhar), 
        # o Django vai pular o IF e vir direto para cá.
        # Nós apenas precisamos renderizar o template com o 'form' 
        # que já contém os erros.

        context = {
            'form': form, # 'form' aqui já contém os erros de validação
            'sala': sala,
            'bloco': bloco,
            'cursos': cursos,
            'turmas': turmas
        }
        # Seu template de formulário deve exibir o {{ form.non_field_errors }}
        return render(request, 'reservas/reservarsala.html', context)