from .Control import Control

class Facade:
    
    def __init__(self):
        self.control=Control()
    
    def cargar_imagen(self):
        self.control.cargar_imagen()
        return True
    def estimar_edad(self):
        self.control.estimar_edad()
        return True
    def desplegar_edad(self):
        self.control.desplegar_edad()
        return 0
    def guardar_informacion_paciente(self):
        self.control.guardar_informacion_paciente()
        return True
    def cargar_imagenes(self):
        self.control.cargar_imagenes()
        return True
    def cargar_cvs(self):
        self.control.cargar_cvs()
        return True
    def calcular_MAE(self):
        self.control.calcular_MAE()
        return True
    def calcular_MSE(self):
        self.control.calcular_MSE()
        return True