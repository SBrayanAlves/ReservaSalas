from django.test import TestCase
from django.forms import ValidationError
from datetime import date
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group  # <<< 1. IMPORTE O GROUP
from salas.models import Bloco, Sala, Curso, Turma
from .models import Reserva, ReservaSala, Periodo, DiaSemana
from .views import validar_conflito

Usuario = get_user_model()

class ReservaConflictTest(TestCase):

    def setUp(self):
        """
        Cria uma 'Reserva Base' no banco de dados antes de cada teste.
        """
        # 1. Criar dados base
        
        # --- CORREÇÃO AQUI ---
        # O signal 'passagem_de_cargo' (em usuarios/signals.py)
        # exige que o Grupo 'Diretor' exista no banco ANTES
        # de criar o usuário.
        Group.objects.create(name='Diretor')
        # --- FIM DA CORREÇÃO ---

        self.user = Usuario.objects.create_user(
            matricula='123456', 
            password='123',
            nome='Diretor de Teste',
            email_institucional='diretor@teste.com',
            telefone='61999998888',
            data_nascimento=date(1980, 1, 1),
            sexo='Outro', 
            cargo='Diretor'
        )
        
        self.bloco_a = Bloco.objects.create(bloco='A')
        self.sala_101 = Sala.objects.create(
            id_bloco=self.bloco_a, 
            numero_sala='101', 
            capacidade=50
        )
        self.curso_ads = Curso.objects.create(nome_curso='ADS')
        self.turma_ads01 = Turma.objects.create(
            id_curso=self.curso_ads, 
            codigo_turma='ADS01M1'
        )

        # 2. Criar a Reserva Base
        self.reserva_base = Reserva.objects.create(
            criador_por=self.user,
            id_turma=self.turma_ads01,
            codigo_turma='ADS01M1',
            data_inicial=date(2025, 1, 1),
            data_final=date(2025, 6, 30)
        )
        self.reserva_sala_base = ReservaSala.objects.create(
            id_reserva=self.reserva_base,
            id_sala=self.sala_101,
            turno='Matutino',
            responsavel='Prof. Base'
        )
        self.periodo_base = Periodo.objects.create(
            id_reservasala=self.reserva_sala_base,
            primeiro=True # 1º Período
        )
        self.dia_base = DiaSemana.objects.create(
            id_reservasala=self.reserva_sala_base,
            id_periodo=self.periodo_base,
            segunda=True # Segunda-feira
        )

    def test_conflito_direto_exato(self):
        """
        Tenta reservar a MESMA sala, data, turno, dia e período.
        DEVE levantar um ValidationError.
        """
        print("Executando: test_conflito_direto_exato")
        
        # Dados da nova reserva (idênticos)
        dias = {'segunda': True}
        periodos = {'primeiro': True}

        # self.assertRaises() é um teste que SÓ PASSA se a função
        # dentro dele levantar o erro especificado.
        with self.assertRaises(ValidationError, msg="Conflito direto não foi detectado!"):
            validar_conflito(
                sala=self.sala_101,
                data_ini=date(2025, 2, 1),
                data_fim=date(2025, 3, 1),
                turno='Matutino',
                dias_selecionados=dias,
                periodos_selecionados=periodos
            )

    def test_sem_conflito_outro_dia(self):
        """
        Tenta reservar a mesma sala, turno e período, mas em OUTRO DIA.
        NÃO DEVE levantar erro.
        """
        print("Executando: test_sem_conflito_outro_dia")
        
        # Dados da nova reserva (terça-feira)
        dias = {'terca': True} # Dia diferente
        periodos = {'primeiro': True}

        try:
            validar_conflito(
                sala=self.sala_101,
                data_ini=date(2025, 2, 1),
                data_fim=date(2025, 3, 1),
                turno='Matutino',
                dias_selecionados=dias,
                periodos_selecionados=periodos
            )
        except ValidationError as e:
            # self.fail() faz o teste falhar imediatamente.
            self.fail(f"Teste falhou! Um conflito foi detectado indevidamente: {e}")

    def test_sem_conflito_outro_periodo(self):
        """
        Tenta reservar a mesma sala, turno e dia, mas em OUTRO PERÍODO.
        NÃO DEVE levantar erro.
        """
        print("Executando: test_sem_conflito_outro_periodo")
        
        dias = {'segunda': True}
        periodos = {'segundo': True} # Período diferente

        try:
            validar_conflito(
                sala=self.sala_101,
                data_ini=date(2025, 2, 1),
                data_fim=date(2025, 3, 1),
                turno='Matutino',
                dias_selecionados=dias,
                periodos_selecionados=periodos
            )
        except ValidationError as e:
            self.fail(f"Teste falhou! Conflito de período detectado indevidamente: {e}")

    def test_sem_conflito_outro_turno(self):
        """
        Tenta reservar a mesma sala, dia e período, mas em OUTRO TURNO.
        NÃO DEVE levantar erro.
        """
        print("Executando: test_sem_conflito_outro_turno")
        
        dias = {'segunda': True}
        periodos = {'primeiro': True}

        try:
            validar_conflito(
                sala=self.sala_101,
                data_ini=date(2025, 2, 1),
                data_fim=date(2025, 3, 1),
                turno='Noturno', # Turno diferente
                dias_selecionados=dias,
                periodos_selecionados=periodos
            )
        except ValidationError as e:
            self.fail(f"Teste falhou! Conflito de turno detectado indevidamente: {e}")

    def test_sem_conflito_outra_data(self):
        """
        Tenta reservar a mesma sala, dia, turno e período, mas em OUTRO SEMESTRE.
        NÃO DEVE levantar erro.
        """
        print("Executando: test_sem_conflito_outra_data")
        
        dias = {'segunda': True}
        periodos = {'primeiro': True}

        try:
            validar_conflito(
                sala=self.sala_101,
                data_ini=date(2025, 7, 1), # Data não sobrepõe a base (que termina em 6/30)
                data_fim=date(2025, 12, 15),
                turno='Matutino',
                dias_selecionados=dias,
                periodos_selecionados=periodos
            )
        except ValidationError as e:
            self.fail(f"Teste falhou! Conflito de data detectado indevidamente: {e}")