from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pedido(models.Model):
    enderecoRua = models.CharField(max_length=250, verbose_name="Endereço")
    enderecoNum = models.IntegerField(verbose_name="Número")
    enderecoBairro = models.CharField(max_length=50, verbose_name="Bairro")

    cliente = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{}, Nº {} - {}".format(self.enderecoRua, self.enderecoNum, self.enderecoBairro)

class Produto(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Sabor")
    preco = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    descricao = models.CharField(max_length=250, verbose_name="Ingredientes")

    def __str__(self):
        return "{} no Valor de R$ {} / Ingredientes {}".format(self.nome, self.preco, self.descricao)

class Pedido_Produto(models.Model):
    quantidade = models.IntegerField()
    totalPedido = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Total")

    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)

    def __str__(self):
        return "#{} - {} x {} = R${}".format(self.pedido.pk, self.produto.nome, self.quantidade, self.totalPedido)


class Carrinho(models.Model):
    quantidade = models.IntegerField()
    totalPedido = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Total")

    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    cliente = models.ForeignKey(User, on_delete=models.PROTECT)

    # def __str__(self):+
        # return f"{self.quantidade} x {self.produto} - {self.cliente}"
