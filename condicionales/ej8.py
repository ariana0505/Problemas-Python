puntuacion = float(input("Ingrese su puntuacion: "))
nivelRendimiento = input("Ingrese su nivel de rendimiento(I/A/M): ").upper()
pago = 2400

match(puntuacion):
    case _ if puntuacion == 0.0 and nivelRendimiento == "I":
        print(f"su ingreso es: ${pago * 0.0}")
    case _ if puntuacion == 0.0 and nivelRendimiento == "A":
        print(f"su ingreso es: ${pago * 0.4}")
    case _ if puntuacion == 0.0 and nivelRendimiento == "M":
        print(f"su ingreso es: ${pago * 0.6}")
    case _ :
        print("Tu puntuacion no coincide con tu nivel de rendimiento ingrese el correcto")