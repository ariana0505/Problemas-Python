#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
import numpy as np

A = np.array([1, 2, 3])
B = np.array([-1, 0, 2])

producto_escalar = np.dot(A, B)

print(producto_escalar)  