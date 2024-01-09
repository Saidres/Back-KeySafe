from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ClaveFavorita_serializer
from .models import clavesFavoritas
import json



# Create your views here.
class ClavesFavoritasApiView(APIView):
    
    def get(self,request,*args,**kwargs):
        lista_clavesFavoritas = clavesFavoritas.objects.all()
        serializador = ClaveFavorita_serializer(lista_clavesFavoritas,many=True)
        return Response(serializador.data,status=status.HTTP_200_OK)
    

    def post(self,request,*args,**kwargs):
        data={
            'nombre': request.data.get('nombre'),
            'clave': request.data.get('clave'),
            'pista': request.data.get('pista')
        }
        
        serializador = ClaveFavorita_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
        
    def put (self,request, pkid):
        my_claveFavorita=clavesFavoritas.objects.filter(id=pkid).update(
            nombre=request.data.get('nombre'),
            clave=request.data.get('clave'),
            pista=request.data.get('pista'),
        )
        return Response(None,status=status.HTTP_200_OK)
    
    
    def delete(self, request, pkid):
        try:
            claveFavorita = clavesFavoritas.objects.get(id=pkid)
            claveFavorita.delete() 
            return Response(status=status.HTTP_204_NO_CONTENT)
        except clavesFavoritas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)