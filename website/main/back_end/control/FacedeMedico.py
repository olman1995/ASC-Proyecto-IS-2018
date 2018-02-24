from .Facade import Facade

class FacadeMedico(Facade):
    
    def __init__(self):
        Facade.__init__()
    
    def cargar_imagen(self):
        Facade.cargar_imagen(self)
        return True
    
    def estimar_edad(self):
        Facade.estimar_edad(self)
        return True
    
    def desplegar_edad(self):
        Facade.estimar_edad(self)
        return 0
    
    def guardar_informacion_paciente(self):
        Facade.guardar_informacion_paciente(self)
        return True
