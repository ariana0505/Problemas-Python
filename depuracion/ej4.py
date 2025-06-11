# listin = {'Juan':123456789, 'Pedro':987654321}

# def elimina(listin, usuario):
#     del listin[usuario]
#     return listin[usuario]

# print(elimina(listin, 'Pablo'))
listin = {'Juan':123456789, 'Pedro':987654321}

def elimina(listin, usuario):
    if usuario in listin:
        del listin[usuario]
        return listin
    else:
        return f"Usuario {usuario} no encontrado en la lista."

print(elimina(listin, 'Pablo'))