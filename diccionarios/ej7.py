#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

cesta_compras = {}

continuar = True

while continuar:
    clave = input('¿Que fruta quiere introducir? ').strip()
    
    if not clave:
        print("La clave no puede estar vacía. Por favor, ingresa un dato válido.")
        continue
    
    valor = int(input(f'Introduce el precio de "{clave}": '))
    
    if not valor:
        print(f"El precio de '{clave}' no puede estar vacio. Por favor, ingresa un valor valido.")
        continue
    
    cesta_compras[clave] = valor

    
    while True:
        continuar_respuesta = input('¿Quieres añadir mas articulos (Si/No)? ').strip().lower()
        if continuar_respuesta == "si":
            continuar = True
            break
        elif continuar_respuesta == "no":
            continuar = False
            print(f"La suma total es: {sum(cesta_compras.values())}")
        else:
            print("Por favor, responde con 'Si' o 'No'.")
            