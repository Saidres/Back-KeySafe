from django.contrib import admin
from .models import clavesFavoritas

@admin.register(clavesFavoritas)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre','clave','pista']