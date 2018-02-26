from .GestorMuestra import GestorMuestra
from .GestorPaciente import GestorPaciente

##@package Control
#
#

## Documentation for a class.
#
#  Clase Control.
class Control:
    
    
    def __init__(self):
        ## The constructor.
        self.gestor_muestra=GestorMuestra()
    
    ## Documentation Cargar imagen.
    #  @param self : 
    #  @return true
    def cargar_imagen(self):
        return True
    
    ## Documentation estimar_edad.
    #  @param self : 
    #  @return true
    def estimar_edad(self):
        return True
    
    ## Documentation desplegar_edad.
    #  @param self : 
    #  @return true
    def desplegar_edad(self):
        return 0
    
    ## Documentation guardar_informacion_paciente.
    #  @param self : 
    #  @return true
    def guardar_informacion_paciente(self):
        return True
    
    ## Documentation Cargar_imagenes.
    #  @param self : 
    #  @return true
    def cargar_imagenes(self):
        return True
    
    ## Documentation Cargar_cvs.
    #  @param self : 
    #  @return true
    def cargar_cvs(self):
        return True
    
    ## Documentation clacular_MAE.
    #  @param self :
    #  @return true
    def calcular_MAE(self):
        return True
    
    ## Documentation Calcuar_MSE .
    #  @param self : 
    #  @return true
    def calcular_MSE(self):
        return True
    
        