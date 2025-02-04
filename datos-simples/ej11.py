cuenta_ahorro = float(input("Ingrese el monto de la cuenta: "))
interes = 0.04
balance1 = cuenta_ahorro * (1 + interes)
print(f"Balance tras el primer año: {round(balance1, 2)}")
balance2 = balance1 * (1 + interes)
print(f"Balance tras el segundo año: {round(balance2, 2)}")
balance3 = balance2 * (1 + interes)
print(f"Balance tras el tercer año: {round(balance3, 2)}")