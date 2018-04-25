from .Facade import Facade

# #@package Control
#
#


# # Documentation for a class.
#
#  Clase FacadeMedico.
class FacadeMedico(Facade):
    
    def __init__(self):
        # # The constructor.
        Facade.__init__(self)

    # # Documentation Cargar imagen.
    #  @param self : 
    #  @param nombre : string
    #  @return true
    def cargar_imagen(self, nombre):
        Facade.cargar_imagen(self, nombre)
        return True

    # # Documentation estimar_edad.
    #  @param self : 
    #  @return true
    def estimar_edad(self, sexo, url_imagen):
        resultado = Facade.estimar_edad(self, sexo, url_imagen)
        return resultado

    # # Documentation desplegar_edad.
    #  @param self : 
    #  @return true
    def desplegar_edad(self):
        return Facade.desplegar_edad(self)
    
    # # Documentation guardar_informacion_paciente.
    #  @param self : 
    #  @param datos : DTOPaciente
    #  @return true
    def guardar_informacion_paciente(self, datos):
        Facade.guardar_informacion_paciente(datos)
        return True
