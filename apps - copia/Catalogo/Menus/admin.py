from django.contrib import admin
from apps.Catalogo.Menus.models import Menus

@admin.register(Menus)
class MenusAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['NombrePlatillo', 'Descripcion','Precio']
# Register your models here.
