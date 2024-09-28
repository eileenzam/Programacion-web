from django.contrib import admin
from apps.Catalogo.Mesero.models import Mesero

@admin.register(Mesero)
class MeseroAdmin(admin.ModelAdmin):
    search_fields = ['Id']
    list_display = ['NombreMesero','NumeroMesero','Fecha','Hora']
# Register your models here.
