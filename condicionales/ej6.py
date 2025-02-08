nombre = input("Ingrese su nombre: ").lower().strip()
sexo = input("Ingrese su sexo(F/M): ").lower().strip()
if (nombre[0] < "m" and sexo == "f") or (nombre[0] > "n" and sexo == "m") :
    print("Eres del Grupo A")
else:
    print("Eres del Grupo B")
    
#INPUT: 
#nombre -> cadena
#sexo -> cadena
    
#OUTPUT:
#"Eres del Grupo B" OR "Eres del Grupo A"

#Grupo A
#mujeres: nombre anterior a la M
#Hombre: nombre posterior a la N

#Grupo B
# RESTO

