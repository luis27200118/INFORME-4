import numpy as np
import random
A=[]
def pedir_f():
    filas = int(input("Digame la cantidad de filas:"))
    return filas

def pedir_c():
    columnas = int(input("Digame la cantidad de columnas: "))
    return columnas

def llenar(matriz):
    filas = pedir_f()
    columnas = pedir_c()
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(random.randint(1, 10))
    print(matriz)

def transpuesta(A):
    matriz1 = np.array(A)
    matriz2 = np.transpose(matriz1)
    print(matriz2)

llenar(A)
transpuesta(A)