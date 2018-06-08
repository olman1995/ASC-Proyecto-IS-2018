from .Facade import Facade
'''
@package Control
@version: 0.1.20
@author: Olman Castilla, Fernanda Alvarado y Yonnattan Serrano
Documentation for a class.
Clase FacadeMedico.
'''


class FacadeMedico(Facade):
    def __init__(self):
        # The constructor.
        Facade.__init__(self)
    '''
    Documentation Cargar imagen.
    @param self :
    @param nombre : string
    @return true
    '''
    def cargar_informacion (self):
        return Facade.cargar_informacion(self)
    
    def cargar_imagen(self, nombre):
        Facade.cargar_imagen(self, nombre)
        return True
    '''
    Documentation estimar.
    @param self
    @param sexo= F,M  solo acepta los valores de F y M
    @return float positvo
    '''
    def estimar_edad(self, sexo, url_imagen):
        resultado = Facade.estimar_edad(self, sexo, url_imagen)
        return resultado
    '''
    Documentation desplegar_edad.
    @param self :
    @return true
    '''
    def desplegar_edad(self):
        return Facade.desplegar_edad(self)
    '''
    Documentation guardar_informacion_paciente.
    @param self :
    @param datos : DTOPaciente
    @return true
    '''
    def guardar_informacion_paciente(self, datos):
        Facade.guardar_informacion_paciente(self, datos)
        return True
