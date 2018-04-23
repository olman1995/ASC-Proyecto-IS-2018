from .Imagen import Imagen
from .Estimador import Estimador

##@package modelo
#
#

## Documentation for a class.
#
#  Clase Paciente.
class Paciente:
    
    def __init__(self):
        ## The constructor.
        self.edad = None
        self.estimacion_edad = None
        self.url_imagen = None
        self.nombre = None
        self.apellido_1 = None
        self.apellido_2 = None
        self.cedula = None
        self.hospital = None
        self.img = Imagen()
        self.estimador = Estimador()

    ## Documentation estimar_edad.
    #  @param self : 
    #  @return true
    def estimar_edad(self,sexo):
        resultado=self.estimador.estimar(sexo)
        return resultado