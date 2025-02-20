frase = input('Ingrese una frase: ')

#Vereficar si la letra ingresada es una vocal

while True:
    vocal = input('Ingrese una vocal: ')
    if vocal == ("a" or "e" or "i" or "o" or "u"):
        break
    else:
        print("Ingrese una vocal porfavor")

#contar cuantas veces aparece la vocal

cantidadvocal = frase.count(vocal)
print(f"La veces repetidas son :{cantidadvocal}")