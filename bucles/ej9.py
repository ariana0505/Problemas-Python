#mi forma


# contraseña = "Hola123.321"
# while True:
#     intentoIngreso = input("Ingrese su contraseña: ")
#     if(intentoIngreso  == contraseña):
#         print("¡Bienvenido!")
#         break
#     else:
#         print("error en la contraseña, intente denuevo")

#Su forma:

key = "contraseña"
password =""
i = 0
while password != key:
    if i != 0:
        print("ERROR")
    password = input("Introduce la contraseña: ")
    i = 1
print("Contraseña correcta")


#La mejor forma:

# Contraseña predefinida
contraseña = "Hola123.321"
max_intentos = 3  # Limitar el número de intentos

# Ciclo para permitir intentos de ingreso de contraseña
intentos = 0
while intentos < max_intentos:
    intentoIngreso = input("Ingrese su contraseña: ")
    
    if intentoIngreso == contraseña:
        print("¡Bienvenido!")
        break
    else:
        intentos += 1
        intentos_restantes = max_intentos - intentos
        if intentos_restantes > 0:
            print(f"Error en la contraseña. Te quedan {intentos_restantes} intentos.")
        else:
            print("Has superado el número máximo de intentos. Acceso bloqueado.")
            break