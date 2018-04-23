##@package modelo
#
#

## Documentation for a class.
#
#  Clase Estimador.
from .BoneAge_XRay_CNN.output_predictions import Predict

class Estimador:
    def __init__(self):        
        ## The constructor
        predecir=None

    def estimar(self,sexo="F"):
        
        predecir = Predict();
        resultado = predecir.predict(sexo)
        return resultado