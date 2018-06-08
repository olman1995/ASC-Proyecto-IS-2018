from .GestorMuestra import GestorMuestra
from .GestorPaciente import GestorPaciente

'''
@package Control
@version: 0.1.20
@author: Olman Castilla, Fernanda Alvarado y Yonnattan Serrano
Documentation for a class.
Clase Control.
'''
__author__ = "Olman Castilla, Fernanda Alvarado y Yonnattan Serrano"
__version__ = "0.1.20"

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
    def cargar_informacion (self):
        return self.gestor_paciente.cargar_informacion()
    
    def cargar_imagen(self, nombre):
        return True
    '''
    Documentation estimar.
    @param self
    @param sexo= F,M  solo acepta los valores de F y M
    @return float positvo
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
    Documentation Cargar_Muestra.
    @param self
    @param muestra= dicionario de estructura {"id":[id_image],"edad":[edad],"sexo":[("f","M")]} ,cualquier otro valor
    @param k= entero positivo, cualquier otro valor
    @param cant_img= entero positivo, cualquier otro valor  
    @return resultado={"sub":self.sub_muestra,"mae":[],"mse":[],"res":[],"mean":[],"std":[],"var":[]}
    '''
    def cargar_muestra(self ,muestra,k,cant_img):
        resultado = self.gestor_muestra.cargar_muestra(muestra, k, cant_img)
        return resultado 
    