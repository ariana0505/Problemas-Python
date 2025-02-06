nombre = input("Ingrese su nombre completo: ").strip()
#cambios
nombreMinuscula = nombre.lower()
nombreMayucula = nombre.upper()
nombreCapitalizado = nombre.capitalize()
#alt + 92 -> \
print(f"{nombreMinuscula} \n{nombreMayucula} \n{nombreCapitalizado}")