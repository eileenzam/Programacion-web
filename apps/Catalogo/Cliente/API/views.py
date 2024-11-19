from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.Catalogo.Cliente.models import Cliente
from apps.Catalogo.Cliente.API.serializers import ClienteSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.seguridad.permission import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers

# Configura el logger
logger = logging.getLogger(__name__)


class ClientesAPIView(PaginationMixin, APIView):
    """
    Vista para listar todas los clientes o crear uno nuevo.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Cliente

    @swagger_auto_schema(responses={200: ClienteSerializer(many=True)})
    def get(self, request):
        """
        Listar todas los Clientes.
        """
        logger.info("GET request to list all Cliente")
        clientes = Cliente.objects.all()
        page = self.paginate_queryset(clientes, request)

        if page is not None:
            serializer = ClienteSerializer(page, many=True)
            logger.info("Paginated response for clientes")
            return self.get_paginated_response(serializer.data)

        serializer = ClienteSerializer(clientes, many=True)
        logger.error("Returning all Clientes without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ClienteSerializer, responses={201: ClienteSerializer})
    def post(self, request):
        """
        Crear un nuevo cliente
        """
        email = request.data.get('email')
        telefono = request.data.get('telefono')

        if Cliente.objects.filter(email=email).exists():
            logger.warning("El cliente ya existe con el email: %s", email)
            return Response({"detail": "El cliente ya existe con ese email."}, status=status.HTTP_400_BAD_REQUEST)

        if Cliente.objects.filter(telefono=telefono).exists():
            logger.warning("El cliente ya existe con el teléfono: %s", telefono)
            return Response({"detail": "El cliente ya existe con ese teléfono."}, status=status.HTTP_400_BAD_REQUEST)

        logger.info("POST request to create a new Cliente")

        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Cliente created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.error("Failed to create Cliente")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetails(APIView):
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Cliente

    @swagger_auto_schema(request_body=ClienteSerializer, responses={200: ClienteSerializer})
    def put(self, request, nombre):
        """
        Actualizar completamente un cliente por su nombre.
        """
        logger.info("PUT request to update Cliente with nombre: %s", nombre)
        clientes = get_object_or_404(Cliente, nombre=nombre)

        self.check_object_permissions(request, clientes)
        serializer = ClienteSerializer(clientes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Cliente updated successfully with nombre: %s", nombre)
            return Response(serializer.data)

        logger.error("Failed to update Cliente with nombre: %s. Errors: %s", nombre, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ClienteSerializer, responses={200: ClienteSerializer})
    def patch(self, request, nombre):
        """
        Actualizar parcialmente un cliente por su nombre.
        """
        logger.info("PATCH request to partially update Cliente with nombre: %s", nombre)
        clientes = get_object_or_404(Cliente, nombre=nombre)

        self.check_object_permissions(request, clientes)
        serializer = ClienteSerializer(clientes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Cliente partially updated successfully with nombre: %s", nombre)
            return Response(serializer.data)

        logger.error("Failed to partially update Cliente with nombre: %s. Errors: %s", nombre, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, nombre):
        """
        Eliminar un cliente por su nombre.
        """
        logger.info("DELETE request to delete Cliente with nombre: %s", nombre)
        clientes = get_object_or_404(Cliente, nombre=nombre)

        self.check_object_permissions(request, clientes)
        clientes.delete()
        logger.info("Cliente deleted successfully with nombre: %s", nombre)
        return Response(status=status.HTTP_204_NO_CONTENT)
