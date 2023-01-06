#Ejercicio 6
import random
import numpy as np
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
def determinante_matriz(A):
    #matriz
    print("Matriz A con numpy")
    matriz_array = np.array(A)
    print(matriz_array)
    #calcular la determinante
    determinante = np.linalg.det(matriz_array)
    print(round(determinante,0))
llenar(A)
determinante_matriz(A)