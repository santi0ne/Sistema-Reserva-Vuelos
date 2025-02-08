from rest_framework import generics, permissions
from .models import Vuelo
from .serializers import VueloSerializer

class BuscarVuelos(generics.ListCreateAPIView):
    serializer_class = VueloSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        origen = self.request.query_params.get('origen')
        destino = self.request.query_params.get('destino')
        fecha = self.request.query_params.get('fecha')
        
        queryset = Vuelo.objects.all()
        if origen:
            queryset = queryset.filter(origen=origen)
        if destino:
            queryset = queryset.filter(destino=destino)
        if fecha:
            queryset = queryset.filter(fecha=fecha)

        return queryset
    
class CrearVuelo(generics.CreateAPIView):
    queryset = Vuelo.objects.all()
    serializer_class = VueloSerializer
    permission_classes = [permissions.IsAdminUser]

class ObtenerVuelo(generics.RetrieveAPIView):
    queryset = Vuelo.objects.all()
    serializer_class = VueloSerializer
    permission_classes = [permissions.IsAuthenticated]