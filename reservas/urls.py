from django.urls import path
from .views import ReservarSala, Relatorio

urlpatterns = [
    path("reservar/<str:bloco_nome>/<int:numero_sala>/", ReservarSala.as_view(), name="reservarsala"),
    path("reservas/relatorio/", Relatorio.as_view(), name="relatorio")
]
