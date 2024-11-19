from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    apellido = models.CharField(verbose_name='Apellido', max_length=100)
    telefono = models.CharField(verbose_name='Teléfono', max_length=20)
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'