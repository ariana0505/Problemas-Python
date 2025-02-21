#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"] 
notas = {}
cursosJalados = []
for asignatura in asignaturas:
    nota = float(input(f"ingrese su nota de {asignatura}: "))
    notas[asignatura] = nota


for curso, nota in notas.items():
    if (nota <= 10):
        cursosJalados.append(curso)
        
print("Los cursos que tienes que repetir son: ")
print(*cursosJalados, sep=", " )