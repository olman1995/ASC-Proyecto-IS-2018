from .BoneAge_XRay_CNN.output_predictions import Predict
'''
@package modelo
@version: 0.1.20
@author: Olman Castilla, Fernanda Alvarado y Yonnattan Serrano
Documentation for a class.
Clase Estimador.
'''
from sqlalchemy.sql.expression import except_


class Estimador:
    def __init__(self):
        # The constructor
        self.predecir = None
    '''
    Documentation estimar.
    @param self
    @param sexo= F,M solo acepta los valores de F y M
    @return float positvo , -1 si es error
    '''
    def estimar(self, sexo):
        try:
            self.predecir = Predict()
            self.predecir.star()
            resultado = self.predecir.predict(sexo)
        except:
            return -1
        
        return resultado
    
    '''
    Documentation estimar_muestra.
    @param self
    @param muestra= [id_image] clase erronea cualquier otro valor que no sea una lista con el numero de id de la imagen
    @param sexo= [(F,M)]  solo acepta los valores de F y M
    @return resultado=[res], -1 si es error
    '''
    def estimar_muestra(self,sub_muestra,sexo):
        try:
            self.predecir = Predict()
            self.predecir.star()
            resultado = self.predecir.predict_1(sub_muestra,sexo)
        except:
            return -1
        
        return resultado
        