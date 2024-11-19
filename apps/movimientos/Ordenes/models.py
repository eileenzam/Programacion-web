from django.db import models

class Ordenes(models.Model):
    DetalleMesa = models.CharField(verbose_name= 'DetalleMesa', max_length=6)

    class Meta:
        verbose_name = 'Ordenes'

    def __str__(self):
        return f'{self.DetalleMesa}'
