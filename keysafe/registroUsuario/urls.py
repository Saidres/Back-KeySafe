from django.urls import path
from .views import UsuariosApiView


urlpatterns = [
    path('Usuarios',UsuariosApiView.as_view(), name = 'registro'),
    path('Usuario/<int:pkid>/', UsuariosApiView.as_view(), name='actualizar')
   
]
