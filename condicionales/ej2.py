codigo = "contraseña"

intento = input("Ingrese la contraseña: ")
if codigo == intento.lower() or intento.upper():
    print("entro")
else:
    print("ingrse la contraseña correcta: ")  