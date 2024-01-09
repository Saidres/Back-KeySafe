from rest_framework import serializers
from claveFavorita.models import clavesFavoritas


class ClaveFavorita_serializer(serializers.ModelSerializer):
    class Meta:
        model = clavesFavoritas
        fields = ['nombre','clave','pista']