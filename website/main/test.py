from django.test import TestCase

from .back_end.control.DaoBDUsuario import  DaoBDUsuario
from .back_end.control.DaoBDPaciente import DaoBDPaciente
from .back_end.control.DTOPaciente import DTOPaciente
from .back_end.control.Control import Control
from main.views import cargar_imagen
#click izquierdo en el proyecto
#>django
#>>managepy. {custon}
#>>>test main

class DjangoTest(TestCase):
    
    def test_1(self):
        print("Test1: Login")
        usuario = DaoBDUsuario()
        usuario.ingresar("olman", "12345")
    
    def test_2(self):
        print("Test2: Agregar paciente")
        dto_paciente = DTOPaciente(10,10," ","olman","castillo","picado",2324,"nose")
        paciente = DaoBDPaciente()
        paciente.guardar_informacion_paciente(dto_paciente)
    
    def test_3(self):
        print("Test3: Cargar imagen")
        imagen = Control()
        imagen.cargar_imagen("/website/main/media/upload") 
        