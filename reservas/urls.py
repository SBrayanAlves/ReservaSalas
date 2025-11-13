from django.urls import path
from .views import ReservarSala

urlpatterns = [
    path("reservar/<int:sala_id>/", ReservarSala.as_view(), name="reservarsala"),
]
