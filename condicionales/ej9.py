edad = int(input("Ingrese su edad: "))

if (edad<4):
    precio = 0
elif (4<=edad<=18):
    precio = 5
else:
    precio = 18

print(f"El costo de entrada es: ${precio}")