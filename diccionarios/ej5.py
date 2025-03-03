#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.


asignatura = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

for key,valuer in asignatura.items():
    print(f"{key} tiene credito: {valuer}")

print(f"El valor del curso es: {sum(asignatura.values())}")