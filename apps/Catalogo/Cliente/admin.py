from django.contrib import admin

from apps.Catalogo.Cliente.models import Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id','nombre', 'apellido', 'telefono', 'email']

# Register your models here.
