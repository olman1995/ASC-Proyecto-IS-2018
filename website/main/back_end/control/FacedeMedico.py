from .Facade import Facade

##@package Control
#
#

## Documentation for a class.
#
#  Clase FacadeMedico.
class FacadeMedico(Facade):
    
    def __init__(self):
        ## The constructor.
        Facade.__init__()

    ## Documentation Cargar imagen.
    #  @param self : 
    #  @param nombre : string
    #  @return true
    def cargar_imagen(self,nombre):
        Facade.cargar_imagen(self,nombre)
        return True

    ## Documentation estimar_edad.
    #  @param self : 
    #  @return true
    def estimar_edad(self):
        Facade.estimar_edad(self)
        return True

    ## Documentation desplegar_edad.
    #  @param self : 
    #  @return true
    def desplegar_edad(self):
        Facade.estimar_edad(self)
        return 0
    
    ## Documentation guardar_informacion_paciente.
    #  @param self : 
    #  @param datos : DTOPaciente
    #  @return true
    def guardar_informacion_paciente(self,datos):
        Facade.guardar_informacion_paciente(datos)
        return True
