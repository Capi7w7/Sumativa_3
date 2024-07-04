from django.shortcuts import redirect

def lista_camionetas(request):
    return redirect('lista_vehiculos')

def solicitar_cotizacion_camioneta(request, camioneta_id):
    return redirect('solicitar_cotizacion', 'camioneta', camioneta_id)
