from django.db import models

class Mesero(models.Model):
    NombreMesero = models.CharField(max_length=50)
    NumeroMesero = models.IntegerField()
    Fecha = models.DateField()
    Hora = models.TimeField()
    def __str__(self):
        return self.NombreMesero
# Create your models here.
