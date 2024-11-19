from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Catalogo.Restaurante.API.views import RestauranteApiView, RestauranteDetails

router = DefaultRouter()
router.register('', RestauranteApiView, basename='Restaurante')

urlpatterns = [
    path('', RestauranteApiView.as_view()),
    path('<int:pk>', RestauranteDetails.as_view()),
]