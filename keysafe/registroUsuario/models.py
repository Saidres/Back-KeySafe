from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario=models.CharField(max_length=60)
    contrasena=models.CharField(max_length=30)
