from .Facade import Facade
from .FacadeAdministrador import FacadeAdministrador
from .FacedeMedico import FacadeMedico
from .DaoBDUsuario import DaoBDUsuario
'''
@package Control
@version: 0.1.20
@author: Olman Castilla, Fernanda Alvarado y Yonnattan Serrano
Documentation for a class.
Clase UIUsuario.
'''


class UIUsuario:
    def __init__(self):
        # The constructor.
        self.nombre = None
        self.contrasena = None
        self.tipo = None
        self.dao_bd_usuario = DaoBDUsuario()
        self.facade = None
    '''
    Documentation Cargar imagen.
    @param self :
    @param nombre :  string
    @param contrasena :  string
    @return true
    '''
    def ingresar(self, nombre, contrasena):
        
        self.nombre, self.contrasena, self.tipo = self.dao_bd_usuario.ingresar(nombre, contrasena)
        if self.tipo == 0:
            self.facade = FacadeAdministrador()
        elif self.tipo == 1:
            self.facade = FacadeMedico()
        else:
            self.facade = FacadeMedico()
            
        return self.tipo
