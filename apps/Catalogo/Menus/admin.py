from django.contrib import admin
from apps.Catalogo.Menus.models import Menu

@admin.register(Menu)
class MenusAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['nombre_platillo', 'descripcion','precio']
