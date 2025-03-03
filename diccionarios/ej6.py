#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
perfil = {}
for i in range(4):
    match i:
        case 1:
            perfil["nombre"] = input("Ingrese su nombre: ")
        case 2:
            perfil["edad"] = int(input("Ingrese su edad: "))    
        case 1:
            perfil["nombre"] = input("Ingrese su nombre")
    print(perfil)