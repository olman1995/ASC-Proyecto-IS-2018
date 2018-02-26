from .Facade import Facade

##@package Control
#
#

## Documentation for a class.
#
#  Clase FacadeAdministrador.
class FacadeAdministrador(Facade):
    
    def __init__(self):
        ## The constructor.
        Facade.__init__(self)
    
    ## Documentation Cargar imagenes.
    #  @param self : 
    #  @return true
    def cargar_imagenes(self):
        Facade.cargar_imagenes(self)
        return True
    
    ## Documentation Cargar_cvs.
    #  @param self : 
    #  @return true    
    def cargar_cvs(self):
        Facade.cargar_cvs(self)
        return True
    
    ## Documentation clacular_MAE.
    #  @param self :
    #  @return true
    def calcular_MAE(self):
        Facade.calcular_MAE(self)
        return True
    
    ## Documentation clacular_MSE.
    #  @param self :
    #  @return true
    def calcular_MSE(self):
        Facade.calcular_MSE(self)
        return True