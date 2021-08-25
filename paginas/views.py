from django.views.generic import TemplateView

#Impedir que usuários não autenticados acessem uma determinada página
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

#Feito herança de TemplateView como se fosse o extends de java
class ModeloView(TemplateView):
    template_name = "paginas/modelo.html"


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "paginas/index.html"


class PedidoView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "paginas/pedido.html"
