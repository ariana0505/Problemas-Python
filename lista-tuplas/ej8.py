#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra = input("Ingrese una palabra: ").lower
confirmar = palabra[::-1]
print(confirmar)

if palabra == confirmar:
    print("Es un polindromo")
else:
    print("No es un polidromo")