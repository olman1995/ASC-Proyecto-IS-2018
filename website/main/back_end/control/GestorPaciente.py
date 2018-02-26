from ..modelo.Paciente import Paciente
from .DaoBDPaciente import DaoBDPaciente
class GestorPaciente:
    
    def __init__(self):
        self.paciente = Paciente()
        self.dao_db_pacinete = DaoBDPaciente()
    
    def guardar_informacion_paciente(self,datos):
        return True
        