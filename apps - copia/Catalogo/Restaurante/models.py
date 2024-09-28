from django.db import models

class Restaurante(models.Model):
    Nombre = models.CharField(verbose_name="Nombre", max_length=50)
    Direccion = models.CharField(verbose_name="Direccion", max_length=50)
    Telefono = models.CharField(verbose_name="Telefono", max_length=50)

    class Meta:
        verbose_name_plural = "Restaurantes"

    def __str__(self):
        return f'{self.Nombre} {self.Direccion} {self.Telefono}'
# Create your models here.
