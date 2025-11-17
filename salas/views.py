from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from salas.models import Sala, Bloco, Curso, Turma # Importe tudo
from reservas.models import DiaSemana, ReservaSala # Importe o necessário de reservas

# Create your views here.

class ListarSalas(LoginRequiredMixin, ListView):
    model = Sala
    template_name = "salas/listarsalas.html"
    context_object_name = 'salas' # Definir aqui é mais limpo

    def get_queryset(self):
        # Otimização: Usa select_related para buscar o Bloco junto com a Sala
        # Isso evita o problema N+1
        return Sala.objects.filter(is_deleted=False).select_related('id_bloco')

    def get_context_data(self, **kwargs):
        # Chama a implementação base primeiro para pegar o 'salas'
        context = super().get_context_data(**kwargs)
        
        # Adiciona o contexto extra para os filtros
        context['blocos'] = Bloco.objects.filter(ativo=True).order_by('bloco')
        context['cursos'] = Curso.objects.filter(is_deleted=False).order_by('nome_curso')
        context['turmas'] = Turma.objects.filter(is_deleted=False).order_by('codigo_turma')
        
        # Você também tinha filtros para dias e turnos:
        # (Idealmente, você definiria isso em um lugar, mas para o filtro:)
        context['diassemanas'] = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
        context['reservas'] = ReservaSala.objects.distinct('turno').values_list('turno', flat=True)

        return context