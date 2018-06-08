from django.test import TestCase

from ..back_end.control.DaoBDUsuario import  DaoBDUsuario
from ..back_end.control.DaoBDPaciente import DaoBDPaciente
from ..back_end.control.DTOPaciente import DTOPaciente
from ..back_end.control.Control import Control
from ..back_end.control.UIUsuario import UIUsuario
from ..back_end.control.Facade import Facade
from ..back_end.control.FacadeAdministrador import FacadeAdministrador
from ..back_end.control.FacedeMedico import FacadeMedico
from ..back_end.modelo.Estimador import Estimador

import os
import shutil
#from main.views import cargar_imagen
#click izquierdo en el proyecto
#>djang
#>>managepy. {custon}
#>>>test main


class DjangoTest(TestCase):
    
    
    
    def test_1(self):
        print("Test1: Agregar paciente")
        usuario = UIUsuario()
        usuario.ingresar("abc", "12345")
        f= usuario.facade
        dto_paciente = DTOPaciente(10,10," ","olman","castillo","picado","2324","nose")
        ret = f.guardar_informacion_paciente(dto_paciente) 
        self.assertEqual(ret,True, "Error al agregar paciente")        
        
    def test_2(self):
        print("Test2: Ver paciente")
        usuario = UIUsuario()
        usuario.ingresar("abc", "12345")
        f= usuario.facade
        dto_paciente = DTOPaciente(10,10," ","olman","castillo","picado","2324","nose")
        f.guardar_informacion_paciente(dto_paciente) 
        ret= f.cargar_informacion()
        print(ret.exists())
        self.assertEqual(ret.exists(),True, "Error al ver paciente")
    
    def test_3(self):
        print("Test2: Estimar")
        directory=os.path.split(os.path.abspath(__file__))[0]
        print(directory)
        #shutil.copyfile(src, dst)
        usuario = UIUsuario()
        usuario.ingresar("abc", "12345")
        f= usuario.facade
        directory=os.path.split(os.path.abspath(__file__))[0]+"\\test.png"
        ret= f.estimar_edad("F", directory)
        self.assertEqual(ret > 0,True, "Error valor < 0")
        
    def test_4(self):
        print("Test4: prueba")
        usuario = UIUsuario()
        usuario.ingresar("admin", "12345")
        f= usuario.facade
        k=2
        cant_img=2
        muestra={"id":[1414,1406,1394,1388,1412],"age":[78,106,57,126,156],"sex":["M","F","M","F","F"]}
        ret= f.cargar_muestra(muestra,k,cant_img)
        self.assertEqual(isinstance(ret,dict),True, "Error en la prueba")
        
        
        