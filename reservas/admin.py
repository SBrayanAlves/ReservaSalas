from django.contrib import admin
from .models import Reserva, ReservaSala, DiaSemana, Periodo

# Register your models here.

admin.site.register(Reserva)
admin.site.register(ReservaSala)
admin.site.register(DiaSemana)
admin.site.register(Periodo)