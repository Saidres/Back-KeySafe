import json
from typing import Self
from django.test import TestCase
from django.urls import reverse

from registroUsuario.models import Usuario


from gestionElementos.models import Identificacion, Secreto, tarjeta, login

class test_identificacion(TestCase):
    #metodo de clase
    @classmethod
    def setUptestData(cls):
  
        mi_identificacion = Identificacion.objects.create(
            nombre = 'diana',
            numeroIdentificacion = 12345678,
            nombreCompleto = 'diana rosero',
            fechaCumpleaños = '20-05-1997',
            fechaExpedicion = '20-05-2024',
            nota = 'sin observacion',
            #fechaExpiracionClave = '20-12-2023'
        )
        
        
    def tearDown(self):
        pass 
    
    def test_consultar_identificacion(self):
        response=self.client.get('api/gestionElementos/identificacion')
        data=json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code,200)
        #self.assertGreater(len(data),0)
    
    def test_crear_identificacion(self):
        
        
        response=self.client.post(
            'api/gestionElementos/identificacion',
            data={
                'nombre':'diana',
                'numeroIdentificacion':'12345678',
                'nombreCompleto':'diana rosero',
                'fechaCumpleaños':'20-05-1997',
                'fechaExpedicion':'20-05-2024',
                'nota':'sin observacion', 
                #'fechaExpiracionClave':'20-12-2023'
            }
        )
        self.assertEqual(response.status_code,201)
        identificacion_filtrado=Identificacion.objects.filter(nombre='diana').first()
        self.assertEqual(identificacion_filtrado.numeroIdentificacion,'12345678')
       
    def test_actualizar_identificacion(self):
        identificacion=identificacion.objects.create(
            nombre = 'santiago',
            numeroIdentificacion = 9876529,
            nombreCompleto = 'santiago chamorro',
            fechaCumpleaños = '20-05-2000',
            fechaExpedicion = '20-05-2018',
            nota = 'sin observacion',
            #fechaExpiracionClave = '01-01-2024'
           )
        url=reverse('actualizar_identificacion', kwargs={'pkid':Identificacion.id})
        identificacion_modificada={
            'nombre':'diana rosero',
            'numeroIdentificacion':'12399678',
            'nombreCompleto':'diana carolina rosero bastidas',
            'fechaCumpleaños':'20-05-1998',
            'fechaExpedicion':'20-06-2016',
            'nota':'sin observacion', 
            #'fechaExpiracionClave':'20-12-2023'
        }
        
        identificacion_json = json.dumps(identificacion_modificada)
        response=self.client.put(url,identificacion_json,content_type='application/json')
        self.assertEqual(response.status_code,200)
        
class test_login(TestCase):
    #metodo de clase
    @classmethod
    def setUptestData(cls):
  
        mi_login = login.objects.create(
            nombre = 'diana',
            nombreUsuario = 'dianarosero01',
            correo = 'diana123@admin.com',
            clave = 'Diana-1234',
            nota = 'sin observaciones',
            #fechaExpiracionClave = '01-01-2023'
        )
        
        
    def tearDown(self):
        pass 
    
    def test_consultar_login(self):
        response=self.client.get('api/gestionElementos/login')
        data=json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code,200)
        #self.assertGreater(len(data),0)
    
    def test_crear_login(self):
        
        
        response=self.client.post(
            'api/gestionElementos/login',
            data={
                'nombre':'david',
                'nombreUsuario':'daviacost01',
                'correo':'david345@admin.com',
                'clave':'David-1234',
                'nota':'sin observaciones',
                #'fechaExpiracionClave':'01-02-2023'
            }
        )
        self.assertEqual(response.status_code,201)
        login_filtrado=login.objects.filter(nombreUsuario='daviacost01').first()
        self.assertEqual(login_filtrado.nombre,'david')
       
    def test_actualizar_login(self):
        login=login.objects.create(
            nombre = 'diana',
            nombreUsuario = 'dianarosero01',
            correo = 'diana123@admin.com',
            clave = 'diana-1234',
            nota = 'sin observaciones',
            #fechaExpiracionClave = '01-01-2023'
           )
        url=reverse('actualizar_login', kwargs={'pkid':login.id})
        login_modificado={
            'nombre':'diana carolina',
            'nombreUsuario':'dianarosero01',
            'correo':'diana123@admin.com',
            'clave':'diana-1234',
            'nota':'sin observaciones',
            #'fechaExpiracionClave':'01-01-2023'
        }
        
        login_json = json.dumps(login_modificado)
        response=self.client.put(url,login_json,content_type='application/json')
        self.assertEqual(response.status_code,200)
        

