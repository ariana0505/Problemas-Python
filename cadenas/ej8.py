dolares = input("Ingrese un monto de un producto en euros con 2 decimales: ").strip()

entero = dolares[:dolares.find(".")]
centimos = dolares[1 + dolares.find("."):]

print(f"numero de euros: {entero} y numero de centimos: {centimos}")