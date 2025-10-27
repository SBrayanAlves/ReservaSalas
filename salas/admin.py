from django.contrib import admin
from .models import Sala, Bloco, Curso, Turma

# Register your models here.

admin.site.register(Sala)
admin.site.register(Bloco)
admin.site.register(Curso)
admin.site.register(Turma)