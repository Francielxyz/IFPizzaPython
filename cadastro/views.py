from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Pedido, Produto, Pedido_Produto

from django.urls import reverse_lazy

#Endereço Provavelmente não será adicionando e sim buscado da internet
class PedidoCreate(CreateView):
    model = Pedido
    fields = ["enderecoRua", "enderecoNum", "enderecoBairro"]
    template_name = "cadastro/form.html"
    success_url = reverse_lazy("index")

class ProdutoCreate(CreateView):
    model = Produto
    fields = ["nome", "preco", "descricao"]
    template_name = "cadastro/form.html"
    success_url = reverse_lazy("index")

############# Update #############
class PedidoUpdate(UpdateView):
    model = Pedido
    fields = ["enderecoRua", "enderecoNum", "enderecoBairro"]
    template_name = "cadastro/form.html"
    success_url = reverse_lazy("index")

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ["nome", "preco", "descricao"]
    template_name = "cadastro/form.html"
    success_url = reverse_lazy("index")

############# Delete #############
class PedidoDelete(DeleteView):
    model = Pedido
    template_name = "cadastro/form-excluir.html"
    success_url = reverse_lazy("index")

class ProdutoDelete(DeleteView):
    model = Produto
    template_name = "cadastro/form-excluir.html"
    success_url = reverse_lazy("index")

############# Listar #############
class PedidoList(ListView):
    model = Pedido
    template_name = "cadastro/listas/pedidoo.html"

class ProdutoList(ListView):
    model = Produto
    template_name = "cadastro/listas/produto.html"
