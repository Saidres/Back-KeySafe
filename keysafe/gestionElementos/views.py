from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializer import identificacion_serializer, tarjeta_serializer, secreto_serializer, login_serializer
from .models import Identificacion, tarjeta, Secreto, login
import json
import datetime


# Create your views here.
class identificacionApiView(APIView):
    def get(self, request, *args, **kwargs):
        lista_identificacion = Identificacion.objects.all()
        serializador = identificacion_serializer(lista_identificacion, many=True)
        return Response(serializador.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        now = datetime.datetime.now()        
        data = {
            'nombre': request.data.get('nombre'),
            'numeroIdentificacion': request.data.get('numeroIdentificacion'), 
            'nombreCompleto': request.data.get('nombreCompleto'),
            'fechaCumpleaños': request.data.get('fechaCumpleaños'), 
            'fechaExpedicion': request.data.get('fechaExpedicion'), 
            'nota': request.data.get('nota'), 
            'fechaExpiracionClave': now.date(),
        }
        serializador = identificacion_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try: 
            return Identificacion.objects.get(pk=pk)
        except Identificacion.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, fromat=None):
        Identificacion = self.get_object(pk)
        serializer = identificacion_serializer(Identificacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Identificacion = self.get_object(pk)
        Identificacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class tarjetaApiView(APIView):
    def get(self, request, *args, **kwargs):
        lista_tarjeta = tarjeta.objects.all()
        serializador = tarjeta_serializer(lista_tarjeta, many=True)
        return Response(serializador.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        data = {
            'nombre': request.data.get('nombre'),
            'numero': request.data.get('numero'), 
            'titular': request.data.get('titular'), 
            'fechaVencimiento': request.data.get('fechaVencimiento'),
            'cvc': request.data.get('cvc'),
            'clave': request.data.get('clave'), 
            'nota': request.data.get('nota'),
            'telefono': request.data.get('telefono'),
            'direccion': request.data.get('direccion'), 
            'fechaExpiracionClave': now.date(),
        }
        serializador = tarjeta_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try: 
            return tarjeta.objects.get(pk=pk)
        except tarjeta.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, fromat=None):
        tarjeta = self.get_object(pk)
        serializer = tarjeta_serializer(tarjeta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        tarjeta = self.get_object(pk)
        tarjeta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class secretoApiView(APIView):
    def get(self, request, *args, **kwargs):
        lista_secretos = Secreto.objects.all()
        serializador = secreto_serializer(lista_secretos, many=True)
        return Response(serializador.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        data = {
            'nombre': request.data.get('nombre'),
            'secreto': request.data.get('secreto'), 
            'clave': request.data.get('clave'),
            'nota': request.data.get('nota'),
            'fechaExpiracionClave': now.date(),
        }
        serializador = secreto_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try: 
            return Secreto.objects.get(pk=pk)
        except Secreto.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, fromat=None):
        Secreto = self.get_object(pk)
        serializer = secreto_serializer(Secreto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Secreto = self.get_object(pk)
        Secreto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class loginApiView(APIView):
    def get(self, request, *args, **kwargs):
        lista_login = login.objects.all()
        serializador = login_serializer(lista_login, many=True)
        return Response(serializador.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        data = {
            'nombre': request.data.get('nombre'),
            'nombreUsuario': request.data.get('nombreUsuario'),
            'correo': request.data.get('correo'),
            'clave': request.data.get('clave'),
            'nota': request.data.get('nota'),
            'fechaExpiracionClave': now.date(),
        }
        serializador = login_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try: 
            return login.objects.get(pk=pk)
        except login.DoesNotExist:
            raise Http404
    
    def put(self, request, pk, fromat=None):
        login = self.get_object(pk)
        serializer = login_serializer(login, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        login = self.get_object(pk)
        login.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
