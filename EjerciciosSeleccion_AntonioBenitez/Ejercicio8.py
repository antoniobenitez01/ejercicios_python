# //Sentencias de Selección - Ejercicio 8
# Programa que recoge un mes del año en número y devuelve
# el número de días que tiene ese mes
# Autor: Antonio Benítez Rodríguez
# Fecha: 16/09/2025
print("Introduzca el número del mes")
mes = int(input("Mes: "))
match mes:
    case 2:
        dias=28
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        dias=31
    case 4 | 6 | 9 | 11:
        dias=30
    case _:
        dias=-1
if dias == -1:
    print("El mes introducido es incorrecto")
else:
    print("El mes introducido tiene",dias,"dias")