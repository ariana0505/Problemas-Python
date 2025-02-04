peso = float(input("Porfavor ingrese su peso en kg: "))
altura = float(input("Porfavor indrese su altura en metros: "))
imc = round(peso/altura**2)
print(f"Tu indice de masa corporal es: {str(imc)}")