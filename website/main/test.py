from django.test import TestCase

from .back_end.control.DaoBDUsuario import  DaoBDUsuario

#click izquierdo en el proyecto
#>django
#>>managepy. {custon}
#>>>test main

class DjangoTest(TestCase):
    
    def test_1(self):
        print("Test1: Login")
        usuario = DaoBDUsuario()
        usuario.ingresar("olman", "12345")