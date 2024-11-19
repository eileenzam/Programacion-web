from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from apps.Catalogo.Cliente.models import Cliente
from apps.movimientos.Factura.API.views import logger
from apps.movimientos.Factura.models import Factura, DetalleFactura
from apps.movimientos.Factura.API.serializers import FacturaSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class FacturaAPIView(APIView):
    """
    Vista para listar todas las facturas, crear una nueva, actualizar y eliminar.
    """
    logger = logger.getLogger(__name__)

    @swagger_auto_schema(
        operation_summary="Listar todas las facturas",
        responses={200: FacturaSerializer(many=True)}
    )
    def get(self, request):
        """
        Listar todas las Facturas.
        """
        logger.info("GET request para listar todas las facturas.")
        try:
            facturas = Factura.objects.all()
            serializer = FacturaSerializer(facturas, many=True)
            logger.info(f"Facturas listadas correctamente, cantidad: {len(facturas)}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error al listar facturas: {str(e)}")
            return Response({"Error": "Error al obtener las facturas."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @swagger_auto_schema(request_body=FacturaSerializer, responses={201: FacturaSerializer})
    def post(self, request):
        """
        Crear una nueva Factura.
        """
        logger.info("POST request para crear una nueva factura.")
        serializer = FacturaSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                logger.info(f"Factura creada con éxito. Número: {serializer.instance.numero_factura}")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                logger.error(f"Error al crear la factura: {str(e)}")
                return Response({"Error": "Error al crear la factura."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        logger.warning(f"Datos inválidos para la factura: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Actualizar una factura existente",
        request_body=FacturaSerializer,
        responses={200: FacturaSerializer, 400: 'Bad Request', 404: 'Not Found'}
    )
    def patch(self, request, pk=None):
        """
        Actualizar una factura existente.
        """
        logger.info(f"PATCH request para actualizar la factura con ID: {pk}")
        factura = get_object_or_404(Factura, pk=pk)
        serializer = FacturaSerializer(factura, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
                logger.info(f"Factura con ID: {pk} actualizada correctamente.")
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                logger.error(f"Error al actualizar la factura con ID: {pk}: {str(e)}")
                return Response({"Error": f"Error al actualizar la factura con ID {pk}."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        logger.warning(f"Datos inválidos para la factura con ID {pk}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Eliminar una factura por su ID",
        responses={204: 'No Content', 404: 'Not Found'}
    )
    def delete(self, request, pk=None):
        """
        Eliminar una Factura por su ID.
        """
        logger.info(f"DELETE request para eliminar la factura con ID: {pk}")
        try:
            factura = get_object_or_404(Factura, pk=pk)
            factura.delete()
            logger.info(f"Factura con ID {pk} eliminada correctamente.")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error al eliminar la factura con ID {pk}: {str(e)}")
            return Response({"Error": f"Error al eliminar la factura con ID {pk}."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
