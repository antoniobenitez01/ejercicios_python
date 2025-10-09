# //Sentencias de Selección - Ejercicio 5
# Programa que calcula el precio de una entrada de museo
# en torno a la edad del visitante
# Autor: Antonio Benítez Rodríguez
# Fecha: 16/09/2025
print("Introduzca su edad")
edad = int(input("Edad: "))
match edad:
    case n if n < 5:
        precio = 0
    case n if n >= 5 and n < 18:
        precio = 3
    case n if n >= 18 and n < 65:
        precio = 6
    case _:
        precio = 0
if precio == 0:
    print("Entrada gratis")
else:
    print("La entrada al museo cuesta",precio,"€")