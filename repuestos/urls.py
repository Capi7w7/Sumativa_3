from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_repuestos, name='catalogo_repuestos'),
]
