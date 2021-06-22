from django.views.generic import TemplateView

#Feito herana de TemplateView como se fosse o extends de java
class IndexView(TemplateView):
    template_name = "paginas/index.html"