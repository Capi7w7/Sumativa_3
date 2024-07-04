from django.shortcuts import redirect

def lista_motos(request):
    return redirect('lista_vehiculos')

def solicitar_cotizacion_moto(request, moto_id):
    return redirect('solicitar_cotizacion', 'moto', moto_id)
