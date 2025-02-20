#mi forma

verificacion = False
contraseña = "Hola123.321"
while verificacion == False:
    intentoIngreso = input("Ingrese su contraseña: ")
    if(intentoIngreso  == contraseña):
        print("¡Bienvenido!")
        verificacion = True

    else:
        print("error en la contraseña, intente denuevo")

#Su forma:

key = "contraseña"
password =""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")