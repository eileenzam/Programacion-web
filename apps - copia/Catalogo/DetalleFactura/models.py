
from django.db import models
from apps.Catalogo.Factura.models import Factura

class DetalleFactura(models.Model):
    NumeroFactura = models.CharField(verbose_name='NumeroFactura', max_length=50)
    NumeroMesa = models.CharField(verbose_name='NumeroMesa', max_length=50)
    MetodoPago = models.CharField(verbose_name='MetodoPago',max_length=60)
    Descuento = models.CharField(verbose_name='Descuento',max_length=50)
    Propina = models.CharField(verbose_name='Propina',max_length=50)

    Factura = models.ForeignKey(Factura,verbose_name='Factura',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'DetalleFactura'



    def __str__(self):
        return f'{self.NumeroFactura} -{self.NumeroMesa}-{self.NumeroMesa}-{self.MetodoPago}-{self.Descuento}-{self.Propina}'
# Create your models here.
