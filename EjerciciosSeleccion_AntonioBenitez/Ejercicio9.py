# //Sentencias de Selección - Ejercicio 9
# Programa que recoge un año e indica si es un año bisiesto
# Autor: Antonio Benítez Rodríguez
# Fecha: 16/09/2025
print("Introduzca un año por teclado")
anio = int(input("Año: "))
if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")