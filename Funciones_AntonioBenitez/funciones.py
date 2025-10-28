# //Funciones
# Programa que muestra un menú de opciones y funciones
# Autor: Antonio Benítez Rodríguez
# Fecha: 30/09/2025

#IMPORT ============================================================================

import random
import math

#FUNCIONES =========================================================================

# NUM CHECK - Comprueba que el dato introducido por teclado es un número
def numCheck(mensaje:str) -> int:
    isNum = False
    while(isNum is False):
        try:
            print(mensaje)
            num = int(input("Número:"))
            isNum = True
        except ValueError:
            print("No se ha introducido un número, inténtelo de nuevo.")
    return num

# ROMBO - Muestra un rombo por consola a partir de un número impar introducido por parámetro
def rombo(num):
    space = int(num/2) + 1 # Calculamos el número de espacios inicial
    for i in range(1,num+1):
        if i%2!=0:
            for j in range(1, space):
                print(" ",end="")
            for k in range(0,i):
                print("*",end="")
            print()
            space -=1
    space = 1
    for i in range(num-1, 0,-1):
        if i%2 != 0:
            for j in range(0,space):
                print(" ",end="")
            for k in range(0,i):
                print("*",end="")
            print()
            space += 1

# ECUACION - Resuelve una ecuación de segundo grado o devuelve 0 si es imposible
def ecuacion(a,b,c):
    if(a != 0):
        try:
            x = (-b + math.sqrt(math.pow(b,2) - 4*a*c)) / 2*a
            resultado = x
        except ValueError:
            resultado = 0
    return resultado

# TABLA NUM - Muestra por consola una tabla de números aleatorios en base a un número de filas y columnas
def tablaNum(filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            print(random.randrange(1,100),end=" ")
        print()

# FACTORIAL - Calcula el factorial de un número entero
def factorial(num):
    resultado = 1
    for i in range(1,num+1):
        resultado = resultado * i
    return resultado

# FIBONACCI - Devuelve el número de la sucesión de Fibonacci en la posición introducida por parámetro
def fibonacci(posicion):
    num = 1
    last = 0
    for i in range(posicion - 1):
        temp = num
        num = num + last
        last = temp
    return num

# TABLA MULT - Muestra por consola la tabla de multiplicar del número introducido por parámetro
def tablaMult(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

#PROGRAMA =========================================================================
respuesta = ""
while(respuesta.lower() != "h"):
    print("==== MENÚ PRINCIPAL ===="
          +"\na) Mostrar un rombo"
          +"\nb) Adivinar un número"
          +"\nc) Resolver una ecuación de segundo grado"
          +"\nd) Tabla de números"
          +"\ne) Cálculo del número factorial de un número"
          +"\nf) Cálculo de un número de la sucesión de Fibonacci"
          +"\ng) Tabla de multiplicar"
          +"\nh) Salir")
    print("Introduzca la opción a ejecutar")
    respuesta = input("Opción: ")
    match(respuesta.lower()):
        case("a"): # ROMBO ---------------------------------------------------------
            num = 10
            while(num % 2 == 0):
                num = numCheck("Introduzca un número impar")
                if(num % 2 == 0):
                    print("El número introducido no es impar, inténtelo de nuevo")
            rombo(num)
        case("b"): # ADIVINAR ------------------------------------------------------
            print("--- ADIVINAR EL NÚMERO ---"
                  +"\nAdivina un número del 1 al 100!")
            randnumber = random.randrange(1,100)
            print(f"DEBUG: {randnumber}")
            guessed = False
            while(guessed is False):
                num = numCheck("Introduzca un número del 1 al 100")
                if(num == randnumber):
                    guessed = True
                    print("Lo has adivinado! Enhorabuena!")
                else:
                    if(num > randnumber):
                        print(f"El número a adivinar es menor que {num}")
                    else:
                        print(f"El número a adivinar es mayor que {num}")
        case("c"): # ECUACION ------------------------------------------------------
            a = numCheck("Introduzca el valor de a")
            b = numCheck("Introduzca el valor de b ")
            c = numCheck("Introduzca el valor de c")
            resultado = ecuacion(a,b,c)
            if(resultado == 0):
                print("La ecuación no es real o el coeficiente a es 0")
            else:
                print(f"Resultado de ecuación = {resultado}")
        case("d"): # TABLA ---------------------------------------------------------
            print("--- TABLA DE NÚMEROS ALEATORIOS ---")
            filas = abs(numCheck("Introduzca un número de filas"))
            columnas = abs(numCheck("Introduzca un número de columnas"))
            tablaNum(filas,columnas)
        case("e"): # FACTORIAL -----------------------------------------------------
            print("--- CÁLCULO DE FACTORIAL ---")
            print(f"Resultado de factorial = {factorial(numCheck("Introduzca un número"))}")
        case("f"): # FIBONACCI -----------------------------------------------------
            print("--- SUCESIÓN DE FIBONACCI ---")
            posicion = numCheck("Introduzca el número de posición")
            print(f"Número en la posicion Nº{posicion}: {fibonacci(posicion)}")
        case("g"): # MULTIPLICAR ---------------------------------------------------
            print("--- TABLA DE MULTIPLICAR ---")
            tablaMult(numCheck("Introduzca un número para hacer su tabla de multiplicar"))
        case("h"): # APAGAR --------------------------------------------------------
            print("Apagando programa ...")
        case _: # ERROR ------------------------------------------------------------
            print("Opción introducida no válida, inténtelo de nuevo.")