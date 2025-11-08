from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from salas.models import Sala, Bloco
from django.urls import reverse_lazy

# Create your views here.

class ListarSalas(ListView):
    model = Sala
    template_name = "salas/listarsalas.html"
    def get_context_object_name(self, object_list):
        return 'salas'