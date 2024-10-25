from django.contrib import admin
from .models import GestorPedidos

# Register your models here.

from .models import GestorPedidos, Producto

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('numero_pedido', 'Total', 'estado')  
    list_filter = ('estado',)  

admin.site.register(GestorPedidos, PedidoAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')  
    search_fields = ('nombre',)  

admin.site.register(Producto, ProductoAdmin)  
