from django.urls import path
from .views import ReservarSala

urlpatterns = [
    path("reservar/<str:bloco_nome>/<int:numero_sala>/", ReservarSala.as_view(), name="reservarsala"),
]
