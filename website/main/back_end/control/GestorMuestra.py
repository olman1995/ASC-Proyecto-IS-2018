from .DaoDBMuestra import DaoDBMuestra
from ..modelo.Muestra import Muestra

##@package Control
#
#

## Documentation for a class.
#
#  Clase GestorMuestra.
class GestorMuestra:
    
    def __init__(self):
        ## The constructor.
        self.DB=DaoDBMuestra()
        
    ## Documentation Cargar imagenes.
    #  @param self : 
    #  @return true
    def cargar_imagenes(self):
        return True
    
    ## Documentation Cargar_cvs.
    #  @param self : 
    #  @return true
    def cargar_cvs(self):
        return True
    