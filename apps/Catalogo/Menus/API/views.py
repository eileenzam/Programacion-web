from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.Catalogo.Menus.models import Menu
from apps.Catalogo.Menus.API.serializers import MenusSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.seguridad.permission import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging

# Configura el logger
logger = logging.getLogger(__name__)

class MenusAPIView(PaginationMixin, APIView):
    """
    Vista para listar todos los Menús y crear nuevos.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Menu

    @swagger_auto_schema(responses={200: MenusSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los Menús
        """
        logger.info("GET request to list all Menús")
        menus = Menu.objects.all()
        page = self.paginate_queryset(menus, request)
        if page is not None:
            serializer = MenusSerializer(page, many=True)
            logger.info("Paginated response for Menús")
            return self.get_paginated_response(serializer.data)

        serializer = MenusSerializer(menus, many=True)
        logger.info("Returning all Menús without pagination")
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=MenusSerializer, responses={201: MenusSerializer})
    def post(self, request):
        """
        Crear un nuevo Menú
        """
        logger.info("POST request to create a new Menú")
        serializer = MenusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Menú created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.error("Failed to create Menú: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetails(APIView):
    """
    Vista para obtener, actualizar y eliminar Menús por nombre de platillo.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Menu

    @swagger_auto_schema(responses={200: MenusSerializer})
    def get(self, request, nombre_platillo):
        """
        Obtener un Menú por nombre de platillo.
        """
        logger.info("GET request for Menú with nombre_platillo: %s", nombre_platillo)
        menu = get_object_or_404(Menu, nombre_platillo=nombre_platillo)
        serializer = MenusSerializer(menu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=MenusSerializer, responses={200: MenusSerializer})
    def put(self, request, nombre_platillo):
        """
        Actualizar un Menú completamente por nombre de platillo.
        """
        logger.info("PUT request to update Menú with nombre_platillo: %s", nombre_platillo)
        menu = get_object_or_404(Menu, nombre_platillo=nombre_platillo)
        self.check_object_permissions(request, menu)
        serializer = MenusSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Menú updated successfully with nombre_platillo: %s", nombre_platillo)
            return Response(serializer.data, status=status.HTTP_200_OK)

        logger.error("Failed to update Menú with nombre_platillo: %s. Errors: %s", nombre_platillo, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MenusSerializer, responses={200: MenusSerializer})
    def patch(self, request, nombre_platillo):
        """
        Actualizar parcialmente un Menú por nombre de platillo.
        """
        logger.info("PATCH request to partially update Menú with nombre_platillo: %s", nombre_platillo)
        menu = get_object_or_404(Menu, nombre_platillo=nombre_platillo)
        self.check_object_permissions(request, menu)
        serializer = MenusSerializer(menu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Menú partially updated successfully with nombre_platillo: %s", nombre_platillo)
            return Response(serializer.data, status=status.HTTP_200_OK)

        logger.error("Failed to partially update Menú with nombre_platillo: %s. Errors: %s", nombre_platillo, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, nombre_platillo):
        """
        Eliminar un Menú por nombre de platillo.
        """
        logger.info("DELETE request to delete Menú with nombre_platillo: %s", nombre_platillo)
        menu = get_object_or_404(Menu, nombre_platillo=nombre_platillo)
        self.check_object_permissions(request, menu)
        menu.delete()
        logger.info("Menú deleted successfully with nombre_platillo: %s", nombre_platillo)
        return Response(status=status.HTTP_204_NO_CONTENT)
