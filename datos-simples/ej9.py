monto = float(input("ingrese la cantidad a invertir: "))
Taza_interes = float(input("ingrese taza de interes anual: "))
tiempo = int(input("Ingrese el numero de años: "))
#round((),2)-> numero maximo de decimales
print(f"El capital obtenido redondeado{round(((monto - (Taza_interes/100)*monto*tiempo)),2)}")