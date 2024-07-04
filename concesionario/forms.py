from django import forms
from .models import Cotizacion

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['nombre_cliente', 'rut_cliente', 'telefono', 'direccion']
