# carrito/models.py
from django.db import models
from django.contrib.auth.models import User
from repuestos.models import Repuesto

class ItemCarrito(models.Model):
    repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.repuesto.nombre}"

class CarritoCompras(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    repuestos = models.ManyToManyField(ItemCarrito)
