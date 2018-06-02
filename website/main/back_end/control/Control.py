from .GestorMuestra import GestorMuestra
from .GestorPaciente import GestorPaciente
'''
@package Control
Documentation for a class.
Clase Control.
'''


class Control:
    def __init__(self):
        # The constructor.
        self.gestor_muestra = GestorMuestra()
        self.gestor_paciente = GestorPaciente()
    '''
    Documentation Cargar imagen.
    @param self :
    @param nombre : string
    @return true
    '''
    def cargar_imagen(self, nombre):
        self.gestor_paciente.cargar_imagen(nombre)
        return True
    '''
    Documentation estimar_edad.
    @param self :
    @return true
    '''
    def estimar_edad(self, sexo, url_imagen):
        resultado = self.gestor_paciente.estimar_edad(sexo, url_imagen)
        return resultado
    '''
    Documentation desplegar_edad.
    @param self :
    @return edad : int, edad_estimadad : int
    '''
    def desplegar_edad(self):
        return self.gestor_paciente.desplegar_edad()
    '''
    Documentation guardar_informacion_paciente.
    @param self :
    @param datos : DTOPaciente
    @return true
    '''
    def guardar_informacion_paciente(self, datos):
        self.gestor_paciente.guardar_informacion_paciente(datos)
        return True
    '''
    Documentation Cargar_imagenes.
    @param self :
    @parma nombre : string
    @return true
    '''
    def cargar_muestra(self ,muestra,k,cant_img):
        resultado = self.gestor_muestra.cargar_muestra(muestra, k, cant_img)
        return resultado 
    