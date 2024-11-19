from rest_framework import serializers
from apps.movimientos.Factura.models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido', 'telefono', 'email']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'nombre_platillo', 'descripcion', 'precio']

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ['id', 'nombre']

class MetodoPagoInputSerializer(serializers.Serializer):
    cliente = serializers.IntegerField()
    metodo = serializers.IntegerField()

class DetalleFacturaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    menu_nombre = serializers.CharField(source='menu.nombre_platillo', read_only=True)

    class Meta:
        model = DetalleFactura
        fields = [
            'id', 'cliente', 'cliente_nombre', 'menu', 'menu_nombre', 'cantidad',
            'precio_unitario', 'subtotal', 'propina_individual'
        ]
        read_only_fields = ['precio_unitario', 'subtotal']

class PagoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    metodo_pago_nombre = serializers.CharField(source='metodo_pago.nombre', read_only=True)

    class Meta:
        model = Pago
        fields = [
            'id', 'factura', 'cliente', 'cliente_nombre', 'monto_pagado',
            'metodo_pago', 'metodo_pago_nombre'
        ]

class FacturaSerializer(serializers.ModelSerializer):
    detalles = DetalleFacturaSerializer(many=True)
    pagos = PagoSerializer(many=True, read_only=True)
    metodo_pago = MetodoPagoInputSerializer(many=True, write_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    cliente_principal_nombre = serializers.CharField(source='cliente_principal.nombre', read_only=True)

    class Meta:
        model = Factura
        fields = [
            'id', 'numero_factura', 'cliente_principal', 'cliente_principal_nombre',
            'propina_general', 'descuento_general', 'numero_mesa', 'total',
            'detalles', 'pagos', 'metodo_pago'
        ]