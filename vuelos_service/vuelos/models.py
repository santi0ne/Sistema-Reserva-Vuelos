from django.db import models

class Vuelo(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    precio = models.FloatField()
    disponibilidad = models.IntegerField()

    def __str__(self):
        return f'{self.origen} -> {self.destino} ({self.fecha})'