from django.db import models

class Menu(models.Model):
    nombre_platillo = models.CharField(verbose_name="Nombre del Platillo", max_length=100, unique=True)
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    precio = models.DecimalField(verbose_name="Precio", max_digits=8, decimal_places=2)

    class Meta:
        verbose_name_plural = "Menús"

    def __str__(self):
        return f'{self.nombre_platillo} - {self.descripcion} - {self.precio}'
# Create your models here.
