from django.forms import ValidationError
import requests
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, AuthenticationFailed
from .models import Reserva
from .serializers import ReservaSerializer

VUELOS_SERVICE_URL = 'http://127.0.0.1:8001/api/vuelos/'

class CrearReserva(generics.CreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user_id = self.request.user.id
        vuelo_id = self.request.data.get('vuelo_id')
        token = self.request.auth

        # Debugging: Log the vuelo_id and URL
        print(f"vuelo_id: {vuelo_id}")
        print(f"URL: {VUELOS_SERVICE_URL}{vuelo_id}/")
        print(f"Token: {token}")

        headers = {"Authorization": f"Token {token}"}

        vuelo_response = requests.get(f'{VUELOS_SERVICE_URL}{vuelo_id}/', headers=headers)

        if vuelo_response.status_code == 401:
            raise AuthenticationFailed("No autorizado para consultar vuelos_service")

        if vuelo_response.status_code != 200:
            raise NotFound("El vuelo no existe en vuelos_service")
        
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=user_id, vuelo_id=vuelo_id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ListarReservas(generics.ListAPIView):
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return Reserva.objects.filter(user_id=user_id)
    
class CancelarReserva(generics.DestroyAPIView):
    queryset = Reserva.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        reserva = Reserva.objects.filter(id=self.kwargs['pk'], user_id=self.request.user.id).first()
        if not reserva:
            raise NotFound('Reserva no encontrada.')
        return reserva