#diccionario clave numero fatura : valor costes de factura 
facturas = {}
pendiente = 0
cobrado = 0
continuar = "c"
while continuar: 
    while True:
        opcion = input("Desea añadir, eliminar o pagar alguna factura? (a/p): ").strip().lower()
        if opcion in ("a", "p"):
            print("Okey! Prosigamos...")
            break
        else:
            print("Porfavor ingrese alguna de las opciones: ")

    if opcion == "a":
        numFactura = int(input("Ingrese un numero de factura: "))
        coste = float(input("Ingrese el costo de la factura: "))
        facturas[numFactura] = coste
        pendiente += coste

    if opcion == "p":
        numFactura = int(input("Ingrese el numero de factura que desea pagar: "))
        print("Comenzando tramite...")
        try:
            del(facturas[numFactura])
        except:
            print("El numero de Factura que a ingresado no existe")
        print("¡Termino!")
    
    continuar = input("Desea terminar o continuar? (T/C): ").strip().lower()