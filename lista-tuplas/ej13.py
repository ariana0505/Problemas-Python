#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
import math

muestra_num = input("Ingrese una muestra de números, separados por comas: ")
lista = list(map(lambda i: int(i),muestra_num.split(",")))
media = sum(lista)/len(lista)
print(f"Tu media es: {media} :D")
sumatoria = sum((x - media) ** 2 for x in lista)
desviacion = math.sqrt(sumatoria / (len(lista) - 1))
print(desviacion)