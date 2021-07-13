from django.db import models

# Create your models here.
class Pedido(models.Model):
    enderecoRua = models.CharField(max_length=250, verbose_name="Endereço")
    enderecoNum = models.IntegerField(verbose_name="Número")
    enderecoBairro = models.CharField(max_length=50, verbose_name="Bairro")

    def __str__(self):
        return "{} / {}".format(self.enderecoRua, self.enderecoNum)

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    descricao = models.CharField(max_length=250)

    def __str__(self):
        return "{}, R$ {} + {}".format(self.nome, self.preco, self.descricao)

class Pedido_Produto(models.Model):
    quantidade = models.IntegerField()
    totalPedido = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Total")

    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)

    def __str_(self):
        return "{} - Quantidade {} = Preço {}".format(self.produto.nome, self.quatidade, self.totalPedido)
