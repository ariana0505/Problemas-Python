#Escribir un programa que almacene las matrices a y b en una lista y muestre por pantalla su producto.Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

C = np.dot(A, B)

print(C)