from django.views.generic import TemplateView

#Feito herana de TemplateView como se fosse o extends de java
class ModeloView(TemplateView):
    template_name = "paginas/modelo.html"

class IndexView(TemplateView):
    template_name = "paginas/index.html"

class PedidoView(TemplateView):
    template_name = "paginas/pedido.html"