from rest_framework import serializers
from gestionElementos.models import login, Identificacion, tarjeta, Secreto

class identificacion_serializer (serializers.ModelSerializer):
    class Meta:
        model = Identificacion
        fields = '__all__'

class tarjeta_serializer (serializers.ModelSerializer):
    class Meta:
        model = tarjeta
        fields = '__all__'
    
class secreto_serializer (serializers.ModelSerializer):
    class Meta:
        model = Secreto
        fields = '__all__'

class login_serializer (serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'