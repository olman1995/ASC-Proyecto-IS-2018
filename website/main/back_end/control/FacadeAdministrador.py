from .Facade import Facade
'''
@package Control
@version: 0.1.20
@author: Olman Castilla, Fernanda Alvarado y Yonnattan Serrano
Documentation for a class.
Clase FacadeAdministrador.
'''


class FacadeAdministrador(Facade):
    def __init__(self):
        # The constructor.
        Facade.__init__(self)
    '''
    Documentation Cargar_Muestra.
    @param self
    @param muestra= dicionario de estructura {"id":[id_image],"edad":[edad],"sexo":[("f","M")]} ,cualquier otro valor
    @param k= entero positivo, cualquier otro valor
    @param cant_img= entero positivo, cualquier otro valor  
    @return resultado={"sub":self.sub_muestra,"mae":[],"mse":[],"res":[],"mean":[],"std":[],"var":[]}
    '''
    def cargar_muestra(self ,muestra,k,cant_img):
        resultado = Facade.cargar_muestra(self ,muestra, k, cant_img)
        return resultado 

