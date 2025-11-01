'''
signal -> evento de criar conta passando o cargo
sender -> objeto q envia o sinal "usuario"
receive -> ouve o sinal e faz a funcao

usados
post_save()
user.save()
'''

from django.db.models.signals import post_save
from .models import Usuario
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_save, sender=Usuario)
def passagem_de_cargo(sender, instance, created, **kwargs):
    if created:  
        cargo = instance.cargo
        grupo = Group.objects.get(name=cargo)
        instance.groups.add(grupo)