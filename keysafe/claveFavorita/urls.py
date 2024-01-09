from django.urls import path
from .views import ClavesFavoritasApiView

urlpatterns = [
    path('clavesFavoritas', ClavesFavoritasApiView.as_view(), name='clavesfavoritas-lista'),
    path('clavesFavoritas/<int:pkid>/', ClavesFavoritasApiView.as_view(), name='clavesFavoritas-detalles'),
    path('crear', ClavesFavoritasApiView.as_view(), name='clavesfavoritas-lista'),

]
