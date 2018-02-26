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
    #  @return true
    def cargar_imagen(self):
        Facade.cargar_imagen(self)
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
    #  @return true
    def guardar_informacion_paciente(self):
        Facade.guardar_informacion_paciente(self)
        return True
