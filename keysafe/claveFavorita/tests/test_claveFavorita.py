import json
from typing import Self
from django.test import TestCase
from django.urls import reverse

from claveFavorita.models import clavesFavoritas

class test_claveFavorita(TestCase):

    @classmethod
    def setUptestData(cls):
        
        mi_claveFavorita= clavesFavoritas.objects.create(
            nombre='Luis',
            clave="Clave123456",
            pista= 'rojo'
        )
        
    def tearDown(self):
        pass 
    
    def test_consultar_claveFavoritas(self):
        response=self.client.get('/api/gestion-vehiculos/vehiculos')
        data=json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code,200)
        #self.assertGreater(len(data),0)
    
    def test_crear_vehiculos(self):
        
        
        response=self.client.post(
            '/api/gestion-vehiculos/vehiculos',
            data={
                'placa':'abc123',
                'modelo':'1999',
                'marca':'Renault',
                'color':'azul'
            }
        )
        self.assertEqual(response.status_code,201)
        vehiculo_filtrado=clavesFavoritas.objects.filter(placa='abc123').first()
        self.assertEqual(vehiculo_filtrado.marca,'Renault')
