# //Sentencias de Selección - Ejercicio 6
# Programa que muestra la nota final de un alumno
# a partir de su calificación numérica
# Autor: Antonio Benítez Rodríguez
# Fecha: 16/09/2025
print("Introduzca la calificación del alumno")
nota = int(input("Calificación: "))
match nota:
    case n if n < 5:
        resultado = "Suspenso"
    case n if n >= 5 and n < 6:
        resultado = "Suficiente"
    case n if n >= 6 and n < 7:
        resultado = "Bien"
    case n if n >= 7 and n < 9:
        resultado = "Notable"
    case n if n >= 9 and n < 10:
        resultado = "Sobresaliente"
    case _:
        resultado = "Matrícula de Honor"
print("La nota final del alumno es:",resultado)