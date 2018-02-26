from ..modelo.Paciente import Paciente
from .DaoBDPaciente import DaoBDPaciente

##@package Control
#
#

## Documentation for a class.
#
#  Clase GestorPaciente.
class GestorPaciente:
    
    def __init__(self):
        ## The constructor.
        self.paciente = Paciente()
        self.dao_db_pacinete = DaoBDPaciente()

    ## Documentation guardar_informacion_paciente.
    #  @param self : 
    #  @return true
    def guardar_informacion_paciente(self,datos):
        return True
        