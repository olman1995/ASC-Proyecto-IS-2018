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
        self.cont=0
        self.predecir = Predict()

    def estimar(self,sexo="F"):
        #self.predecir=None
        if(self.cont==0):
            self.predecir.star()
            print("h1")
            self.cont=1
        
        resultado = self.predecir.predict(sexo)
        
        return resultado