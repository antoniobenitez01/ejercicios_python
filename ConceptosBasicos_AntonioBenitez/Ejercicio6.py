# //Conceptos Básicos - Ejercicio 6
# Programa que recoge las notas de tres evaluaciones de un alumno
# para calcular la nota final teniendo en cuenta que cada evaluación
# tiene un porcentaje correspondiente
# Autor: Antonio Benítez Rodríguez
# Fecha: 16/09/2025
print("Introduzca las notas del alumno")
primera = int(input("1º Evaluación: "))
segunda = int(input("2º Evaluación: "))
tercera = int(input("3º Evaluación: "))
notafinal = (primera * 0.2) + (segunda * 0.35) * (tercera * 0.45)
print("La nota final del alumno es:", notafinal, ".")