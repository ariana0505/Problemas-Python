correo = input("Ingrse su correo electronico: ").strip()
#nombre = correo.replace('@gmail.com', '@ceu.es')
nombre = correo[:correo.find("@")]

nom_directorio = nombre + "@ceu.es"
print(nom_directorio)

#input
#aalvarop@gmail.com

#ouput
#aalvaropc@ceu.es