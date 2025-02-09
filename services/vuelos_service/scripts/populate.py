import django, os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vuelos_service.settings")
django.setup()

from vuelos.models import Vuelo

## vuelos data
vuelos_data = [
    {"origen": "Guayaquil", "destino": "Quito", "fecha": "2025-02-10", "hora": "08:30:00", "precio": 250.00, "disponibilidad": 50},
    {"origen": "Quito", "destino": "Cuenca", "fecha": "2025-02-12", "hora": "10:00:00", "precio": 212.00, "disponibilidad": 30},
    {"origen": "Manta", "destino": "Guayaquil", "fecha": "2025-02-15", "hora": "14:45:00", "precio": 55.00, "disponibilidad": 20},
    {"origen": "Guayaquil", "destino": "Loja", "fecha": "2025-02-18", "hora": "16:30:00", "precio": 85.00, "disponibilidad": 40},
    {"origen": "Cuenca", "destino": "Manta", "fecha": "2025-02-20", "hora": "09:00:00", "precio": 105.50, "disponibilidad": 25},
    {"origen": "Loja", "destino": "Quito", "fecha": "2025-02-22", "hora": "13:15:00", "precio": 300.00, "disponibilidad": 15},
    {"origen": "Quito", "destino": "Manta", "fecha": "2025-02-25", "hora": "18:45:00", "precio": 210.00, "disponibilidad": 35},
    {"origen": "Guayaquil", "destino": "Cuenca", "fecha": "2025-02-28", "hora": "20:00:00", "precio": 125.00, "disponibilidad": 10},
    {"origen": "Manta", "destino": "Loja", "fecha": "2025-03-02", "hora": "07:00:00", "precio": 179.99, "disponibilidad": 45},
    {"origen": "Loja", "destino": "Guayaquil", "fecha": "2025-03-05", "hora": "15:30:00", "precio": 160.00, "disponibilidad": 50}
]

for vuelo in vuelos_data:
    Vuelo.objects.get_or_create(**vuelo)

print("Vuelos creados con éxito")