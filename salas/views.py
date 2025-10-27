from django.shortcuts import render
from django.views.generic import CreateView, ListView#, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from salas.models import Sala, Bloco, Curso, Turma
from django.urls import reverse_lazy

# Create your views here.

class EscolherBloco(LoginRequiredMixin, CreateView):
    model = Bloco
    fields = ['bloco', 'ativo', 'motivo_inativo']
    template_name = 'salas/criarbloco.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        bloco = form.save(commit=False)
        bloco.criada_por = self.request.user
        bloco.save()
        return super().form_valid(form)

class CriarSala(LoginRequiredMixin, CreateView):
    model = Sala
    fields = ['andar', 'numero_sala', 'capacidade', 'tv_tamanho', 'data_show', 'ativo', 'motivo_inativo']
    template_name = 'salas/criarsalas.html'
    success_url = reverse_lazy('listarsalas')
    def form_valid(self, form):
        sala = form.save(commit=False)
        sala.criada_por = self.request.user
        sala.save()
        return super().form_valid(form)
    
class ListarSalas(ListView):
    model = Sala
    template_name = "salas/listarsalas.html"
    def get_context_object_name(self, object_list):
        return 'salas'
