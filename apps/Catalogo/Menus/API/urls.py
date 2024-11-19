from django.urls import path
from .views import MenusAPIView, MenuDetails

urlpatterns = [
    path('', MenusAPIView.as_view()),  # Para listar Menus
    path('<int:pk>', MenuDetails.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
]

#from django.urls import path
#from rest_framework.routers import DefaultRouter
#from apps.Catalogo.Menus.API.views import MenusAPIView

#router = DefaultRouter()
#router.register('', MenusAPIView, basename='Menus')

#urlpatterns = [
#    path('', MenusAPIView.as_view()),
#]