from django.urls import path
from . import views

urlpatterns = [
    path('elementos-proximos-caducidad/', views.ElementosProximosCaducidad.as_view(), name='elementos_proximos_caducidad'),
    path('claves-duplicadas/', views.ClavesDuplicadas.as_view(), name='claves_duplicadas'),
    path('claves-favoritas/', views.CantidadClavesFavoritasInseguras.as_view(), name='claves_favoritas'),
    path('nivel-seguridad/', views.NivelSeguridad.as_view(), name='nivel_seguridad'),
]
