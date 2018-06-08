
from .Estimador import Estimador
import os
import shutil
'''
@package modelo
@version: 0.1.20
@author: Olman Castilla, Fernanda Alvarado y Yonnattan Serrano
Documentation for a class.
Clase Paciente.
'''


class Paciente:
    def __init__(self):
        # The constructor.
        self.edad = None
        self.sexo = None
        self.estimacion_edad = None
        self.url_imagen = None
        self.nombre = None
        self.apellido_1 = None
        self.apellido_2 = None
        self.cedula = None
        self.hospital = None
        self.estimador = Estimador()
    '''
    Documentation estimar.
    @param self
    sexo= [(F,M)]  solo acepta los valores de F y M
    @return float positvo
    '''
    def estimar_edad(self, sexo, url_imagen):
        self.sexo = sexo
        self.url_imagen = url_imagen
        self.estimacion_edad = self.estimador.estimar(sexo)[0][0]
        return self.estimacion_edad
    
