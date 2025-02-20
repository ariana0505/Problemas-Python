#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    palabra = input(" ")
    if palabra == "salir":
        break
    else:
        continue