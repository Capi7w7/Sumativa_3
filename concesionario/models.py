from django.db import models
from autos.models import Auto
from motos.models import Moto
from camionetas.models import Camioneta
from repuestos.models import Repuesto


class Cotizacion(models.Model):
    CATEGORIAS = [
        ('auto', 'Auto'),
        ('moto', 'Moto'),
        ('camioneta', 'Camioneta')
    ]
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='vehiculo')
    nombre_cliente = models.CharField(max_length=100)
    rut_cliente = models.CharField(max_length=12)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    vehiculo_auto = models.ForeignKey(Auto, on_delete=models.CASCADE, null=True, blank=True)
    vehiculo_moto = models.ForeignKey(Moto, on_delete=models.CASCADE, null=True, blank=True)
    vehiculo_camioneta = models.ForeignKey(Camioneta, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Cotización de {self.nombre_cliente} para {self.get_categoria_display()}"
