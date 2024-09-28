from django.db import models

class MetodoPago(models.Model):
    Tarjeta = models.CharField(verbose_name="Tarjeta", max_length=100)
    Transferencia = models.CharField(verbose_name="Transferencia", max_length=100)
    Efectivo = models.CharField(verbose_name="Efectivo", max_length=100)

    class Meta:
        verbose_name_plural = "MetodoPago"

    def __str__(self):
        return f'{self.Tarjeta} {self.Transferencia} {self.Efectivo}'

# Create your models here.
