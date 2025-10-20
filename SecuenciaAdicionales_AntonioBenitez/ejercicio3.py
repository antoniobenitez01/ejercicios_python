# // Sentencias de Secuencias Adicionales - Ejercicio 3
# Programa que devuelve la suma de dos números, siendo usado para sumar tres números
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/10/2025

#FUNCIONES =========================================================================

def suma(num1,num2): return num1 + num2

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
num1 = numCheck("Introduza el primer número.")
num2 = numCheck("Introduzca el segundo número.")
num3 = numCheck("Introduzca el tercer número.")
print(f'Resultado suma de tres números = {suma(suma(num1,num2),num3)}')