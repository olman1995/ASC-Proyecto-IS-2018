# #@package Control
#
#


# # Documentation for a class.
#
#  Clase DTOPaciente.
class DTOPaciente:
    
    def __init__(self, edad, estimacion_edad, url_imagen, nombre, apellido_1, apellido_2, cedula, hospital):
        # # The constructor.
        self.edad = edad
        self.estimacion_edad = estimacion_edad
        self.url_imagen = url_imagen
        self.nombre = nombre
        self.apellido_1 = apellido_1
        self.apellido_2 = apellido_2
        self.cedula = cedula
        self.hospital = hospital
        
        
