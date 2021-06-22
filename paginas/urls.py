from django.urls import path 
from .views import IndexView # . indica que esta pegando algo dentro deste diretório (pasta paginas)

urlpatterns = [
    #path('endereço'/', MinhaView.as_view(), name='nome-da-url')
    path('', IndexView.as_view(), name='inicio'),
]
