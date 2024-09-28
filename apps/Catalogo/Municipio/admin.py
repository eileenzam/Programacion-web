from django.contrib import admin
from apps.Catalogo.Municipio.models import Municipio

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['NombreMunicipio','CodigoMunicipio','Departamento']
# Register your models here.
