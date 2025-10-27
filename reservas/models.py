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
    id_curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, blank=True, null=True)
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    codigo_turma = models.CharField(max_length=255)
    data_inicial = models.DateField(blank=True, null=True)
    data_final = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserva {self.codigo_turma} - {self.criador_por}"

class ReservaSala(models.Model):
    id_reserva = models.ForeignKey(Reserva, on_delete=models.DO_NOTHING, blank=True, null=True)
    id_sala = models.ForeignKey(Sala, on_delete=models.DO_NOTHING, blank=True, null=True)
    turno = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    descricao_reserva = models.TextField()
    status_reserva = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserva Sala {self.id_sala} ({self.turno})"

class Periodo(models.Model):
    id_reservasala = models.ForeignKey(ReservaSala, on_delete=models.DO_NOTHING, blank=True, null=True)
    primeiro = models.BooleanField(default=False)
    segundo = models.BooleanField(default=False)
    terceiro = models.BooleanField(default=False)
    quarto = models.BooleanField(default=False)
    integral = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

class DiaSemana(models.Model):
    id_reservasala = models.ForeignKey(ReservaSala, on_delete=models.DO_NOTHING, blank=True, null=True)
    id_periodo = models.ForeignKey(Periodo, on_delete=models.DO_NOTHING, blank=True, null=True)
    segunda = models.BooleanField(default=False)
    terca = models.BooleanField(default=False)
    quarta = models.BooleanField(default=False)
    quinta = models.BooleanField(default=False)
    sexta = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)
    domingo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
