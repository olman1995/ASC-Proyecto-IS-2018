from .DaoDBMuestra import DaoDBMuestra
from ..modelo.Muestra import Muestra

class GestorMuestra:
    
    def __init__(self):
        self.DB=DaoDBMuestra()
        
    def cargar_imagenes(self):
        return True
    
    def cargar_cvs(self):
        return True
    