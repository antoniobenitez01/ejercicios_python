# //Sentencias de Selección - Ejercicio 2
# Programa que recoge un número por teclado y muestra
# el día de la semana que le corresponde
# Autor: Antonio Benítez Rodríguez
# Fecha: 16/09/2025
print("Introduzca un número de la semana")
x = int(input("Número: "))
match x:
    case 1:
        string = "Lunes"
    case 2:
        string = "Martes"
    case 3:
        string = "Miércoles"
    case 4:
        string = "Jueves"
    case 5:
        string = "Viernes"
    case 6:
        string = "Sábado"
    case 7:
        string = "Domingo"
    case _:
        string = "Día de la semana incorrecto"
print(string)