pan = 3.49
pan_dia = pan * 0.6

npan= int(input("Ingrese el numero de panes frescos: "))
npan_dia = int(input("ingrese la cantidad de panes no frescos: "))
print(f"El precio habitual por ser fesco es : ${pan} pero por no ser fresco tiene un descuento del 60% ")
print(f"El precio total es: ${round((pan * npan + pan_dia*npan_dia),2)}")