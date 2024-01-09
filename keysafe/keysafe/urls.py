"""
URL configuration for keysafe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from registroUsuario import urls as usuarios_urls
from inicioSesion import urls as enteruser_urls
from gestionElementos import urls as gestionElementos_urls
from claveFavorita import urls as clavesFavoritas_urls
from reporteDeSeguridad import urls as reporteDeSeguridad_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registroUsuario/', include(usuarios_urls)),
    path('api/iniciarSesion/', include(enteruser_urls)),
    path('api/gestionElementos/', include(gestionElementos_urls)),
    path('api/clavesFavoritas/', include(clavesFavoritas_urls)),
    path('api/reporteDeSeguridad/', include(reporteDeSeguridad_urls))

]
    