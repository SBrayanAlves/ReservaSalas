from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from salas.models import Bloco, Sala, Curso, Turma
from reservas.models import Reserva, ReservaSala
from salas.forms import ValidacaoSala
from usuarios.forms import ValidacaoUsuario
# Create your views here.

# DashBoard Principal deve ser responsavel pela passagens da salas reservadas!
class Home(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request:HttpRequest )-> HttpResponse:
        blocos = Bloco.objects.filter().order_by('bloco')
        salas = Sala.objects.filter(ativo=True)
        cursos = Curso.objects.filter()
        turmas = Turma.objects.filter()
        turnos = ReservaSala.objects.filter()
        return render(request, 'home/home.html', {
            'salas': salas, 
            'blocos': blocos, 
            'cursos': cursos, 
            'turmas': turmas,
            'turnos': turnos,
            })
    

class Cadastro(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'usuarios.add_usuario'

    def get(self, request:HttpRequest)->HttpResponse:
        blocos = Bloco.objects.filter().order_by('bloco')
        salaForm = ValidacaoSala()
        usuarioForm = ValidacaoUsuario()
        context = {
            'sala_form': salaForm,
            'usuario_form': usuarioForm,
            'blocos': blocos
        }
        return render(request, 'home/cadastrar.html', context)
    
    def post(self, request:HttpRequest)->HttpResponse:
        salaForm = ValidacaoSala()
        usuarioForm = ValidacaoUsuario()

        if 'cadastro_sala' in request.POST: 
            print('entrou no post de sala')
            salaForm = ValidacaoSala(request.POST)
            if salaForm.is_valid():
                print('formulario validado')
                salaForm.save()
                return redirect('home')
            else:
                print('--- ERRO DE VALIDAÇÃO ---')
                print(salaForm.errors)
            return render(request, 'home/cadastrar.html', {'form': salaForm})
                
        elif 'cadastro_usuario' in request.POST:
            usuarioForm = ValidacaoUsuario(request.POST)
            if usuarioForm.is_valid():
                usuarioForm.save()
                return redirect('home')
            return render(request, 'home/cadastrar.html', {'form': usuarioForm})
        
        context = {
            'sala_form': salaForm,
            'usuario_form': usuarioForm
        }
        
        return render(request, 'home/cadastrar.html', context)
    
