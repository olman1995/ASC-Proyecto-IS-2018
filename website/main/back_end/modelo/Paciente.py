from .Imagen import Imagen
from .RED import RED

class Paciente():
    
    def __init__(self):
        self.edad = None
        self.estimacion_edad = None
        self.url_imagen = None
        self.nombre = None
        self.apellido_1 = None
        self.apellido_2 = None
        self.cedula = None
        self.hospital = None
        self.img = Imagen()
        self.red = RED()

    def estimar_edad(self):
        return True