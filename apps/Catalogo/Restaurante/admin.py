from django.contrib import admin
from apps.Catalogo.Restaurante.models import Restaurante

@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['Nombre', 'Direccion','Telefono']
# Register your models here.
