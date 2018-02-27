from .Control import Control

##@package Control
#
#

## Documentation for a class.
#
#  Clase Facade.
class Facade:
    
    def __init__(self):
        ## The constructor.
        self.control=Control()
    
    ## Documentation Cargar imagen.
    #  @param self :
    #  @param nombre : string  
    #  @return true
    def cargar_imagen(self,nombre):
        self.control.cargar_imagen()
        return True
    
    ## Documentation estimar_edad.
    #  @param self : 
    #  @return true
    def estimar_edad(self):
        self.control.estimar_edad()
        return True
    
    ## Documentation desplegar_edad.
    #  @param self : 
    #  @return true
    def desplegar_edad(self):
        self.control.desplegar_edad()
        return 0
    
    ## Documentation guardar_informacion_paciente.
    #  @param self : 
    #  @param datos : DTOPaciente 
    #  @return true
    def guardar_informacion_paciente(self,datos):
        self.control.guardar_informacion_paciente(datos)
        return True
    
    ## Documentation Cargar_imagenes.
    #  @param self : 
    #  @param direccion : string
    #  @return true
    def cargar_imagenes(self,direccion):
        self.control.cargar_imagenes(direccion)
        return True
    
    ## Documentation Cargar_cvs.
    #  @param self : 
    #  @param nombre : string
    #  @return true
    def cargar_cvs(self,nombre):
        self.control.cargar_cvs(nombre)
        return True
        
    ## Documentation clacular_MAE.
    #  @param self :
    #  @return true
    def calcular_MAE(self):
        self.control.calcular_MAE()
        return True
    
    ## Documentation Calcuar_MSE .
    #  @param self : 
    #  @return true
    def calcular_MSE(self):
        self.control.calcular_MSE()
        return True