from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.Catalogo.Restaurante.models import Restaurante
from apps.Catalogo.Restaurante.API.serializers import RestauranteSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.seguridad.permission import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging

# Configura el logger
logger = logging.getLogger(__name__)

class RestauranteApiView(APIView, PaginationMixin):
    """
    Vista para listar y crear restaurantes.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Restaurante

    @swagger_auto_schema(responses={200: RestauranteSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los restaurantes.
        """
        logger.info("GET request to list all restaurantes")
        restaurantes = Restaurante.objects.all()
        page = self.paginate_queryset(restaurantes, request)

        if page is not None:
            serializer = RestauranteSerializer(page, many=True)
            logger.info("Paginated response for restaurantes")
            return self.get_paginated_response(serializer.data)

        serializer = RestauranteSerializer(restaurantes, many=True)
        logger.info("Returning all restaurantes without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RestauranteSerializer, responses={201: RestauranteSerializer})
    def post(self, request):
        """
        Crear un nuevo restaurante.
        """
        logger.info("POST request to create a new restaurante")
        serializer = RestauranteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Restaurante created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create restaurante")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestauranteDetails(APIView):
    """
    Vista para recuperar, actualizar y eliminar un restaurante por nombre.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Restaurante

    def get_object_by_nombre(self, nombre):
        return get_object_or_404(Restaurante, Nombre=nombre)

    @swagger_auto_schema(responses={200: RestauranteSerializer})
    def get(self, request, nombre):
        """
        Obtener detalles de un restaurante por nombre.
        """
        logger.info("GET request to retrieve Restaurante with Nombre: %s", nombre)
        restaurante = self.get_object_by_nombre(nombre)
        serializer = RestauranteSerializer(restaurante)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RestauranteSerializer, responses={200: RestauranteSerializer})
    def put(self, request, nombre):
        """
        Actualizar completamente un restaurante por nombre.
        """
        logger.info("PUT request to update Restaurante with Nombre: %s", nombre)
        restaurante = self.get_object_by_nombre(nombre)
        self.check_object_permissions(request, restaurante)
        serializer = RestauranteSerializer(restaurante, data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("Restaurante updated successfully with Nombre: %s", nombre)
            return Response(serializer.data)

        logger.error("Failed to update restaurante with Nombre: %s. Errors: %s", nombre, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=RestauranteSerializer, responses={200: RestauranteSerializer})
    def patch(self, request, nombre):
        """
        Actualizar parcialmente un restaurante por nombre.
        """
        logger.info("PATCH request to partially update Restaurante with Nombre: %s", nombre)
        restaurante = self.get_object_by_nombre(nombre)
        self.check_object_permissions(request, restaurante)
        serializer = RestauranteSerializer(restaurante, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            logger.info("Restaurante partially updated successfully with Nombre: %s", nombre)
            return Response(serializer.data)

        logger.error("Failed to partially update Restaurante with Nombre: %s. Errors: %s", nombre, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, nombre):
        """
        Eliminar un restaurante por nombre.
        """
        logger.info("DELETE request to delete Restaurante with Nombre: %s", nombre)
        restaurante = self.get_object_by_nombre(nombre)
        self.check_object_permissions(request, restaurante)
        restaurante.delete()
        logger.info("Restaurante deleted successfully with Nombre: %s", nombre)
        return Response(status=status.HTTP_204_NO_CONTENT)

