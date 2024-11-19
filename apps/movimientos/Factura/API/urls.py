from django.urls import path
from .views import *

app_name = "Factura"

urlpatterns = [
    path('facturas/', FacturaListAPIView.as_view(), name='factura-list'),
    path('facturas/<int:pk>/', FacturaDetailAPIView.as_view(), name='factura-detail'),
]