#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
perfil = {
    "nombre": input("Ingrese su nombre: "),
    "edad": int(input("Ingrese su edad: ")),
    "direccion": input("Ingrese su dirección: "),
    "telefono": input("Ingrese su número de teléfono: ")
}

print(f'{perfil["nombre"]} tiene {perfil["edad"]} años, vive en {perfil["direccion"]} y su número de teléfono es {perfil["telefono"]}.')