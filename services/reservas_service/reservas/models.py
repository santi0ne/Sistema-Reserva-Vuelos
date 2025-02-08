from django.db import models

class Reserva(models.Model):
    user_id = models.IntegerField(null=True)
    vuelo_id = models.IntegerField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'Reserva de Usuario {self.user_id} en Vuelo {self.vuelo_id}'