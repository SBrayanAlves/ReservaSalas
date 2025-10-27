from django.urls import path
from .views import CriarUsuario, LoginUsuario, LogoutUsuario, EdicaoUsuario, EnviarEmail, ConfirmacaoCodigo, NovaSenha

urlpatterns = [
    path('registrar/', CriarUsuario.as_view(), name='registrar'),
    path('login/', LoginUsuario.as_view(), name='login'),
    path('logout/', LogoutUsuario.as_view(), name='logout'),
    #path('perfil/', ) -> Visualizacao do proprio perfil 
    path('perfil/editar', EdicaoUsuario.as_view(), name='edicaousuario'),
    path('recuperar/', EnviarEmail.as_view(), name='enviaremail'),
    path('codigo/', ConfirmacaoCodigo.as_view(), name='confirmacaocodigo'),
    path('nova-senha/', NovaSenha.as_view(), name='novasenha')
]
