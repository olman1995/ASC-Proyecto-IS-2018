from ...models import usuario
'''
@package Control
@version: 0.1.20
@author: Olman Castilla, Fernanda Alvarado y Yonnattan Serrano
Documentation for a class.
Clase DaoBDUsuario.
'''


class DaoBDUsuario:
    def __init__(self):
        # The constructor.
        self.x = 0
    '''
    Documentation Cargar imagen.
    @param self :
    @param nombre :  string
    @param contrasena :  string
    @return nombre : string,contrasena : string,tipo : int
    '''
    def ingresar(self, nombre, contrasena):
        try:
            for i in usuario.objects.all():
                if i.nombre == nombre and i.contrasena == contrasena:
                    return i.nombre, i.contrasena, i.tipo
        except:
            return "", "", -1
        return "", "", -1
