def factorial(n):
    num = 1
    resultado  = 0
    for i in range(1,(n+1)):
        resultado = num * i
        num = resultado
    return resultado    

respuesta = factorial(4)
print(respuesta)