from .Estimador import Estimador
import random
import numpy as np
'''
@package modelo
Documentation for a class.
Clase Muestra.
'''


class Muestra:
    def __init__(self):
        # The constructor.
        self.muestra = []
        self.estimador = Estimador()
        self.sub_muestra =[]
        
        # self.estimador = Estimador()
    '''
    Documentation clacular_MAE.
    @param self :
    @return true
    '''
    def calcular_MAE(self,y1,y2):
        y_1=np.array(y1)
        y_2=np.array(y2)
        mae = (1/len(y1))*sum(np.abs(y_1-y_2))
        return mae
    '''
    Documentation Calcuar_MSE .
    @param self :
    @return true
    '''
    def calcular_MSE(self,y1,y2):
        y_1=np.array(y1)
        y_2=np.array(y2)
        mae = (1/len(y1))*sum((y_1-y_2)**2)
        return mae
        return True
    '''
    Documentation Calcuar_MSE .
    @param self :
    @return true
    '''
    def cargar_muestra(self,muestra,k,cant_img):
        self.sub_muestra=[]
        for i in range(k):
            self.sub_muestra.append([])
            for j in range(cant_img):
                self.sub_muestra[i].append([])
                self.sub_muestra[i].append([])
                self.sub_muestra[i].append([])
                cambio=True
                while(cambio):
                    valor=random.choice(muestra.get("id"))
                    if valor in self.sub_muestra[i][0]:
                        cambio=True
                    else:
                        index=muestra.get("id").index(valor)
                        self.sub_muestra[i][0].append(valor)
                        self.sub_muestra[i][1].append(muestra.get("age")[index])
                        self.sub_muestra[i][2].append(muestra.get("sex")[index])
                        cambio=False
        
        self.muestra=muestra
        resultado={"sub":self.sub_muestra,"mae":[],"mse":[],"res":[],"mean":[],"std":[],"var":[]}
        
        
        for i in self.sub_muestra:
            estimacion=self.estimador.estimar_muestra(i[0],i[2])
            resultado.get("res").append(estimacion)
            resultado.get("mae").append(self.calcular_MAE(estimacion,i[1]))
            resultado.get("mse").append(self.calcular_MSE(estimacion,i[1]))
            resultado.get("mean").append(np.mean(estimacion))
            resultado.get("std").append(np.std(estimacion))
            resultado.get("var").append(np.var(estimacion))
        
        return resultado
