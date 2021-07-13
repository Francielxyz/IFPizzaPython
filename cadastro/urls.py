from django.urls import path 

from .views import PedidoCreate, ProdutoCreate
from .views import PedidoUpdate, ProdutoUpdate
from .views import PedidoDelete, ProdutoDelete
from .views import PedidoList, ProdutoList

urlpatterns = [
    path('cadastrar/pedido/', PedidoCreate.as_view(), name='cadastrar-pedido'),
    path('cadastrar/produto/', ProdutoCreate.as_view(), name='cadastrar-produto'),

    path('atualizar/pedido/<int:pk>/', PedidoUpdate.as_view(), name='atualizar-pedido'),
    path('atualizar/produto/<int:pk>/', ProdutoUpdate.as_view(), name='atualizar-produto'),

    path('excluir/pedido/<int:pk>/', PedidoDelete.as_view(), name='excluir-pedido'),
    path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name='excluir-produto'),

    path('listar/pedido/', PedidoList.as_view(), name='listar-pedido'),
    path('listar/produto/', ProdutoList.as_view(), name='listar-produto'),
]
