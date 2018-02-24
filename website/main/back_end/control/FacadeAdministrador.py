from .Facade import Facade

class FacadeAdministrador(Facade):
    
    def __init__(self):
        Facade.__init__()
    
    def cargar_imagenes(self):
        Facade.cargar_imagenes(self)
        return True
    
    def cargar_cvs(self):
        Facade.cargar_cvs(self)
        return True
    
    def calcular_MAE(self):
        Facade.calcular_MAE(self)
        return True
    
    def calcular_MSE(self):
        Facade.calcular_MSE(self)
        return True