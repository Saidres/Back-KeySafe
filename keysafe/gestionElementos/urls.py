from rest_framework import routers
from .views import loginApiView, identificacionApiView, tarjetaApiView, secretoApiView
from django.urls import path

urlpatterns = [
    path('identificacion', identificacionApiView.as_view()),
    path('identificacion-actualizada/<pk>', identificacionApiView.as_view()),
    path('tarjeta', tarjetaApiView.as_view()),
    path('tarjeta-actualizada/<pk>', tarjetaApiView.as_view()),
    path('secreto', secretoApiView.as_view()),
    path('secreto-actualizado/<pk>', secretoApiView.as_view()),
    path('login', loginApiView.as_view()),
    path('login-actualizada/<pk>', loginApiView.as_view())
]