from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.shortcuts import get_object_or_404
from apps.movimientos.Factura.models import Factura, DetalleFactura, Pago
from apps.Catalogo.Cliente.models import Cliente
from apps.Catalogo.Menus.models import Menu
from apps.Catalogo.MetodoPago.models import MetodoPago
from .serializers import FacturaSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from apps.seguridad.permission import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging

# Configura el logger
logger = logging.getLogger(__name__)


class FacturaListAPIView(PaginationMixin, APIView):
    """
    Vista para listar todas las facturas.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Factura

    @swagger_auto_schema(
        operation_summary="Listar todas las facturas",
        responses={200: FacturaSerializer(many=True)}
    )
    def get(self, request):
        logger.info("GET request para listar todas las facturas.")
        try:
            facturas = Factura.objects.all()
            page = self.paginate_queryset(facturas, request)

            if page is not None:
                serializer = FacturaSerializer(page, many=True)
                logger.info("Paginación aplicada en la lista de facturas.")
                return self.get_paginated_response(serializer.data)

            serializer = FacturaSerializer(facturas, many=True)
            logger.info("Devolviendo todas las facturas sin paginar.")
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error al listar facturas: {str(e)}")
            return Response({"Error": "Error al obtener las facturas."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FacturaDetailAPIView(APIView):
    """
    Vista para crear una nueva factura.
    """
    permission_classes = [IsAuthenticated, CustomPermission]

    @swagger_auto_schema(request_body=FacturaSerializer, responses={201: FacturaSerializer})
    def post(self, request):
        logger.info("POST request para crear una nueva factura.")
        serializer = FacturaSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    detalles_data = serializer.validated_data.pop('detalles')
                    metodo_pago_data = serializer.validated_data.pop('metodo_pago')

                    factura = Factura.objects.create(**serializer.validated_data)
                    logger.info(f"Factura creada con número: {factura.numero_factura}")

                    total_factura = 0
                    total_propina = 0
                    client_totals = {}

                    for detalle_data in detalles_data:
                        cliente = get_object_or_404(Cliente, id=detalle_data['cliente'].id)
                        menu_item = get_object_or_404(Menu, id=detalle_data['menu'].id)
                        cantidad = detalle_data['cantidad']
                        propina_individual = detalle_data.get('propina_individual', 0)
                        subtotal = (menu_item.precio * cantidad) + propina_individual

                        # Crear DetalleFactura
                        DetalleFactura.objects.create(
                            factura=factura,
                            cliente=cliente,
                            menu=menu_item,
                            cantidad=cantidad,
                            precio_unitario=menu_item.precio,
                            subtotal=subtotal,
                            propina_individual=propina_individual
                        )

                        logger.debug(f"DetalleFactura creado para cliente: {cliente.Nombre} - Subtotal: {subtotal}")

                        total_factura += subtotal
                        total_propina += propina_individual
                        client_totals[cliente.id] = client_totals.get(cliente.id, 0) + subtotal

                    factura.propina_general = total_propina
                    factura.total = total_factura - factura.descuento_general
                    factura.save()
                    logger.info(f"Total de factura calculado: {factura.total}")

                    metodo_pago_dict = {item['cliente']: item['metodo'] for item in metodo_pago_data}
                    for cliente_id, cliente_total in client_totals.items():
                        cliente = get_object_or_404(Cliente, id=cliente_id)
                        metodo_pago_id = metodo_pago_dict.get(cliente_id)

                        if not metodo_pago_id:
                            logger.error(f"No se proporcionó método de pago para el cliente {cliente.Nombre}")
                            return Response({"Error": f"Falta método de pago para el cliente {cliente.Nombre}"},
                                            status=status.HTTP_400_BAD_REQUEST)

                        metodo_pago = get_object_or_404(MetodoPago, id=metodo_pago_id)
                        Pago.objects.create(factura=factura, cliente=cliente, monto_pagado=cliente_total,
                                            metodo_pago=metodo_pago)
                        logger.info(f"Pago registrado para cliente: {cliente.Nombre}")

                    return Response(FacturaSerializer(factura).data, status=status.HTTP_201_CREATED)

            except Exception as e:
                logger.error(f"Error al crear la factura: {str(e)}")
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        logger.error(f"Datos inválidos para la factura: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
