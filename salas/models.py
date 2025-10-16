from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Bloco(models.Model):
    bloco = models.CharField(max_length=1)
    matriculauser = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='salas')
    ativo = models.BooleanField()
    motivoinativo = models.TextField()

    def __str__(self):
        return f"Bloco {self.bloco}"


class Sala(models.Model):
    id_bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    matriculauser = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='salas')
    andar = models.IntegerField()
    nome_bloco = models.CharField(max_length=100)
    numero_sala = models.IntegerField()
    capacidade = models.IntegerField()
    tv_tamanho = models.DecimalField(max_digits=5, decimal_places=2)
    data_show = models.BooleanField(default=False)
    ativo = models.BooleanField(default=False)
    motivo_inativo = models.TextField(blank=True, null=True)
    dthinsert = models.DateTimeField(blank=True, null=True)
    dthdelete = models.DateTimeField(blank=True, null=True)
    statusdelete = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"Sala {self.numero_sala} - Bloco {self.nome_bloco}"