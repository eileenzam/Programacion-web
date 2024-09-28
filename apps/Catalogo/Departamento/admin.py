from django.contrib import admin

from apps.Catalogo.Departamento.models import Departamento
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['CodigoDepartamento', 'NombreDepartamento']
# Register your models here.
