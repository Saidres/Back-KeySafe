from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import Usuario_serializer
from .models import Usuario
import json

# Create your views here.

class UsuariosApiView(APIView):
    
    def get(self,request,*args,**kwargs):
        lista_usuarios = Usuario.objects.all()
        serializador = Usuario_serializer(lista_usuarios,many=True)
        return Response(serializador.data,status=status.HTTP_200_OK)
    

    def post(self,request,*args,**kwargs):
        data={
            'nombre_usuario': request.data.get('nombre_usuario'),
            'contrasena': request.data.get('contrasena')
        }
        
        serializador = Usuario_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
        
    def put (self,request, pkid):
        my_usuario=Usuario.objects.filter(id=pkid).update(
            nombre_usuario=request.data.get('nombre_usuario'),
            contrasena=request.data.get('contrasena'),
        )
        return Response(None,status=status.HTTP_200_OK)
