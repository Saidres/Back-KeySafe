from django.http import JsonResponse
from rest_framework.views import APIView
from datetime import datetime, timedelta
from gestionElementos.models import Identificacion, tarjeta, Secreto, login
from rest_framework.response import Response
from claveFavorita.models import clavesFavoritas
import re
from django.db.models import Count


class ElementosProximosCaducidad(APIView):
    def get(self, request, *args, **kwargs):
        # Calcula la fecha actual
        hoy = datetime.now().date()
    
        # Calcula la fecha dentro de 3 meses
        tres_meses_despues = hoy + timedelta(days=90)
    
        # Filtra los elementos cuya fecha de vencimiento de clave está dentro de los próximos 3 meses
        elementos_tarjeta = tarjeta.objects.filter(fechaExpiracionClave__lte=tres_meses_despues).count()
        elementos_secreto = Secreto.objects.filter(fechaExpiracionClave__lte=tres_meses_despues).count()
        elementos_login = login.objects.filter(fechaExpiracionClave__lte=tres_meses_despues).count()
    
        return JsonResponse({
            'cantidad_tarjeta': elementos_tarjeta,
            'cantidad_secreto': elementos_secreto,
            'cantidad_login': elementos_login,
        })



class ClavesDuplicadas(APIView):
    def get(self, request, *args, **kwargs):
        claves_duplicadas = set()
        modelos_con_clave = [login, tarjeta, Secreto]

        for modelo in modelos_con_clave:
            campo_clave = 'clave'  # Asegúrate de ajustar el nombre del campo correcto
            claves = modelo.objects.values(campo_clave).annotate(count=Count(campo_clave))
            claves_duplicadas.update([item[campo_clave] for item in claves if item['count'] > 1])

        return Response({'claves_duplicadas': len(claves_duplicadas)})



class CantidadClavesFavoritasInseguras(APIView):
    def get(self, request, *args, **kwargs):
        claves_favoritas = clavesFavoritas.objects.all()
        claves_validas = []

        for clave_favorita in claves_favoritas:
            clave = clave_favorita.clave
            if (len(clave) >= 8 and re.search(r'\d', clave) and
                re.search(r'[A-Z]', clave) and re.search(r'[a-z]', clave)):
                claves_validas.append({'nombre': clave_favorita.nombre, 'clave': clave_favorita.clave, 'valida': True})
            else:
                claves_validas.append({'nombre': clave_favorita.nombre, 'clave': clave_favorita.clave, 'valida': False})

        return Response({'claves_favoritas_validas': claves_validas})

class NivelSeguridad(APIView):
    def get(self, request, *args, **kwargs):
        # Calcular el Porcentaje de Claves Seguras (SC)
        claves_favoritas = clavesFavoritas.objects.all()
        claves_validas = [clave_favorita for clave_favorita in claves_favoritas if
                         (len(clave_favorita.clave) >= 8 and re.search(r'\d', clave_favorita.clave) and
                          re.search(r'[A-Z]', clave_favorita.clave) and re.search(r'[a-z]', clave_favorita.clave))]
        porcentaje_claves_seguras = len(claves_validas) / len(claves_favoritas)

        # Llamar a la vista ElementosProximosCaducidad y recibir los datos
        elementos_proximos_data = ElementosProximosCaducidad().get(request)
        
        # Obtener las cantidades de elementos no vencidos de los datos recibidos
        cantidad_tarjeta = elementos_proximos_data.get('cantidad_tarjeta', 0)
        cantidad_secreto = elementos_proximos_data.get('cantidad_secreto', 0)
        cantidad_login = elementos_proximos_data.get('cantidad_login', 0)

        total_elementos = len(tarjeta.objects.all()) + len(Secreto.objects.all()) + len(login.objects.all())
        porcentaje_elementos_no_vencidos = 1 - (cantidad_tarjeta + cantidad_secreto + cantidad_login) / total_elementos

        # Obtener el resultado de la vista ClavesDuplicadas
        claves_duplicadas_data = ClavesDuplicadas().get(request)

        # Verificar si 'claves_duplicadas' está presente en el diccionario
        if 'claves_duplicadas' in claves_duplicadas_data and claves_duplicadas_data['claves_duplicadas'] > 0:
            porcentaje_claves_usadas_varias_veces = 0
        else:
            porcentaje_claves_usadas_varias_veces = 1


        # Calcular el Nivel de Seguridad
        nivel_seguridad = porcentaje_claves_seguras * 0.5 + porcentaje_elementos_no_vencidos * 0.2 + porcentaje_claves_usadas_varias_veces * 0.3

        return JsonResponse({'nivel_seguridad': nivel_seguridad * 100})






