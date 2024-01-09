from django.contrib import admin
from .models import login, Secreto, Identificacion, tarjeta

# Registra tus modelos aquí.

@admin.register(login)
class loginAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nombreUsuario', 'correo', 'clave', 'nota', 'fechaExpiracionClave']

@admin.register(Secreto)
class SecretoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'secreto', 'clave', 'nota', 'fechaExpiracionClave']

@admin.register(tarjeta)
class tarjetaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero', 'titular', 'fechaVencimiento', 'cvc', 'clave', 'nota', 'telefono', 'direccion', 'fechaExpiracionClave']
    
@admin.register(Identificacion)
class IdentificacionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numeroIdentificacion', 'nombreCompleto', 'fechaCumpleaños', 'fechaExpedicion', 'nota', 'fechaExpiracionClave']



