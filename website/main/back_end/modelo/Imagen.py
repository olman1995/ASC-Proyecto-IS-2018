import numpy as np
import cv2


class Imagen:
    
    def __init__(self,img=None):
        self.img = img
        self.vector = []


    def vectorizar(self):
        self.vector = self.img.T.flatten().T
        return None

    def leer_imagen(self,directorio):
        self.img = cv2.imread(directorio)
        #self.cambiar_dimenciones_imagen(Configuracion.IMG_X, Configuracion.IMG_Y)
        self.vectorizar()
        return True 

    def cambiar_tamano_porcentual_imagen(self,porcentaje_x,porcentaje_y):
        self.img = cv2.resize(self.img, (0,0), fx = porcentaje_x, fy = porcentaje_y)
        return None

    def cambiar_dimenciones_imagen(self,tamano_x, tamano_y):
        self.img = cv2.resize(self.img, (tamano_x, tamano_y))
        return None