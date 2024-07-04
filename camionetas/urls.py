from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_camionetas, name='lista_camionetas'),
    path('<int:camioneta_id>/cotizar/', views.solicitar_cotizacion_camioneta, name='solicitar_cotizacion_camioneta'),
]
