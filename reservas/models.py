from django.db import models
from salas.models import Curso, Turma, Sala

class Reserva(models.Model):
    criador_por = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.SET_NULL,
        to_field='matricula',
        blank=True,
        null=True
        )
    id_curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Curso')
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, verbose_name='Turma')
    codigo_turma = models.CharField(max_length=255, verbose_name='Código da turma')
    data_inicial = models.DateField(blank=True, null=True)
    data_final = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserva {self.codigo_turma} - {self.criador_por}"

class ReservaSala(models.Model):
    id_reserva = models.ForeignKey(Reserva, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Reserva')
    id_sala = models.ForeignKey(Sala, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Sala')
    turno = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255, verbose_name='Responsável')
    descricao_reserva = models.TextField(verbose_name='Descrição da reserva')
    status_reserva = models.BooleanField(default=True, verbose_name='Status da reserva')
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserva Sala {self.id_sala} ({self.turno})"

class Periodo(models.Model):
    id_reservasala = models.ForeignKey(ReservaSala, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Sala reservada')
    primeiro = models.BooleanField(default=False)
    segundo = models.BooleanField(default=False)
    terceiro = models.BooleanField(default=False)
    quarto = models.BooleanField(default=False)
    integral = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

class DiaSemana(models.Model):
    id_reservasala = models.ForeignKey(ReservaSala, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Sala reservada')
    id_periodo = models.ForeignKey(Periodo, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Período')
    segunda = models.BooleanField(default=False, verbose_name='Segunda-feira')
    terca = models.BooleanField(default=False, verbose_name='Terça-feira')
    quarta = models.BooleanField(default=False, verbose_name='Quarta-feira')
    quinta = models.BooleanField(default=False, verbose_name='Quinta-feira')
    sexta = models.BooleanField(default=False, verbose_name='Sexta-feira')
    sabado = models.BooleanField(default=False, verbose_name='Sábado')
    domingo = models.BooleanField(default=False, verbose_name='Domingo')
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
