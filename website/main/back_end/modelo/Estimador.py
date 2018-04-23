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
        self.predecir = Predict()

    def estimar(self,sexo="F"):
        #self.predecir=None
        
        
        resultado = self.predecir.predict(sexo)
        
        return resultado