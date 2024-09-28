from django.db import models

from apps.Catalogo.MetodoPago.models import MetodoPago


class Factura(models.Model):
    NumeroFactura = models.IntegerField(verbose_name="NumeroFactura", max_length=60)
    Precio = models.IntegerField(verbose_name="Precio", max_length=60)
    Subtotal = models.IntegerField(verbose_name="Subtotal", max_length=60)
    Propina = models.IntegerField(verbose_name="Propina", max_length=60)
    MetodoPago = models.CharField(verbose_name='MetodoPago', max_length=60)
    Descuento = models.IntegerField(verbose_name="Descuento", max_length=60)

    class Meta:
        verbose_name_plural = "Facturas"

    def __str__(self):
        return f'{self.NumeroFactura} - {self.Precio} - {self.Subtotal} - {self.Propina} - {self.Descuento}'