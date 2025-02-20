#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

#Mi forma:

numero = int(input("Ingrese un número entero: "))
divisores = set()


for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.add(i)


if len(divisores) == 2:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
#su forma:

n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")