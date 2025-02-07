from django.urls import path
from .views import BuscarVuelos, CrearVuelo

urlpatterns = [
    path('vuelos/', BuscarVuelos.as_view(), name='buscar_vuelos'),
    path('crear/', CrearVuelo.as_view(), name='crear_vuelo'),
]