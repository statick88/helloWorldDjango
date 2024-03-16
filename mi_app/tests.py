from django.test import TestCase, Client

class HelloWorldTest(TestCase):
    def setUp(self):
        # Crea un cliente de prueba
        self.client = Client()

    def test_hello_world(self):
        # Intenta hacer una solicitud GET a la página de hello world
        response = self.client.get('/mi_app/hello/')

        # Verifica que la respuesta es 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Verifica que el contenido de la respuesta sea "¡Hola Mundo!"
        self.assertContains(response, "¡Hola Mundo!")
