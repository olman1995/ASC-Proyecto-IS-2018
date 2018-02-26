from .Prueba import Prueba
from .MAE import MAE
from .MSE import MSE
from .RED import RED
class Muestra:
    
    def __init__(self):
        self.pruebas = []
        self.mae = MAE()
        self.mse = MSE()
        self.red = RED()