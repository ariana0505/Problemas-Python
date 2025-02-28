#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
perfil = {}
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
direccion = input("Ingrese su direccion: ")
telefono = int(input("Ingrese su numero de telefono: "))
perfil["nombre"] = nombre
perfil["edad"] = edad
perfil["direccion"]= direccion
perfil["telefono"]= telefono