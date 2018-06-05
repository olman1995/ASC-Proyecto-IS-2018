from django.test import TestCase

from ..back_end.control.DaoBDUsuario import  DaoBDUsuario
from ..back_end.control.DaoBDPaciente import DaoBDPaciente
from ..back_end.control.DTOPaciente import DTOPaciente
from ..back_end.modelo.Paciente import Paciente
from ..back_end.modelo.Estimador import Estimador
import os
#from main.views import cargar_imagen
#click izquierdo en el proyecto
#>djang
#>>managepy. {custon}
#>>>test main

class DjangoTest(TestCase):
    
    def test_1(self):
        print("Test1: Login")
        usuario = DaoBDUsuario()
        usr,pas,tipo=usuario.ingresar("abc", "12345")
        
        self.assertEqual(usr,"", "Error usr")
        self.assertEqual(pas,"", "Error pas")
        self.assertEqual(tipo,-1, "Error tipo")
        
    def test_2(self):
        print("\n Test2: Agregar paciente \n")
        dto_paciente = DTOPaciente(10,10," ","olman","castillo","picado","2324","nose")
        paciente = DaoBDPaciente()
        ret=paciente.guardar_informacion_paciente(dto_paciente)
        self.assertEqual(ret,True, "Error no se guardo")
    
    def test_3(self):
        print("\n Test3: Cargar imagen \n")
        directory=os.path.split(os.path.abspath(__file__))[0]+"\\test.png"
        imagen = Paciente()
        ret=imagen.cargar_imagen(directory)
        self.assertEqual(ret,True, "Error no se guardo") 
    
    def test_4(self):
        print("\n Test4: Estimar \n")
        estimador = Estimador()
        valor=estimador.estimar("F")[0][0]
        self.assertEqual(valor > 0,True, "Error valor < 0")
        
        
        
        
        
        