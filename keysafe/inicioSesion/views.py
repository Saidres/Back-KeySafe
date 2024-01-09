from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login


class IniciarSesionApiView(APIView):
    def post(self, request, *args, **kwargs):
        
        nombre_usuario = request.data.get('nombre_usuario')
        contrasena = request.data.get('contrasena')

        usuario = authenticate(request, username=nombre_usuario, password=contrasena)

        if usuario is not None:
            login(request, usuario)

            token, _ = Token.objects.get_or_create(user=usuario)

            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'mensaje': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)