# concesionario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('/home',views.home, name='home'),
    path('', views.landing, name='landing'),
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('cotizar/<str:categoria>/<int:vehiculo_id>/', views.solicitar_cotizacion, name='solicitar_cotizacion'),
]
