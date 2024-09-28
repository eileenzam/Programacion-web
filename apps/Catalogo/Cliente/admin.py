from django.contrib import admin

from apps.Catalogo.Cliente.models import Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['Nombre', 'Apellido', 'Telefono', 'Email']

# Register your models here.
