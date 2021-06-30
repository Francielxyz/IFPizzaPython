from django.db import models

# Create your models here.
class Pedido(models.Model):
    latitude = models.DecimalField(decimal_places=10, max_digits=12)
    longitude = models.DecimalField(decimal_places=10, max_digits=13)

    def __str__(self):
        return "{} / {}".format(self.latitude, self.longitude)

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=5, verbose_name="Preço")
    descricao = models.CharField(max_length=250)

    def __str__(self):
        return "{}, R$ {} + {}".format(self.nome, self.preco, self.descricao)
