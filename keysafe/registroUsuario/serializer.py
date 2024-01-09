from rest_framework import serializers
from registroUsuario.models import Usuario


class Usuario_serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario','contrasena']