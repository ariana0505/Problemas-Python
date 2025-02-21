#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
numGanador = input("iNGRESE LOS NUMEROS GANADORES: ")
orden = []
for i in numGanador:
    orden.append(int(i))
    
nueva_lista = sorted(numGanador, reverse=False) 
print(nueva_lista)