from django.shortcuts import render
from django.db import connection
from repuestos.models import Repuesto

def catalogo_repuestos(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM repuestos_repuesto")
        columnas = [col[0] for col in cursor.description]
        repuestos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    return render(request, 'repuestos/catalogo_repuestos.html', {'repuestos': repuestos})
