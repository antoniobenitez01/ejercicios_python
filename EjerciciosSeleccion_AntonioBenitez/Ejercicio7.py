# //Sentencias de Selección - Ejercicio 7
# Programa que recoge la hora del día y devuelve un saludo
# Autor: Antonio Benítez Rodríguez
# Fecha: 16/09/2025
print("Introduzca la hora del día (de 0 a 24)")
hora = int(input("Hora: "))
match hora:
    case n if n >= 7 and n < 12:
        print("Buenos días.")
    case n if n >= 12 and n < 20:
        print("Buenas tardes.")
    case _:
        print("Buenas noches.")
