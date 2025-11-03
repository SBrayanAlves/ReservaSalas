from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from salas.models import Bloco, Sala, Curso, Turma
from reservas.models import Reserva, ReservaSala, Periodo, DiaSemana
# Create your views here.

# DashBoard Principal deve ser responsavel pela passagens da salas reservadas!
class Home(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request:HttpRequest )-> HttpResponse:
        blocos = Bloco.objects.filter()
        salas = Sala.objects.filter(ativo=True)
        cursos = Curso.objects.filter()
        turmas = Turma.objects.filter()
        diassemana = DiaSemana.objects.filter()
        turnos = ReservaSala.objects.filter()
        periodos = Periodo.objects.filter()
        return render(request, 'home/home.html', {
            'salas': salas, 
            'blocos': blocos, 
            'cursos': cursos, 
            'turmas': turmas,
            'diassemana': diassemana,
            'turnos': turnos,
            'periodos': periodos
            })
    