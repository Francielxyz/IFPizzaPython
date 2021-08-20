from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Pedido, Produto, Pedido_Produto, Carrinho

from django.urls import reverse_lazy

#Impedir que usuários não autenticados acessem uma determinada página
from django.contrib.auth.mixins import LoginRequiredMixin

#Controle de acesso dos login de adm e cliente
from braces.views import GroupRequiredMixin

#Endereço Provavelmente não será adicionando e sim buscado da internet
############# Create #############
class PedidoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pedido
    fields = ["enderecoRua", "enderecoNum", "enderecoBairro"]
    template_name = "cadastro/form-finalizar-pedido.html"
    success_url = reverse_lazy("listar-produto")

    # Sobrescrever método para enviar dados adicionais ao template
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Finalizando Pedido de Pizza"
        context["botao"] = "Finalizar Pedido"
        context["carrinho"] = Carrinho.objects.filter(cliente=self.request.user)
        return context

    # Ao salvar na tela de criar pedido
    def form_valid(self, form):

        # Consultar todos as pizzas que estão no carrinho
        pizzas = Carrinho.objects.filter(cliente=self.request.user)

        # Se tiver pizzas faz o processo normal
        if(pizzas.count() >= 1):

            # Define o cliente como o usuário logado
            form.instance.cliente = self.request.user

            # Salva o objeto no banco e você pode usar o self.object
            url = super().form_valid(form)

            # Criar um Pedido_Produto para cada pizza no carrinho
            for carrinho in pizzas:
                Pedido_Produto.objects.create(
                    quantidade=carrinho.quantidade,
                    totalPedido=carrinho.quantidade*carrinho.produto.preco,
                    pedido=self.object,
                    produto=carrinho.produto
                )
                # Exclui essa pizza do carrinho
                carrinho.delete()

            # retorna a url de sucesso
            return url

        # se não tem, da um erro e não cria esse pedido
        else:
            form.add_error(None, "Você não tem pizzas no carrinho para fechar o pedido!")
            return self.form_invalid(form)


class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    fields = ["nome", "preco", "descricao"]
    template_name = "cadastro/form-cadastrar-produto.html"
    success_url = reverse_lazy("listar-produto")

    # Sobrescrever método para enviar dados adicionais ao template
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastro de Novo Sabor de Pizza"
        context["botao"] = "Cadastrar"
        return context


class CarrinhoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Carrinho
    fields = ["produto", "quantidade"]
    template_name = "cadastro/form-realizar-pedido.html"
    success_url = reverse_lazy("cadastrar-pedido") 

    # Sobrescrever método para enviar dados adicionais ao template
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["botao"] = "Realizar Pedido"
        return context

    def form_valid(self, form):
        
        # Pega o valor do campo quantidade e multiplica pelo preço do produto que foi selecionado
        form.instance.totalPedido = form.instance.quantidade * form.instance.produto.preco
        # define como cliente o usuário que está logado
        form.instance.cliente = self.request.user

        # Salva o objeto no banco e retorna a url do INDEX sabendo que o pedido foi adicionando
        url = super().form_valid(form)

        return url


############# Update #############
class PedidoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pedido
    fields = ["enderecoRua", "enderecoNum", "enderecoBairro"]
    template_name = "cadastro/form-pedido.html"
    success_url = reverse_lazy("inicio")

    # Sobrescrever método para enviar dados adicionais ao template
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Atualizar Endereço de Entrega"
        context["botao"] = "Atualizar Endereço"
        return context


class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    fields = ["nome", "preco", "descricao"]
    template_name = "cadastro/form-atualizar-produto.html"
    success_url = reverse_lazy("listar-produto")

    # Sobrescrever método para enviar dados adicionais ao template
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["botao"] = "Atualizar Pizza"
        return context


############# Delete #############
class PedidoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = "cadastro/form-excluir-produto.html"
    success_url = reverse_lazy("inicio")


class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    template_name = "cadastro/form-excluir-produto.html"
    success_url = reverse_lazy("listar-produto")


############# Listar #############
class PedidoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = "cadastro/listas/pedido.html"


class ProdutoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Produto
    template_name = "cadastro/listas/produto.html"

