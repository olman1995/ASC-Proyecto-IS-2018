from .Control import Control
'''
@package Control
Documentation for a class.
Clase Facade.
'''


class Facade:
    def __init__(self):
        # The constructor.
        self.control = Control()
    '''
    Documentation Cargar imagen.
    @param self :
    @param nombre : string
    @return true
    '''
    def cargar_imagen(self, nombre):
        self.control.cargar_imagen()
        return True
    '''
    Documentation estimar_edad.
    @param self :
    @return true
    '''
    def estimar_edad(self, sexo, url_imagen):
        resultado = self.control.estimar_edad(sexo, url_imagen)
        return resultado
    '''
    Documentation desplegar_edad.
    @param self :
    @return true
    '''
    def desplegar_edad(self):
        return self.control.desplegar_edad()
    '''
    Documentation guardar_informacion_paciente.
    @param self :
    @param datos : DTOPaciente
    @return true
    '''
    def guardar_informacion_paciente(self, datos):
        self.control.guardar_informacion_paciente(datos)
        return True
    '''
    Documentation Cargar_imagenes.
    @param self :
    @param direccion : string
    @return true
    '''
    def cargar_muestra(self ,muestra,k,cant_img):
        resultado = self.control.cargar_muestra(muestra, k, cant_img)
        return resultado 
    