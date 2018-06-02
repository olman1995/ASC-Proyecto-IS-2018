from ..modelo.Paciente import Paciente
from .DaoBDPaciente import DaoBDPaciente

'''
@package Control
Documentation for a class.
Clase GestorPaciente.
'''


class GestorPaciente:
    def __init__(self):
        # The constructor.
        self.paciente = Paciente()
        self.dao_db_pacinete = DaoBDPaciente()
    '''
    Documentation cargar_imagen.
    @param self :
    @param nombre : string
    @return true
    '''
    def cargar_imagen(self, nombre):
 #       self.paciente.img = Imagen()
        self.paciente.img.leer_imagen(nombre)
        return True
    '''
    Documentation estimar_edad.
    @param self :
    @return true
    '''
    def estimar_edad(self, sexo, url_imagen):
        resultado = self.paciente.estimar_edad(sexo, url_imagen)
        return resultado
    '''
    Documentation desplegar_edad.
    @param self :
    @return edad = int , estimacion_edad float
    '''
    def desplegar_edad(self):
        return self.paciente.edad, self.paciente.estimacion_edad
    '''
    Documentation guardar_informacion_paciente.
    @param self :
    @param datos : DTOPaciente
    @return true
    '''
    def guardar_informacion_paciente(self, datos):
        datos.estimacion_edad=self.paciente.estimacion_edad;
        self.dao_db_pacinete.guardar_informacion_paciente(datos)
        return True
