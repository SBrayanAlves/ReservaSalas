from django.db import models
from django.utils import timezone

# Create your models here. 

#Criacao do modelo 'Usuario'
class Usuario(models.Model):

    CARGOS = [
        ('DIRETOR', 'Diretor / Assessora Administrativa'),
        ('NTI', 'Núcleo de Tecnologia e Informação'),
        ('COORDENADOR', 'Coordenador'),
        ('SECRETARIO', 'Secretário'),
        ('NAPI', 'Núcleo de Apoio Psicopedagógico'), #Eu nao sei oq e NAPI, depois vou ver melhor
        ('MANUTENCAO', 'Manutenção'),
    ]

    matricula = models.IntegerField(unique=True)
    matriculauser = models.ForeignKey('self', models.DO_NOTHING, db_column='matriculauser', to_field='matricula', blank=True, null=True)
    nome = models.CharField(max_length=255)
    email_institucional = models.EmailField(unique=True)
    sexo = models.CharField(max_length=1, blank=True, null=True, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    cargo = models.CharField(max_length=25, choices=CARGOS)
    senha = models.CharField(max_length=255)

    status_login = models.BooleanField(default=False)
    dth_insert = models.DateTimeField(default=timezone.now)
    dth_delete = models.DateTimeField(blank=True, null=True)
    status_delete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nome} ({self.get_cargo_display()})'

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'