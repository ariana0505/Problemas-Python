puntuacion = float(input("Ingrese su puntuacion: "))
nivelRendimiento = input("Ingrese su nivel de rendimiento(I/A/M): ").upper()
pago = 2400

match(puntuacion):
    case _ if puntuacion == 0.0 and nivelRendimiento == "I":
        print(f"su ingreso es: ${pago + puntuacion}")
    case _ if puntuacion == 0.4 and nivelRendimiento == "A":
        print(f"su ingreso es: ${pago * puntuacion}")
    case _ if puntuacion >= 0.6 and nivelRendimiento == "M":
        print(f"su ingreso es: ${pago * puntuacion}")
    case _ :
        print("Ingrese los valore correspondientes")