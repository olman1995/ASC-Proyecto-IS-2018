from .BoneAge_XRay_CNN.output_predictions import Predict
'''
@package modelo
Documentation for a class.
Clase Estimador.
'''


class Estimador:
    def __init__(self):
        # The constructor
        self.predecir = None

    def estimar(self, sexo):
        self.predecir = Predict()
        self.predecir.star()
        resultado = self.predecir.predict(sexo)
        return resultado

    def estimar_muestra(self,sub_muestra,sexo):
        self.predecir = Predict()
        self.predecir.star()
        resultado = self.predecir.predict_1(sub_muestra,sexo)
        return resultado
        