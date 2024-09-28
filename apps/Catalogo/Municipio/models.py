from django.db import models

class Municipio(models.Model):
    NombreMunicipio = models.CharField(verbose_name="Nombre del Municipio", max_length=100)
    CodigoMunicipio = models.CharField(verbose_name="Codigo del Municipio", max_length=100)
    Departamento = models.CharField(verbose_name="Departamento", max_length=100)


    class Meta:
        verbose_name_plural = "Municipios"

    def __str__(self):
        return f'{self.NombreMunicipio} {self.CodigoMunicipio} {self.departamento}'
# Create your models here.
