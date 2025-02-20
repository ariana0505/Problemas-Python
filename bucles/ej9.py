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