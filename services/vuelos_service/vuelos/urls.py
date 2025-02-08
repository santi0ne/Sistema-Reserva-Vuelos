from django.urls import path
from .views import BuscarVuelos, CrearVuelo, ObtenerVuelo

urlpatterns = [
    path('vuelos/', BuscarVuelos.as_view(), name='buscar_vuelos'),
    path('vuelos/crear/', CrearVuelo.as_view(), name='crear_vuelo'),
    path('vuelos/<int:pk>/', ObtenerVuelo.as_view(), name='obtener_vuelo'),
]