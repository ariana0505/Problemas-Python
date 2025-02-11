invertir = float(input("Ingrese la cantidad a invertir: "))
interesAnual = float(input("Ingrese el interes anual: %"))
años = int(input("ingrese el numero de años: "))
for i in range(años):
    invertir *= 1 + interesAnual / 100
    print(f"La capital en {1 + i} años {round(invertir,2)}")