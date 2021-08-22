from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import CriarUsuario
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

class CriarUsuario(CreateView):
    template_name="cadastro/form-cadastrar-login.html";
    form_class = CriarUsuario
    success_url = reverse_lazy("login")

    #Método para registrar o usuário no grupo "cliente"
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Cliente")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        
        return url

        return url
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["botao"] = "Cadastrar"
        return context
