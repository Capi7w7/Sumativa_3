# concesionario/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from autos.models import Auto
from motos.models import Moto
from camionetas.models import Camioneta
from .forms import CotizacionForm

def home(request):
    return render(request, 'concesionario/home.html')

def landing(request):
    return render(request, 'concesionario/landing.html')

def lista_vehiculos(request):
    autos = Auto.objects.all()
    motos = Moto.objects.all()
    camionetas = Camioneta.objects.all()
    return render(request, 'concesionario/lista_vehiculos.html', {
        'autos': autos,
        'motos': motos,
        'camionetas': camionetas
    })

def solicitar_cotizacion(request, categoria, vehiculo_id):
    if categoria == 'auto':
        vehiculo = Auto.objects.get(id=vehiculo_id)
    elif categoria == 'moto':
        vehiculo = Moto.objects.get(id=vehiculo_id)
    elif categoria == 'camioneta':
        vehiculo = Camioneta.objects.get(id=vehiculo_id)
    else:
        return redirect('lista_vehiculos')
    
    if request.method == 'POST':
        form = CotizacionForm(request.POST)
        if form.is_valid():
            cotizacion = form.save(commit=False)
            if categoria == 'auto':
                cotizacion.vehiculo_auto = vehiculo
            elif categoria == 'moto':
                cotizacion.vehiculo_moto = vehiculo
            elif categoria == 'camioneta':
                cotizacion.vehiculo_camioneta = vehiculo
            cotizacion.save()
            return redirect('lista_vehiculos')
    else:
        form = CotizacionForm()
    return render(request, 'concesionario/solicitar_cotizacion.html', {'form': form, 'vehiculo': vehiculo, 'categoria': categoria})
