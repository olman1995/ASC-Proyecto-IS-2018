import numpy as np
import cv2
'''
@package modelo
Documentation for a class.
Clase GestorPaciente.
'''


class Imagen:
    def __init__(self, img=None):
        # The constructor.
        self.img = img
        self.vector = []
    '''
    Documentation vectorizar.
    @param self :
    @return true
    '''
    def vectorizar(self):
        self.vector = self.img.T.flatten().T
        return None
    '''
    Documentation leer_imagen.
    @param self :
    @param self : directorio
    @return true
    '''
    def leer_imagen(self, directorio):
        self.img = cv2.imread(directorio)
        return True
