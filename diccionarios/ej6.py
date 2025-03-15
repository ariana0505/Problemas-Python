#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
perfil = {}
continuar = True

while continuar:
    clave = input('¿Qué dato quieres introducir? ').strip()
    
    if not clave:
        print("La clave no puede estar vacía. Por favor, ingresa un dato válido.")
        continue
    
    valor = input(f'Introduce el valor para "{clave}": ').strip()
    
    if not valor:
        print(f"El valor para '{clave}' no puede estar vacio. Por favor, ingresa un valor valido.")
        continue
    
    perfil[clave] = valor
    print("\nPerfil actualizado:")
    print(perfil)
    
    while True:
        continuar_respuesta = input('¿Quieres añadir más información (Si/No)? ').strip().lower()
        if continuar_respuesta == "si":
            continuar = True
            break
        elif continuar_respuesta == "no":
            continuar = False
            print("\n¡Gracias por actualizar tu perfil!")
            break
        else:
            print("Por favor, responde con 'Si' o 'No'.")