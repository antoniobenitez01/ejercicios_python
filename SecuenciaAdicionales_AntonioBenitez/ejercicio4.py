# // Sentencias de Secuencias Adicionales - Ejercicio 4
# Programa que utilizar una función para rotar una lista de números un número de veces
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================

def rotar(num:int,list:list) -> list:
    rotados = list
    for i in range(num):
        temp = rotados[0]
        rotados.pop(0)
        rotados.append(temp)
    return rotados

# NUM CHECK - Comprueba que el dato introducido por teclado es un número
def numCheck(mensaje):
    isNum = False
    while(isNum is False):
        try:
            print(mensaje)
            num = int(input("Número: "))
            isNum = True
            return num
        except ValueError:
            print("No se ha introducido un número, inténtelo de nuevo.")

#PROGRAMA =========================================================================   
numeros = [7,6,5,3,2,1]
print(f'Lista original: {numeros}')
num = numCheck("Introduzca el número de veces que desea rotar la lista.")
print(f'Lista rotada {num} veces: {rotar(num,numeros)}')