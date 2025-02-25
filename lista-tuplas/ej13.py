#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
muestra_num = input("Ingrese una muestra de números, separados por comas: ")
lista = list(map(lambda i: int(i),muestra_num.split(",")))
resultado = sum(lista)/len(lista)
print(f"Tu media es: {resultado} :D")