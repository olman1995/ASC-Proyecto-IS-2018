from ...models import paciente
from ..modelo.Paciente import Paciente

# #@package Control
#
#


# # Documentation for a class.
#
#  Clase DaoBDPaciente.
class DaoBDPaciente:
    
    def __init__(self):
        # # The constructor.
        self.dato = None
    
    # # Documentation guardar_informacion_paciente.
    #  @param self : 
    #  @param datos : DTOPaciente
    #  @return true
    def guardar_informacion_paciente(self, datos):
        self.dato = paciente(edad=datos.edad,
        estimacion_edad=datos.estimacion_edad,
        url_imagen=datos.url_imagen,
        nombre=datos.nombre,
        apellido_1=datos.apellido_1,
        apellido_2=datos.apellido_2,
        cedula=datos.cedula,
        hospital=datos.hospital)
        self.dato.save()
        return True
        
        
