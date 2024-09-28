from django.db import models

class Departamento(models.Model):
    NombreDepartamento = models.CharField(verbose_name="NombreDepartamento", max_length=50)
    CodigoDepartamento = models.CharField(verbose_name="CodigoDepartamento", max_length=50)

    class Meta:
        verbose_name_plural = 'Departamento'

    def __str__(self):
        return f'{self.NombreDepartamento} {self.CodigoDepartamento}'
# Create your models here.
