from django.urls import path
from salas.views import CriarSala, ListarSalas#, AtualizarSala, DeletarSala

urlpatterns = [
    path('criar/', CriarSala.as_view(), name='criarsala'),
    #path('update', AtualizarSala.as_view(), name='atualizarSala'),
    #path('deletar/', DeletarSala.as_view(), name='deletarSala'),
    path('', ListarSalas.as_view(), name='listarsalas'),
]
