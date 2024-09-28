from django.db import models

class Menus(models.Model):
    NombrePlatillo = models.CharField(verbose_name="Nombre del Platillo", max_length=100, unique=True)
    Descripcion = models.CharField(verbose_name= "Descripcion", max_length=100)
    Precio = models.IntegerField(verbose_name="Precio")

    class Meta:
        verbose_name_plural = "Menus"

    def __str__(self):
        return f'{self.NombrePlatillo} - {self.Descripcion} - {self.Precio}'
# Create your models here.
