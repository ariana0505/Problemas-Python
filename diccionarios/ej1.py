#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
divisas = {
  'euro':'€',
  'dollar':'$',
  'yen':'¥'
  }

divisa = input("Ingrese el nombre de la divisa: ").lower()
#get(lo que queremos obtener, mensaje si no se encuentra)
print(divisas.get(divisa, "Divisa no encontrada"))
