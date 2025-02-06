fecha = input("Porfavor ingrese su fecha de nacimiento con el formato dd/mm/aaaa: ")
dia = fecha[:fecha.find("/")]
mes = fecha[:-fecha.find("/")]
print(mes)