from django.contrib import admin
from .models import Auto, Moto, Camioneta, Cotizacion, Repuesto

admin.site.register(Auto)
admin.site.register(Moto)
admin.site.register(Camioneta)
admin.site.register(Repuesto)
admin.site.register(Cotizacion)