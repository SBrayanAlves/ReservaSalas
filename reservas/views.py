from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from salas.models import Sala


# Create your views here.

class ReservarSala(LoginRequiredMixin, View):
    def get(self, request:HttpRequest, sala_id)->HttpResponse:
        sala = get_object_or_404(Sala, id=sala_id)
        return render(request, "reservas/reservarsala.html", context={
            'sala': sala
        })
    
    def post(self, request:HttpRequest)->HttpResponse:
        return render(request, "reservas/reservarsala.html")