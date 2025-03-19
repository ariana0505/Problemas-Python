
diccionario = {}

#pedir palabras atraves de un while ambos 
while True:
    palabra_ES = input("Ingresa una palabra en español: ").strip().lower()
    palabra_ING = input("Ingrese su traduccion en ingles (solo una palabra): ").strip().lower()
    
    if palabra_ES and palabra_ING :
        diccionario[palabra_ES] = palabra_ING
    else:
        print("Por favor ingrese todos los valores pedidos")
        continue

    ampliar = input("Desea seguir ampliando el diccionario?(S/N): ").strip().lower()
    if ampliar == "s":
        print("Ampliemos más el diccionario !")
    elif ampliar == "n":
        print(f"Tu diccionario es: {diccionario}")
        break
    else:
        print("Porfavor ingrese un valor valido")

frase = input("Ingrese una frase en español").lower().strip()
palabras = frase.split(" ")

for i in range(len(palabras)):
    if palabras[i] in diccionario:
        palabras[i] = diccionario[palabras[i]]
    else:
        palabras[i] = "Undefined"
print(" ".join(palabras))