from .DaoDBMuestra import DaoDBMuestra
from ..modelo.Muestra import Muestra
# #@package Control
#
#


# # Documentation for a class.
#
#  Clase GestorMuestra.
class GestorMuestra:
    
    def __init__(self):
        # # The constructor.
        self.dao_db_muestra = DaoDBMuestra()
        self.muestra = Muestra()
        
    # # Documentation Cargar imagenes.
    #  @param self : 
    #  @param direccion : string
    #  @return true
    def cargar_imagenes(self, direccion):
        self.dao_db_muestra.cargar_imagenes(direccion)
        return True
    
    # # Documentation Cargar_cvs.
    #  @param self : 
    #  @param nombre : string 
    #  @return true
    def cargar_cvs(self, nombre):
        self.dao_db_muestra.cargar_cvs(nombre)
        return True
    
    # # Documentation Cargar_cvs.
    #  @param self : 
    #  @return true
    def calcular_MAE(self):
        self.muestra.calcular_MAE()
        return True
    
    def calcular_MSE(self):
        self.muestra.calcular_MSE()
        return True
