from ...models import paciente
from ..modelo.Paciente import Paciente

##@package Control
#
#

## Documentation for a class.
#
#  Clase DaoBDPaciente.
class DaoBDPaciente:
    
    
    def __init__(self):
        ## The constructor.
        self.paciente= Paciente()
    
    ## Documentation guardar_informacion_paciente.
    #  @param self : 
    #  @param datos : DTOPaciente
    #  @return true
    def guardar_informacion_paciente(self,datos):
        return True
        
        