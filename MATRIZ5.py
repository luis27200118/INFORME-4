#Ejercicio5
import numpy as np
import random
"""
Ejemplo de matrices simetricas llenar
[1,0],[0,1]
Ejemplo matriz no simetricas llenar
"""
A=[[1,0],[0,1]]

def transpuesta(A):
    m = np.array(A)
    B = np.transpose(m)
    print(m)
    print(B)
    if np.array_equal(m,B) == True:
        print("Son transpuestas ¡¡¡")
    else:
        print("No son transpuestas :( ")
        
transpuesta(A)