#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Ingrese una palabra: ").lower()

a = palabra.count("a")
e = palabra.count("e")
i = palabra.count("i")
o = palabra.count("o")
u = palabra.count("u")

print(f"tu palabra tiene a:{a}, e:{e}, i:{i}, o:{o}, u:{u}")