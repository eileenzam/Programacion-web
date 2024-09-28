from django.contrib import admin
from apps.Catalogo.DetalleFactura.models import DetalleFactura

@admin.register(DetalleFactura)
class DetalleFacturaAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['NumeroFactura','NumeroMesa','MetodoPago','Descuento','Propina']

# Register your models here.
