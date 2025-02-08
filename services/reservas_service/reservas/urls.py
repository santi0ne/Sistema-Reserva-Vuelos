from django.urls import path
from .views import CrearReserva, ListarReservas, CancelarReserva

urlpatterns = [
    path('reservas/crear/', CrearReserva.as_view(), name='crear_reserva'),
    path('reservas/', ListarReservas.as_view(), name='listar_reservas'),
    path('reservas/cancelar/<int:pk>/', CancelarReserva.as_view(), name='cancelar_reserva'),
]