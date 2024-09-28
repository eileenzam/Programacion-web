from django.db import models

class Mesa(models.Model):
    NumeroMesas = models.CharField(verbose_name="NumeroMesas", max_length=100)
    CapacidadMesas = models.CharField(verbose_name="CapacidadMesas",max_length=60)

    class Meta:
        verbose_name_plural = "Mesa"

    def __str__(self):
        return f'{self.NumeroMesas} - {self.CapacidadMesas}'
# Create your models here.
