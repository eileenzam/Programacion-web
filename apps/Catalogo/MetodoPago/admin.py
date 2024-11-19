from django.contrib import admin
from apps.Catalogo.MetodoPago.models import MetodoPago

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['id', 'nombre']
# Register your models here.
