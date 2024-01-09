from django import forms
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import re

def validar_clave_segura(clave):
    if len(clave) < 8:
        raise ValidationError("La clave debe tener al menos 8 caracteres.")
    if not re.search(r'\d', clave):
        raise ValidationError("La clave debe incluir al menos un número.")
    if not re.search(r'[A-Z]', clave):
        raise ValidationError("La clave debe incluir al menos una letra mayúscula.")
    if not re.search(r'[a-z]', clave):
        raise ValidationError("La clave debe incluir al menos una letra minúscula.")
    # if not re.search(r'[?-*!@#$/(){}=.,;:]', clave):
        # raise ValidationError("La clave debe incluir al menos uno de los siguientes caracteres especiales: ? - * ! @ # $ / () {} = . , ;")


# Create your models here.

class login(models.Model):
    nombre = models.CharField(max_length=50)
    nombreUsuario = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    clave = models.CharField(max_length=50, validators=[validar_clave_segura])
    nota = models.CharField(max_length=500)
    fechaExpiracionClave = models.DateField()

class Identificacion(models.Model):
    nombre = models.CharField(max_length=50)
    numeroIdentificacion = models.CharField(max_length=20)
    nombreCompleto = models.CharField(max_length=80)
    fechaCumpleaños = models.DateField()
    fechaExpedicion = models.DateField()
    nota = models.CharField(max_length=500)
    fechaExpiracionClave = models.DateField()

class tarjeta(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.CharField(max_length=30)
    titular = models.CharField(max_length=30)
    fechaVencimiento = models.CharField(max_length=30)
    cvc = models.CharField(max_length=3)
    clave = models.CharField(max_length=50, validators=[validar_clave_segura])
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    nota = models.CharField(max_length=500)
    fechaExpiracionClave = models.DateField()

class Secreto(models.Model):
    nombre = models.CharField(max_length=50)
    secreto = models.CharField(max_length=50)
    clave = models.CharField(max_length=50, validators=[validar_clave_segura])
    nota = models.CharField(max_length=500)
    fechaExpiracionClave = models.DateField()


  


