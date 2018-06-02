from .DaoDBMuestra import DaoDBMuestra
from ..modelo.Muestra import Muestra
'''
@package Control
Documentation for a class.
Clase GestorMuestra.
'''


class GestorMuestra:
    def __init__(self):
        # The constructor.
        #self.dao_db_muestra = DaoDBMuestra()
        self.muestra = Muestra()
    '''
    Documentation Cargar imagenes.
    @param self :
    @param direccion : string
    @return true
    '''
    def cargar_muestra(self ,muestra,k,cant_img):
        resultado = self.muestra.cargar_muestra(muestra, k, cant_img)
        return resultado 
    