#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

frutas = {
    "plátano": 1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}


fruta = input("Ingrese una fruta: ").strip().lower()
kilos = input("Ingrese el número de kilos: ")

if fruta in frutas:
    if kilos.replace(".", "", 1).isdigit():
        precio_total = round(frutas[fruta] * float(kilos), 2)
        print(f"El precio de {kilos} kilos de {fruta} es: ${precio_total}")
    else:
        print("Debe ingresar un número válido de kilos.")
else:
    print("La fruta ingresada no está en la lista.")