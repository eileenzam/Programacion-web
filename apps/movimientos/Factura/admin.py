from django.contrib import admin
from apps.movimientos.Factura.models import Factura, DetalleFactura

# @admin.register(Factura)
# class FacturaAdmin(admin.ModelAdmin):
#     search_fields = ('numero_factura',)
#     list_display = ('numero_factura', 'propina_general', 'descuento_general', 'numero_mesa', 'total')
#
# @admin.register(DetalleFactura)
# class DetalleFacturaAdmin(admin.ModelAdmin):
#     search_fields = ('cliente__Nombre', 'Menu__NombrePlatillo')
#     list_display = ('factura', 'Menu', 'subtotal')
#
# # Register your models here.
