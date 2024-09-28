from django.contrib import admin
from apps.Catalogo.Mesa.models import Mesa

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    search_fields = ['Id']
    list_display = ['NumeroMesas', 'CapacidadMesas']
# Register your models here.
