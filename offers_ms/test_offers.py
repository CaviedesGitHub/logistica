import json

from unittest import TestCase

from app import app

class testOffers(TestCase):

    def setUp(self):
        self.client=app.test_client()
        self.token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3NTczMTY3MywianRpIjoiOGU1OWJjZmQtNTJlYi00YzQ1LWI1NDUtZTU3MGYxMDBiNTQ0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MiwibmJmIjoxNjc1NzMxNjczLCJleHAiOjE2NzU3Mzg4NzN9.iPaNwx0Sp2TcPOyv5p12e7RyPAUDih3lrLxV0mVN43Q"
        self.tokenexpired="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3NTY4NDg3NiwianRpIjoiZjdkYzNlN2QtMzFhNy00NWZhLTg3NjItNzIwZDQ0NTUyMWZjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MiwibmJmIjoxNjc1Njg0ODc2LCJleHAiOjE2NzU2ODY2NzZ9.fPQFhAK_4k16NqpMGcT2eV-q-PQRUKHrLMiQY-xzDYM"
        self.userId=1
        self.offerId=1
        self.postId=1

    def test_ping(self):
        endpoint_ping='/offers/ping'
        solicitud_ping=self.client.get(endpoint_ping)
        respuesta_ping=json.loads(solicitud_ping.get_data())
        mensaje=respuesta_ping["Mensaje"]
        self.assertEqual(mensaje, "Pong")

    def test_valida_crear_oferta(self):
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }

        endpoint_ofertas='/offers/'

        nueva_oferta={
            "description": "Lorem Ipsum",
            "size": "MEDIUM",
            "fragile": False,
            "offer": 200
        }
        solicitud_nueva_oferta=self.client.post(endpoint_ofertas, 
                                                data=json.dumps(nueva_oferta), 
                                                headers=headers)
        respuesta_nueva_oferta=json.loads(solicitud_nueva_oferta.get_data())
        msg=respuesta_nueva_oferta["msg"]
        self.assertEqual(solicitud_nueva_oferta.status_code, 400)
        self.assertEqual(msg, "Falta la identificacion de la Publicacion.")

        nueva_oferta={
            "postId": 1,   
            "size": "MEDIUM",
            "fragile": False,
            "offer": 200
        }
        solicitud_nueva_oferta=self.client.post(endpoint_ofertas, 
                                                data=json.dumps(nueva_oferta), 
                                                headers=headers)
        respuesta_nueva_oferta=json.loads(solicitud_nueva_oferta.get_data())
        msg=respuesta_nueva_oferta["msg"]
        self.assertEqual(solicitud_nueva_oferta.status_code, 400)
        self.assertEqual(msg, "Falta la descripcion de la Publicacion.")

        nueva_oferta={
            "postId": 1,   
            "description": "Lorem Ipsum",
            "fragile": False,
            "offer": 200
        }
        solicitud_nueva_oferta=self.client.post(endpoint_ofertas, 
                                                data=json.dumps(nueva_oferta), 
                                                headers=headers)
        respuesta_nueva_oferta=json.loads(solicitud_nueva_oferta.get_data())
        msg=respuesta_nueva_oferta["msg"]
        self.assertEqual(solicitud_nueva_oferta.status_code, 400)
        self.assertEqual(msg, "Falta la dimension del paquete.")

        nueva_oferta={
            "postId": 1,   
            "description": "Lorem Ipsum",
            "size": "MEDIUM",
            "offer": 200
        }
        solicitud_nueva_oferta=self.client.post(endpoint_ofertas, 
                                                data=json.dumps(nueva_oferta), 
                                                headers=headers)
        respuesta_nueva_oferta=json.loads(solicitud_nueva_oferta.get_data())
        msg=respuesta_nueva_oferta["msg"]
        self.assertEqual(solicitud_nueva_oferta.status_code, 400)
        self.assertEqual(msg, "Falta la condicion del paquete.")


        nueva_oferta={
            "postId": 1,   
            "description": "Lorem Ipsum",
            "size": "MEDIUM",
            "fragile": False
        }
        solicitud_nueva_oferta=self.client.post(endpoint_ofertas, 
                                                data=json.dumps(nueva_oferta), 
                                                headers=headers)
        respuesta_nueva_oferta=json.loads(solicitud_nueva_oferta.get_data())
        msg=respuesta_nueva_oferta["msg"]
        self.assertEqual(solicitud_nueva_oferta.status_code, 400)
        self.assertEqual(msg, "Falta la oferta por llevar el paquete.")

        nueva_oferta={
            "postId": -1,   
            "description": "Lorem Ipsum",
            "size": "MEDIUM",
            "fragile": False,
            "offer": 200
        }
        solicitud_nueva_oferta=self.client.post(endpoint_ofertas, 
                                                data=json.dumps(nueva_oferta), 
                                                headers=headers)
        respuesta_nueva_oferta=json.loads(solicitud_nueva_oferta.get_data())
        msg=respuesta_nueva_oferta["msg"]
        self.assertEqual(solicitud_nueva_oferta.status_code, 412)
        self.assertEqual(msg, "Id de la publicacion es invalido.")

        nueva_oferta={
            "postId": 1,   
            "description": "Lorem Ipsum",
            "size": "OTRATALLA",
            "fragile": False,
            "offer": 200
        }
        solicitud_nueva_oferta=self.client.post(endpoint_ofertas, 
                                                data=json.dumps(nueva_oferta), 
                                                headers=headers)
        respuesta_nueva_oferta=json.loads(solicitud_nueva_oferta.get_data())
        msg=respuesta_nueva_oferta["msg"]
        self.assertEqual(solicitud_nueva_oferta.status_code, 412)
        self.assertEqual(msg, "Dimension del paquete incorrecta.")

        nueva_oferta={
            "postId": 1,   
            "description": "Lorem Ipsum",
            "size": "MEDIUM",
            "fragile": False,
            "offer": -200
        }
        solicitud_nueva_oferta=self.client.post(endpoint_ofertas, 
                                                data=json.dumps(nueva_oferta), 
                                                headers=headers)
        respuesta_nueva_oferta=json.loads(solicitud_nueva_oferta.get_data())
        msg=respuesta_nueva_oferta["msg"]
        self.assertEqual(solicitud_nueva_oferta.status_code, 412)
        self.assertEqual(msg, "El valor de la oferta es invalido.")


    def test_crear_oferta(self):
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }

        endpoint_ofertas='/offers/'

        nueva_oferta={
            "postId": 1,   
            "description": "Lorem Ipsum",
            "size": "MEDIUM",
            "fragile": False,
            "offer": 200
        }

        solicitud_nueva_oferta=self.client.post(endpoint_ofertas, 
                                                data=json.dumps(nueva_oferta), 
                                                headers=headers)
        print(solicitud_nueva_oferta.status_code)
        respuesta_nueva_oferta=json.loads(solicitud_nueva_oferta.get_data())
        self.offerId=int(respuesta_nueva_oferta["id"])
        print(respuesta_nueva_oferta)
        # OFFERID
        self.assertEqual(solicitud_nueva_oferta.status_code, 201)
    
    def test_consultar_oferta(self):
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }

        endpoint_ofertas='/offers/{}'.format(self.offerId)

        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        respuesta_nueva_oferta=json.loads(solicitud_oferta.get_data())
        print(respuesta_nueva_oferta)
        self.assertEqual(solicitud_oferta.status_code, 200)

    def test_consultar_oferta_inexistente(self):
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }

        endpoint_ofertas='/offers/{}'.format(999)

        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        respuesta_solicitud_oferta=json.loads(solicitud_oferta.get_data())
        msgError=respuesta_solicitud_oferta["Error"]
        self.assertEqual(solicitud_oferta.status_code, 404)
        self.assertEqual(msgError, "No existe oferta con ese Id")

    def test_consultar_oferta_idinvalido(self):
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }

        endpoint_ofertas='/offers/a'

        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        respuesta_solicitud_oferta=json.loads(solicitud_oferta.get_data())
        msgError=respuesta_solicitud_oferta["Error"]
        self.assertEqual(solicitud_oferta.status_code, 400)
        self.assertEqual(msgError, "El id de la Oferta no es un numero valido")


    def test_consultar_oferta_sintoken(self):
        headers={
            'Content-Type': 'application/json',
            'Authorization': ''
        }

        endpoint_ofertas='/offers/1'

        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        respuesta_solicitud_oferta=json.loads(solicitud_oferta.get_data())
        msgError=respuesta_solicitud_oferta["Error"]
        self.assertEqual(solicitud_oferta.status_code, 401)
        self.assertEqual(msgError, "Missing JWT")

    def test_consultar_oferta_contokenmalformado(self):
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'xyz12345678900987654321qwertyuioplkjhgfdsazxcvbnm'
        }

        endpoint_ofertas='/offers/{}'.format(self.offerId)

        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        respuesta_solicitud_oferta=json.loads(solicitud_oferta.get_data())
        print(respuesta_solicitud_oferta)
        msgError=respuesta_solicitud_oferta["Error"]
        self.assertEqual(solicitud_oferta.status_code, 401)
        self.assertEqual(msgError, "Missing JWT")

    def test_consultar_oferta_contokenexpirado(self):
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.tokenexpired)
        }

        endpoint_ofertas='/offers/{}'.format(self.offerId)

        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        respuesta_solicitud_oferta=json.loads(solicitud_oferta.get_data())
        msgError=respuesta_solicitud_oferta["Error"]
        self.assertEqual(solicitud_oferta.status_code, 401)
        self.assertEqual(msgError, "Token Expired")

    def test_valida_lista_ofertas(self):
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }

        endpoint_ofertas='/offers?post=a'
        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        respuesta_solicitud_oferta=json.loads(solicitud_oferta.get_data())
        #print(respuesta_solicitud_oferta)
        msgError=respuesta_solicitud_oferta["Error"]
        self.assertEqual(solicitud_oferta.status_code, 400)
        self.assertEqual(msgError, "El id de la publicacion no es un numero valido.")

        endpoint_ofertas='/offers?filter=tu'
        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        respuesta_solicitud_oferta=json.loads(solicitud_oferta.get_data())
        #print(respuesta_solicitud_oferta)
        msgError=respuesta_solicitud_oferta["Error"]
        self.assertEqual(solicitud_oferta.status_code, 400)
        self.assertEqual(msgError, "Valor de filtro invalido.")

        endpoint_ofertas='/offers'
        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        self.assertEqual(solicitud_oferta.status_code, 200)

        endpoint_ofertas='/offers?post={}'.format(self.postId)
        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        self.assertEqual(solicitud_oferta.status_code, 200)

        endpoint_ofertas='/offers?filter=me'
        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        self.assertEqual(solicitud_oferta.status_code, 200)

        endpoint_ofertas='/offers?post={}&filter=me'.format(self.postId)
        solicitud_oferta=self.client.get(endpoint_ofertas, headers=headers)
        self.assertEqual(solicitud_oferta.status_code, 200)
