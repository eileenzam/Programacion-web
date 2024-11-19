from django.urls import path, include
urlpatterns = [
    path('Factura/', include('apps.movimientos.Factura.API.urls')),
    # path('Ordenes/', include('apps.movimientos.Ordenes.urls')),
]