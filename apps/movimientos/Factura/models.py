from django.db import models
from apps.Catalogo.Cliente.models import Cliente
from apps.Catalogo.Menus.models import Menu
from apps.Catalogo.MetodoPago.models import MetodoPago

class Factura(models.Model):
    numero_factura = models.CharField(max_length=20, unique=True)
    cliente_principal = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='facturas')
    propina_general = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    descuento_general = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    numero_mesa = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = "Facturas"

    def __str__(self):
        return f'Factura #{self.numero_factura} - Mesa: {self.numero_mesa}'

    def calcular_total(self):
        total_detalles = sum(detalle.subtotal for detalle in self.detalles.all())
        self.total = total_detalles - self.descuento_general
        self.propina_general = sum(detalle.propina_individual for detalle in self.detalles.all())
        self.save()

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, related_name='detalles', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='detalles')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2, editable=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    propina_individual = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'Detalles de Facturas'

    def save(self, *args, **kwargs):
        # Actualizar precio_unitario y subtotal automáticamente
        self.precio_unitario = self.menu.precio
        self.subtotal = (self.precio_unitario * self.cantidad) + self.propina_individual
        super().save(*args, **kwargs)
        # Actualizar el total de la factura
        self.factura.calcular_total()

    def __str__(self):
        return f'Cliente: {self.cliente} - Plato: {self.menu} - Subtotal: {self.subtotal}'

class Pago(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='pagos')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pagos')
    monto_pagado = models.DecimalField(max_digits=8, decimal_places=2)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.PROTECT)

    def __str__(self):
        return f'Pago {self.id} - Factura {self.factura.numero_factura} - {self.cliente.nombre}'