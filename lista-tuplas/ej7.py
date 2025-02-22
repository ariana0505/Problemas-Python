#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
import string

abecedario = list(string.ascii_lowercase)

for i in range(len(abecedario), 1, -1):
    if i % 3 == 0:
        abecedario.pop(i-1)
print(abecedario)
#Se usa i-1 porque los índices en listas empiezan en 0, pero range() genera números comenzando desde 1 hasta 26.