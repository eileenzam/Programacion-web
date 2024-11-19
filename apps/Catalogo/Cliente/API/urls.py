from django.urls import path
from .views import ClientesAPIView, ClienteDetails

urlpatterns = [
    path('', ClientesAPIView.as_view()),  # Para listar o crear departamentos
    path('<int:pk>', ClienteDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
]