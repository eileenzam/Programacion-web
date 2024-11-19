from rest_framework import serializers
#from apps.Catalogo.Menus.models import Menu as Menus
from apps.Catalogo.Menus.models import Menu

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'