from django.shortcuts import redirect

def lista_autos(request):
    return redirect('lista_vehiculos')

def solicitar_cotizacion_auto(request, auto_id):
    return redirect('solicitar_cotizacion', 'auto', auto_id)
