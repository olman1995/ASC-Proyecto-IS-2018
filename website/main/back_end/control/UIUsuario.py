from .Facade import Facade
from .FacadeAdministrador import FacadeAdministrador
from .FacedeMedico import FacadeMedico
from .DaoBDUsuario import DaoBDUsuario

class UIUsuario:
    
    def __init__(self):
        self.nombre = None
        self.contrasena = None
        self.tipo= None
        self.dao_bd_usuario= DaoBDUsuario()
        self.facade = None
        
    def ingresar(self,nombre,contrasena):
        self.nombre,self.contrasena,self.tipo=self.dao_bd_usuario.ingresar(nombre,contrasena)
        if self.tipo==0:
            self.facade=FacadeAdministrador()
        elif self.tipo==1:
            self.facade=FacadeMedico()
        
       