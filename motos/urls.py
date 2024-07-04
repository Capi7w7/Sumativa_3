from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_motos, name='lista_motos'),
    path('<int:moto_id>/cotizar/', views.solicitar_cotizacion_moto, name='solicitar_cotizacion_moto'),
]
