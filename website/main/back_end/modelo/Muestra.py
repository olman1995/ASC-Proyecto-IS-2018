from .Prueba import Prueba
from .MAE import MAE
from .MSE import MSE
from .Estimador import Estimador

# #@package modelo
#
#


# # Documentation for a class.
#
#  Clase Muestra.
class Muestra:
    
    def __init__(self):
        # # The constructor.
        self.pruebas = []
        self.mae = MAE()
        self.mse = MSE()
<<<<<<< HEAD
        # self.estimador = Estimador()
=======
        self.estimador = Estimador()
>>>>>>> parent of a752c27... website 0.1.11
        
    # # Documentation clacular_MAE.
    #  @param self :
    #  @return true
    def calcular_MAE(self):
        return True
    
    # # Documentation Calcuar_MSE .
    #  @param self : 
    #  @return true
    def calcular_MSE(self):
        return True
