#!/usr/bin/python
# -*- coding: latin-1 -*-

import numpy as np

"""
Programa con todos los metodos y funciones para el procesamiento de los datos del Encefalograma.
Autores: Oscar Fernando Garzon-Alejandro Espinosa
Fecha: JUeves 9 de Octubre de 2013.
"""

def main():
pass
    """
    Lee los datos de los encefalograma para hacer un espectro de potencias.
    """
def Load_Data(file):
    """
    Carga los datos desde un archivo "file"y los organiza en una matriz.
    Input: filename.
    Output: numpy array (MATRIZ) con todos los datos del encefalograma debidamente organizados.
    """
    return Matriz
def Aplicar_FFT(Columna):
        
    """
    Aplica Fourier a una distribucion de puntos equidistantes que se encuentran organizados en un vector.
    Input: Columna. Vector de datos de una columna de la matriz que creamos en el metodo anterior.
    Output: numpy array con el espectro de potencias de una se�al.
    """
    return Potencias
def PLOT(Espectro):
          
    """
    Da una grafica del espectro de potencias con respecto a las frecuencias K
    Input: Espectro. Vector que contiene el espectro de potencia de una se�al.
    """
    
def Organizar(Espectro):
        
    """
    Organiza de mayor a menor los elementos del vector Espectro con sus respectivas frecuencias.
    Input: Espectro. Vector que contiene el espectro de potencia de una se�al.
    Output: vector que contiene los 10 valores mas grandes del espectro de potencias.
    """
    return Espectro_Limpio
        
def Aplicar_InvFFT(Espectro_Limpio):
    PLOT(Espectro)
          

        """
        Aplica la transformada invrsa de FOurier a un vector de puntos y grafica la se�al filtrada.
        Input: Espectro_Limpio.Vector que contiene los 10 valores mas grandes del espectro de potencias de cada se�al.
        Output: Se�al filtrada. Vector que contiene los datos de una se�al mas limpia.Grafica de dicha se�al.
        """
      
