# //Sentencias de Repetición - Ejercicio 3
# Programa que recoge números por teclado hasta que
# se introduce el valor 0; mostrando a continuación
# el número de valores introducidos, el valor mínimo,
# el valor máxmimo, la suma de todos y la media aritmética
# Autor: Antonio Benítez Rodríguez
# Fecha: 23/09/2025
listanum = []
num = 1
while num != 0:
    print("Introduzca un número. Si introduce '0' se terminará el programa.")
    num = int(input("Número: "))
    if(num != 0):
        listanum.append(num)
print("Número de valores introducidos:",len(listanum))
listanum.sort()
print("Valor mínimo introducido:",listanum[0])
listanum.sort(reverse=True)
print("Valor máximo introducido:",listanum[0])
suma = 0
for n in listanum:
    suma += n
print("Suma de todos los valores:",suma)
print("Media aritmética de los valores:",suma/len(listanum))