class test_tarjeta(TestCase):
    #metodo de clase
    @classmethod
    def setUptestData(cls):
  
        mi_tarjeta = tarjeta.objects.create(
            nombre = 'diana',
            numero = '879-000001-01',
            titular = 'diana carolina rosero',
            fechaVencimiento = '01-02-2023',
            cvc = '123',
            clave = 'Diana-1234',
            telefono = '1234567890',
            direccion = 'avenida123',
            nota = 'sin observaciones',
            #fechaExpiracionClave = '23-01-2023'
        )
        
        
    def tearDown(self):
        pass 
    
    def test_consultar_tarjeta(self):
        response=self.client.get('api/gestionElementos/tarjeta')
        data=json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code,200)
        #self.assertGreater(len(data),0)
    
    def test_crear_tarjeta(self):
        
        
        response=self.client.post(
            'api/gestionElementos/tarjeta',
            data={
                'nombre':'david',
                'numero':'879-000001-02',
                'titular':'david acosta',
                'fechaVencimiento':'01-04-2023',
                'cvc':'456',
                'clave':'David-1234',
                'telefono':'3124567809',
                'direccion':'avenida678',
                'nota':'sin observaciones',
                #'fechaExpiracionClave':'23-08-2023'
            }
        )
        self.assertEqual(response.status_code,201)
        tarjeta_filtrado=tarjeta.objects.filter(nombre='david').first()
        self.assertEqual(tarjeta_filtrado.numero,'879-000001-02')
       
    def test_actualizar_tarjeta(self):
        tarjeta=tarjeta.objects.create(
            nombre = 'diana bastidas',
            numero = '879-000401-01',
            titular = 'diana carolina rosero',
            fechaVencimiento = '01-02-2023',
            cvc = '123',
            clave = 'Diana-1234',
            telefono = '1234567890',
            direccion = 'avenida123',
            nota = 'sin observaciones',
            #fechaExpiracionClave = '23-01-2023'
           )
        url=reverse('actualizar_tarjeta', kwargs={'pkid':login.id})
        tarjeta_modificada={
            'nombre':'diana bastidas',
            'numero':'879-000401-01',
            'titular':'diana carolina rosero',
            'fechaVencimiento':'01-02-2023',
            'cvc':'123',
            'clave':'Diana-1234',
            'telefono':'1234567890',
            'direccion':'avenida123',
            'nota':'sin observaciones',
            #'fechaExpiracionClave':'23-01-2023'
        }
        
        tarjeta_json = json.dumps(tarjeta_modificada)
        response=self.client.put(url,tarjeta_json,content_type='application/json')
        self.assertEqual(response.status_code,200)
        
        
class test_secreto(TestCase):
    #metodo de clase
    @classmethod
    def setUptestData(cls):
  
        mi_secreto = Secreto.objects.create(
            nombre = 'diana',
            secreto = 'mi testamento',
            clave = 'miTestamento1234',
            nota = 'sin observaciones',
            #fechaExpiracionClave = '01-01-2023'
        )
        
        
    def tearDown(self):
        pass 
    
    def test_consultar_secreto(self):
        response=self.client.get('api/gestionElementos/secreto')
        data=json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code,200)
        #self.assertGreater(len(data),0)
    
    def test_crear_secreto(self):
        
        
        response=self.client.post(
            'api/gestionElementos/secreto',
            data={
                'nombre':'lorena',
                'secreto':'mi cuenta de FNA',
                'clave':'miCuentaFna1234',
                'nota':'sin observaciones',
                #'fechaExpiracionClave':'01-06-2023'
            }
        )
        self.assertEqual(response.status_code,201)
        secreto_filtrado=Secreto.objects.filter(nombre='lorena').first()
        self.assertEqual(secreto_filtrado.secreto,'mi cuenta de FNA')
       
    def test_actualizar_secreto(self):
        Secreto=Secreto.objects.create(
            nombre = 'diana rosero bastidas',
            secreto = 'mi testamento',
            clave = 'miTestamento1234',
            nota = 'notaria123',
            #fechaExpiracionClave = '01-01-2023'
           )
        url=reverse('actualizar_tarjeta', kwargs={'pkid':login.id})
        secreto_modificado={
            'nombre':'diana rosero bastidas',
            'secreto':'mi testamento',
            'clave':'miTestamento1234',
            'nota':'notaria123',
            #'fechaExpiracionClave':'01-01-2023'
        }
        
        secreto_json = json.dumps(secreto_modificado)
        response=self.client.put(url,secreto_json,content_type='application/json')
        self.assertEqual(response.status_code,200)
 
        
#Test Registro usuario

class test_usuario(TestCase):
    #metodo de clase
    @classmethod
    def setUptestData(cls):
        #creando un usuario para verificar que cuando se ejecute la prueba 
        #al menos exista un usuario en la repsuesta
        mi_usuario= Usuario.objects.create(
            nombre_usuario='Edison Narvaez',
            contrasena='Edison123'
        )
        
        
    def tearDown(self):
        pass 
    
    def test_consultar_usuario(self):
        response=self.client.get('/api/registroUsuario/Usuarios')
        data=json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code,200)
        #self.assertGreater(len(data),0)
    
    def test_crear_usuario(self):
        
        
        response=self.client.post(
            '/api/registroUsuario/Usuarios',
            data={
                'nombre_usuario':'Santiago',
                'contrasena':'Santiago123'
            }
        )
        self.assertEqual(response.status_code,201)
        usuarioo_filtrado=Usuario.objects.filter(nombre_usuario='Santiago').first()
        self.assertEqual(usuarioo_filtrado.contrasena,'Santiago123')
       
    def test_actualizar_usuario(self):
        usuario=Usuario.objects.create(
               nombre_usuario='Diana',
               contrasena='Diana123'
           )
        url=reverse('actualizar_usuario', kwargs={'pkid':usuario.id})
        usuario_modificado={
            'nombre_usuario':'Diana',
            'contrasena':'Diana789'
        }
        usuario_json = json.dumps(usuario_modificado)
        response=self.client.put(url,usuario_json,content_type='application/json')
        self.assertEqual(response.status_code,200)        
        
