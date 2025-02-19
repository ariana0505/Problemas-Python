#range(inicio, fin, paso)
#inicio (opcional): El número con el que empieza la secuencia. Por defecto es 0.
#fin: El número con el que termina la secuencia (sin incluirlo).
#paso (opcional): La diferencia entre cada número en la secuencia. Por defecto es 1.
print("--> RANGE")

print("for range numero fin")
for i in range(5):  # equivale a range(0, 5)
    print(i)

print("for range numero inicial y final")
for i in range(2, 8):  # Empieza en 2, termina antes de 8
    print(i)

print("for range numero inicial, final y paso")
for i in range(0, 10, 2):  # Paso de 2
    print(i)

