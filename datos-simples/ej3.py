# la coma da un espacio por defecto
# el más no da un espacio por defecto 
nombre = input("¿Cuál es su nombre?: ")

# Verificamos si el nombre contiene solo números
if nombre.isdigit():
    print("Ingrese un nombre válido, no puede ser un número.")
else:
    print(f"¡Hola {nombre}!")

