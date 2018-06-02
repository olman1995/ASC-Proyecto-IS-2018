from .Facade import Facade
'''
@package Control
Documentation for a class.
Clase FacadeAdministrador.
'''


class FacadeAdministrador(Facade):
    def __init__(self):
        # The constructor.
        Facade.__init__(self)
    '''
    Documentation Cargar imagenes.
    @param self :
    @param direccion : string
    @return true
    '''
    def cargar_muestra(self ,muestra,k,cant_img):
        resultado = Facade.cargar_muestra(self ,muestra, k, cant_img)
        return resultado 

