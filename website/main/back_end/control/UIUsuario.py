from .Facade import Facade
from .FacadeAdministrador import FacadeAdministrador
from .FacedeMedico import FacadeMedico
from ...models import usuario
class UIUsuario:
    
    def __init__(self):
        self.facade = None
        
    def ingresar(self,nombre,contrasena):
        
        for i in usuario.objects.all():
            if i.nombre==nombre and i.contrasena == contrasena:
                
                if i.tipo==0:
                    self.facade=FacadeAdministrador()
                elif i.tipo==1:
                    self.facade=FacadeMedico()
                return i.tipo
            
        return -1