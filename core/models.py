from django.db import models
# Create your models here.

ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('R', 'Realizado'),
    ]

class GestorPedidos(models.Model):
    numero_pedido = models.AutoField(primary_key=True)
    Total = models.CharField(max_length=254)
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES,
        default='P',
    )


class Producto(models.Model):
    imagen = models.ImageField(upload_to='productos', null=True)
    nombre = models.CharField(max_length=255)
    precio = models.CharField(max_length=255)



        