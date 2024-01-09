from django.urls import path
from .views import IniciarSesionApiView

urlpatterns = [
    path('iniciar-sesion', IniciarSesionApiView.as_view(), name='iniciar'),
]
