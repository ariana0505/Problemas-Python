#Mi forma:
numero = int(input("Ingrese un numero entero por favor: "))
lista =[]
for i in range(1,numero,2):
   lista.append(i)
   print(*lista[::-1])# El '*' descompone la lista en sus elementos individuales

#su forma:
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")