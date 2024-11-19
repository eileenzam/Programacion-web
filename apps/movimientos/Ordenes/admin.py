from django.contrib import admin
from .models import Ordenes

@admin.register(Ordenes)
class OrdenesAdmin(admin.ModelAdmin):
    list_display = ('DetalleMesa',)  # Muestra el campo 'DetalleMesa' en la lista de objetos
    search_fields = ('DetalleMesa',)  # Permite buscar por el campo 'DetalleMesa'
    list_filter = ('DetalleMesa',)  # Filtro por el campo 'DetalleMesa'
