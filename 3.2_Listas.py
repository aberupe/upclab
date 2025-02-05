# Lista de asignaturas
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

# Lista para almacenar las notas
notas = []

# Preguntar la nota de cada asignatura al usuario y almacenarlas en la lista
for asignatura in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "? "))
    notas.append(nota)

# Mostrar las notas por pantalla
for i in range(len(asignaturas)):
    print("En", asignaturas[i], "has sacado", notas[i])