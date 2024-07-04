from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CarritoCompras, ItemCarrito
from .forms import AgregarAlCarritoForm
from repuestos.models import Repuesto

@login_required
def agregar_al_carrito(request, repuesto_id):
    repuesto = Repuesto.objects.get(id=repuesto_id)
    carrito, created = CarritoCompras.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AgregarAlCarritoForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.repuesto = repuesto
            item.save()
            carrito.repuestos.add(item)
            return redirect('catalogo_repuestos')
    else:
        form = AgregarAlCarritoForm()
    return render(request, 'carrito/agregar_al_carrito.html', {'form': form, 'repuesto': repuesto})

@login_required
def ver_carrito(request):
    carrito, created = CarritoCompras.objects.get_or_create(user=request.user)
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito})
