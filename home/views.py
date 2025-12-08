from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from salas.models import Bloco, Sala, Curso, Turma
from reservas.models import Reserva, ReservaSala
from salas.forms import ValidacaoSala
from usuarios.forms import ValidacaoUsuario
from django.utils import timezone
# Create your views here.

# DashBoard Principal deve ser responsavel pela passagens da salas reservadas!
class Home(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request:HttpRequest)->HttpResponse:

        hoje = timezone.now().date()

        reservas = ReservaSala.objects.filter(
            is_deleted=False,
            status_reserva=True,
            id_reserva__data_final__gte=hoje
        ).select_related(
            'id_sala',
            'id_sala__id_bloco',
            'id_reserva',             
            'id_reserva__id_curso'
        ).order_by('id_reserva__data_inicial', 'id_sala__id_bloco__bloco', 'id_sala__numero_sala')
        return render(request, 'home/home.html', {'reservas': reservas})
        

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
    
