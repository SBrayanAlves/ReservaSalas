from django.urls import path
from .views import Home#, Cadastrar

urlpatterns = [
    path('', Home.as_view(), name='home'),
    #path('cadastrar/', Cadastrar.as_view(), name='cadastrar' )
]
