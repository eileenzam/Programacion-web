from django.db import models

class Cliente(models.Model):
    Nombre = models.CharField(verbose_name= 'Nombre', max_length=6)
    Apellido = models.CharField(verbose_name= 'Apellido', max_length=6)
    Telefono = models.CharField(verbose_name= 'Telefono', max_length=6)
    Email = models.EmailField(verbose_name= 'Email')

    class Meta:
        verbose_name_plural = 'Cliente'

    def __str__(self):
        return f'{self.Nombre} {self.Apellido} {self.Telefono} {self.Email}'
# Create your models here.
