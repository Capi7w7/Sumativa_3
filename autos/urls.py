from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_autos, name='lista_autos'),
    path('<int:auto_id>/cotizar/', views.solicitar_cotizacion_auto, name='solicitar_cotizacion_auto'),
]
