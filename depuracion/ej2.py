# base = input('Introduce la base imponible de la factura: ')
# print(aplica_iva(base, iva))

# def aplica_iva(base, iva = 21):
#     base = base * iva   
#     return base 
def aplica_iva(base, iva = 21):
    base += base * iva / 100   
    return base 

base = input('Introduce la base imponible de la factura: ').strip()
print(aplica_iva(base))



