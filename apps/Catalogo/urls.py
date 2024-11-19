from django.urls import path, include
urlpatterns = [
    path('Cliente/',include('apps.Catalogo.Cliente.API.urls')),
    path('Menus/',include('apps.Catalogo.Menus.API.urls')),
    path('Restaurante/',include('apps.Catalogo.Restaurante.API.urls')),
]