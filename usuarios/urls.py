from django.urls import path 
# django já tem módulos para páginas de login
from django.contrib.auth import views as auth_views
from .views import CriarUsuario

urlpatterns = [
    #path('endereço'/', MinhaView.as_view(), name='nome-da-url')
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', CriarUsuario.as_view(), name='registrar'),
]
