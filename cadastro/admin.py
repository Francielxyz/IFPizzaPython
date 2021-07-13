from django.contrib import admin

from .models import Pedido, Produto, Pedido_Produto

# Register your models here.
admin.site.register(Pedido)
admin.site.register(Produto)
admin.site.register(Pedido_Produto)
