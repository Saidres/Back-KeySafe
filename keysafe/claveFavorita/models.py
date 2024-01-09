from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class clavesFavoritas(models.Model):
    nombre=models.CharField(max_length=60)
    clave=models.CharField(max_length=30)
    pista=models.CharField(max_length=255)