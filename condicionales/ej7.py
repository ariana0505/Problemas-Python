# INPUT:
# rentaAnual -> float

# OUTPUT:
# el tipo impositivo -> porcentaje

rentaAnual = float(input("Ingrese su renta anual: $"))

match rentaAnual:
    case _ if rentaAnual < 10000:
        print("tipo impositivo: 5%")
    case _ if rentaAnual < 2000:
        print("tipo impositivo: 15%")
    case _ if rentaAnual < 35000:
        print("tipo impositivo: 20%")
    case _ if rentaAnual < 60000:
        print("tipo impositivo: 30%")
    case _:
        print("tipo impositivo: 45%")
        
