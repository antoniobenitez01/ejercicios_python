# // Funciones
# Programa que muestra un menú de opciones y funciones
# Autor: Antonio Benítez Rodríguez
# Fecha: 30/09/2025

#IMPORT ============================================================================

import math
import re

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

# EJERCICIO 1. Par o Impar - Devuelve true si el número introducido por parámetro es par
def esPar(n: int) -> bool:
    resultado = False
    if(n%2 == 0):
        resultado = True
    return resultado

# EJERCICIO 2. Calculadora básica - Menú de calculadora (implementa funciones de operación)

def suma(num1,num2): return num1 + num2             # Suma
def resta(num1,num2): return num1 - num2            # Resta
def multiplicacion(num1,num2): return num1 * num2   # Multiplicación
def division(num1,num2):                            # División
    if(num2 == 0): return 0
    else: return num1 / num2

# Calculadora ---------------------------
def calculadora():
    num1 = numCheck("Introduzca el primer número.")
    num2 = numCheck("Introduzca el segundo número.")
    isOperador = False
    while(isOperador is False):
        print("Introduzca el operador por telcado.")
        operador = input("Operador: ")
        match(operador):
            case("+"):
                print("Resultado de suma =",suma(num1,num2))
                isOperador = True
            case("-"):
                print("Resultado de resta =",resta(num1,num2))
                isOperador = True
            case("*"):
                print("Resultado de multiplicación =",multiplicacion(num1,num2))
                isOperador = True
            case("/"):
                print("Resultado de división =",division(num1,num2))
                isOperador = True
            case _:
                print("Opción introducida no válida, inténtelo de nuevo.")

# EJERCICIO 3. Contador de vocales - Cuenta las vocales que hay dentro de una cadena de caracteres
def contar_vocales(cadena: str) -> dict :
    vocales = {
        "a" : 0,
        "e" : 0,
        "i" : 0,
        "o" : 0,
        "u" : 0
    }
    for c in cadena:
        match(c):
            case('a'):
                vocales["a"] = vocales["a"] + 1
            case('e'):
                vocales["e"] = vocales["e"] + 1
            case('i'):
                vocales["i"] = vocales["i"] + 1
            case('o'):
                vocales["o"] = vocales["o"] + 1
            case('u'):
                vocales["u"] = vocales["u"] + 1
    return vocales

# EJERCICIO 4. Máximo hasta fin - Recoge números enteros para luego devolver la lista
def leer_enteros() -> list[int]:
    listaNum = []
    respuesta = ""
    while(respuesta != "fin"):
        try:
            print("Introduzca un número entero")
            respuesta = input("Número: ")
            if(respuesta != "fin"):
                respuesta = int(respuesta)
                listaNum.append(respuesta)
        except ValueError:
            print("No se ha introducido un número, inténtelo de nuevo.")
    return listaNum

# EJERCICIO 5. Números primos - Determina si el número introducido por parámetro es primo, mostrando todos los números primos hasta el introducido
def esPrimo(n: int) -> bool:
    esPrimo = True
    if n <= 1:
        esPrimo = False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                esPrimo = False
    return esPrimo

# EJERCICIO 6. Conversor de temperaturas - Convierte de Celsius a Farenheit y viceversa

def celToFar(c): return c * (9/5) + 32      # Celsius   ->  Farenheit
def farToCel(f): return (5/9)*(f - 32)      # Farenheit ->  Celius

# EJERCICIO 7. Figuras con asteriscos - Funciones para dibujar figuras con astericos

# Triángulo -----------------------
def triangulo(h):
    for i in range(h):
        for j in range(i+1):
            print("*",end=" ")
        print()
# Escalera ------------------------
def escalera(h):
    contador = 0
    i = 0
    while(contador < h):
        if(i % 2 != 0):
            for j in range(i):
                print("*",end=" ")
            contador += 1
            print()
        i += 1
# Rectángulo ----------------------
def rectangulo(w,h):
    for i in range(h):
        for j in range(w):
            print("*",end = "")
        print()

# EJERCICIO 8. Tabla de Multiplicar extendida
def imprimir_tablas(a,b):
    for i in range(a,b+1):
        for j in range(1,11):
            print(i,"*",j,"=",i*j,end="\t")
        print()

# EJERCICIO 9. Validación de Contraseña
def contrasenaValida(s: str) -> bool:
    esValida = False
    hayMayus = False
    hayMinus = False
    haySimbolo = False
    sinEspacio = True
    especiales = "!@#$%^&*()-+?_=,<>/"
    for char in s:
        if(char.isupper and hayMayus is False):
            hayMayus = True
        if(char.islower and hayMinus is False):
            hayMinus = True
        if any(c in especiales for c in char):
            haySimbolo = True
        if(char == " "):
            sinEspacio = False
    if(hayMayus and hayMinus and haySimbolo and sinEspacio and len(s) > 8):
        esValida = True
    return esValida

# EJERCICIO 10. Normaliza nombres
def normalizaNombre(cadena:str) -> str: 
    resultado = ""
    palabras = cadena.split()
    pos = 0
    for str in palabras:
        pos = 0
        for c in str:
            if(pos == 0):
                resultado += c.upper()
            else:
                resultado += c.lower()
            pos += 1
        resultado += " "
    return resultado

# EJERCICIO 11. Contador de dígitos pares e impares
def contarParesImpares(n:int) -> tuple[int,int]:
    numero = n
    pares = 0
    impares = 0
    while numero > 0:
        digito = numero % 10
        if(digito % 2 == 0):
            pares += 1
        else:
            impares += 1
        numero //= 10
    contador = (pares,impares)
    return contador

# EJERCICIO 12. Repetición controlada de texto
def repetirPalabra(palabra: str, n: int) -> str:
    resultado = ""
    for i in range(n):
        resultado += palabra
        if(i != n - 1):
            resultado += "-"
    return resultado

# EJERCICIO 13. Contar vocales y consonantes (sin listas)
def contarVocalesConsonantes(s:str) -> tuple[int,int]:
    numVocales = 0
    consonantes = 0
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for c in s:
        if c.isalpha():
            if c in vocales:
                numVocales += 1
            else:
                consonantes += 1
    contador = (numVocales,consonantes)
    return contador

# EJERCICIO 14. Conversión de segundos a formato h:m:s
def convertirTiempo(segundos: int) -> str:
    hrs = segundos // 3600
    scs = segundos % 3600
    mins = segundos // 60
    scs = segundos % 60
    cadena = f'{hrs}:{mins}:{scs}'
    return cadena

# EJERCICIO 15. Calculadora de potencias con menú
def calcularPotencia(base,exp):
    resultado = base
    for i in range(exp-1):
        resultado = resultado * base
    return resultado

# EJERCICIO 16. Inversión de cadena (sin usar slicing inverso)
def invertirCadena(s: str) -> str:
    resultado = ""
    for c in s:
        resultado = c + resultado
    return resultado

# EJERCICIO 17. Contador de caracteres específicos
def contarCaracter(s:str, c:str) -> int:
    resultado = 0
    for char in s:
        if(char == c):
            resultado += 1
    return resultado

# EJERCICIO 18. Detección de número capicúa
def esCapicua(n:int) -> bool:
    esCapicua = False
    cadena = str(n)
    temp1, temp2 = cadena[:len(cadena)//2], cadena[len(cadena)//2:]
    if(len(temp1) != len(temp2)):
        temp2 = temp2[1:]
    if(temp1 == invertirCadena(temp2)):
        esCapicua = True
    return esCapicua

# EJERCICIO 19. Convertidor de mayúsculas/minúsculas
def convertirMayus(cadena: str) -> str:
    return cadena.upper()
def convertirMinus(cadena: str) -> str:
    return cadena.lower()
def capitalizar(cadena: str) -> str:
    return cadena.capitalize()

#PROGRAMA =========================================================================
respuesta = ""
while(respuesta != 20):
    print("-----------------------------------\n==== MENÚ PRINCIPAL ===="
          +"\n1) Ejercicio 1 - Par o Impar"
          +"\n2) Ejercicio 2 - Calculadora básica"
          +"\n3) Ejercicio 3 - Contador de vocales"
          +"\n4) Ejercicio 4 - Maximo hasta fin"
          +"\n5) Ejercicio 5 - Números primos"
          +"\n6) Ejercicio 6 - Conversor de temperaturas"
          +"\n7) Ejercicio 7 - Figuras con astericos"
          +"\n8) Ejercicio 8 - Tabla de Multiplicar Extendida"
          +"\n9) Ejercicio 9 - Validación de contraseña"
          +"\n10) Ejercicio 10 - Normaliza nombres (cadenas)"
          +"\n11) Ejercicio 11 - Contador de dígitos pares e impares"
          +"\n12) Ejercicio 12 - Repetición controlada de texto"
          +"\n13) Ejercicio 13 - Contar vocales y consonantes (sin listas)"
          +"\n14) Ejercicio 14 - Conversión de segundos a formato h:m:s"
          +"\n15) Ejercicio 15 - Calculadora de potencias con menú"
          +"\n16) Ejercicio 16 - Inversión de cadena (sin usar slicing inverso)"
          +"\n17) Ejercicio 17 - Contador de caracteres específicos"
          +"\n18) Ejercicio 18 - Detección de número capicúa"
          +"\n19) Ejercicio 19 - Convertidor de mayúsculas/minúsculas"
          +"\n20) Salir del programa");
    respuesta = numCheck("Introduzca la opción a elegir.")
    match(respuesta):
        case(1): # EJERCICIO 1 ---------------------------------------------------------
            num = numCheck("Introduzca un número por teclado")
            resultado = esPar(num)
            if(resultado): print("El número introducido es par.")
            else: print("El número introducido es impar")
        case(2): # EJERCICIO 2 ---------------------------------------------------------
            calculadora();
        case(3): # EJERCICIO 3 ---------------------------------------------------------
            print("Introduzca una cadena de caracteres.")
            respuesta = input("Cadena: ")
            vocales = sorted(contar_vocales(respuesta).items(), key=lambda x:x[1])
            vocales.reverse()
            print(vocales)
        case(4): # EJERCICIO 4 ---------------------------------------------------------
            listaNum = leer_enteros()
            if(len(listaNum) != 0):
                listaNum.sort
                print("Número máximo:",listaNum[0])
                print("Número mínimo:",listaNum[len(listaNum)-1])
            else:
                print("La lista de números enteros está vacía.")
        case(5): # EJERCICIO 5 ---------------------------------------------------------
            num = numCheck("Introduzca un número por teclado")
            if(esPrimo(num)):
                print("El número introducido es primo.")
            else:
                print("El número introducido no es primo.")
            n = numCheck("Introduzca el número de primos a mostrar")
            for i in range(n):
                if(esPrimo(i)):
                    print(i,end=" ")
            print()
        case(6): # EJERCICIO 6 ---------------------------------------------------------
            print("--- Conversión Celsius-Farenheit ---")
            chosen = False
            while(chosen is False):
                conversion = numCheck("¿En qué sentido desea realizar la conversión?"
                      +"\n1) Celsius a Farenheit"
                      +"\n2) Farenheit a Celsius"
                      +"\n3) Cancelar")
                match(conversion):
                    case(1):
                        num = numCheck("Introduzca la temperatura en Celsius.")
                        print("Resultado Celsius a Farenheit =",round(celToFar(num),2),"Fº")
                        chosen = True
                    case(2):
                        num = numCheck("Introduzca la temperatura en Farenheit.")
                        print("Resultado Celsius a Farenheit =",round(farToCel(num),2),"Cº")
                        chosen = True
                    case(3):
                        print("Cancelando operación ...")
                        chosen = True
                    case _:
                        print("Opción introducida no válida, inténtelo de nuevo.")
        case(7): # EJERCICIO 7 ---------------------------------------------------------
            print("--- Figuras de asteriscos ---")
            chosen = False
            while(chosen is False):
                print("¿Qué figura desea imprimir?"
                      +"\na) Triángulo rectángulo"
                      +"\nb) Escalera de peldaños"
                      +"\nc) Rectángulo"
                      +"\nd) Cancelar")
                respuesta = input("Opción: ")
                match(respuesta):
                    case("a"):
                        alto = numCheck("Introduzca el alto del triángulo.")
                        triangulo(alto)
                        chosen = True
                    case("b"):
                        peldanyos = numCheck("Introduzca el número de peldaños.")
                        escalera(peldanyos)
                        chosen = True
                    case("c"):
                        alto = numCheck("Introduzca el alto del rectángulo.")
                        ancho = numCheck("Introduzca el ancho del rectángulo.")
                        rectangulo(ancho,alto)
                        chosen = True
                    case("d"):
                        print("Cancelando operación ...")
                        chosen = True
                    case _:
                        print("Opción introducida no válida, inténtelo de nuevo.")
        case(8): # EJERCICIO 8 ---------------------------------------------------------
            chosen = False
            while(chosen is False):
                num1 = numCheck("Introduzca el primer número.")
                num2 = numCheck("Introduzca el segundo número.")
                if(num1 > num2):
                    print("El segundo número debe ser mayor que el primero. Inténtelo de nuevo.")
                else:
                    imprimir_tablas(num1,num2)
                    chosen = True
        case(9): # EJERCICIO 9 ---------------------------------------------------------
            esValida = False
            while(esValida is False):
                print("Introduzca una contraseña válida por teclado.",
                      "\nDebe seguir las siguientes pautas:",
                      "\n- 8 o más caracteres",
                      "\n- Al menos una mayúscula, una minúscula y un símbolo especial",
                      "\n- No puede contener espacios")
                contrasena = input("Contraseña: ")
                esValida = contrasenaValida(contrasena)
                if(esValida):
                    print("Contraseña válida:",contrasena)
                else:
                    print("Contraseña no válida, inténtelo de nuevo.")
        case(10): # EJERCICIO 10 ---------------------------------------------------------
            print("Introduzca una cadena de texto por teclado.")
            cadena = input("Cadena: ")
            normalizado = normalizaNombre(cadena)
            if(normalizado == ""):
                print("Ha ocurrido un error al normalizar la cadena")
            else:
                print("Cadena introducida:",cadena,"\nCadena normalizada:",normalizado)
        case(11): # EJERCICIO 11 ---------------------------------------------------------
            contador = contarParesImpares(numCheck("Introduzca un número."))
            print("Pares:",contador[0],"Impares:",contador[1])
        case(12): # EJERCICIO 12 ---------------------------------------------------------
            print("Introduza una cadena de texto a repetir.")
            cadena = input("Cadena: ")
            num = numCheck("Introduzca cuantas veces quiere repetir la cadena.")
            print("Cadena repetida",num,"veces:",repetirPalabra(cadena,num))
        case(13): # EJERCICIO 13 ---------------------------------------------------------
            print("Introduzca una cadena de texto.")
            cadena = input("Cadena: ")
            contador = contarVocalesConsonantes(cadena)
            print("Vocales:",contador[0],"Consonantes:",contador[1])
        case(14): # EJERCICIO 14 ---------------------------------------------------------
            num = numCheck("Introduzca el tiempo en segundos.")
            print(num,"segundos en h:m:s =",convertirTiempo(num))
        case(15): # EJERCICIO 15 ---------------------------------------------------------
            chosen = False
            while(chosen is False):
                print("¿Que potencia desea calcular?"
                      +"\na) Cuadrado"
                      +"\nb) Cubo"
                      +"\nc) Potencia"
                      +"\nd) Cancelar")
                respuesta = input("Opción: ")
                match(respuesta):
                    case("a"):
                        num = numCheck("Introduzca el número a calcular.")
                        print(f'Potencia al cuadrado de {num} = {num*num}')
                        chosen = True
                    case("b"):
                        num = numCheck("Introduzca el número a calcular.")
                        print(f'Potencia al cubo de {num} = {num*num*num}')
                        chosen = True
                    case("c"):
                        num = numCheck("Introduzca el número a calcular.")
                        potencia = numCheck("Introduzca la potencia a calcular.")
                        print(f'Resultado de {num} con potencia a {potencia} = {calcularPotencia(num,potencia)}')
                        chosen = True
                    case("d"):
                        print("Cancelando operación ...")
                        chosen = True
                    case _:
                        print("Opción introducida no válida, inténtelo de nuevo.")
        case(16): # EJERCICIO 16 ---------------------------------------------------------
            print("Introduzca una cadena de texto.")
            cadena = input("Cadena: ")
            print(f'Cadena inversa = {invertirCadena(cadena)}')
        case(17): # EJERCICIO 17 ---------------------------------------------------------
            print("Introduzca una cadena de texto.")
            cadena = input("Cadena: ")
            caracter = "aaaaa"
            while(len(caracter) > 1 or len(caracter) <= 0):
                print("Introduzca un carácter a buscar.")
                caracter = input("Carácter: ")
                if(len(caracter)>1 or len(caracter) <= 0):
                    print("Debe introducir solo un caracter. Inténtelo de nuevo.")
            print(f'El carácter "{caracter}" aparece {contarCaracter(cadena,caracter)} veces.')
        case(18): # EJERCICIO 18 ---------------------------------------------------------
            num = numCheck("Introduzca un número.")
            if(esCapicua(num)):
                print(f'El número {num} es capicúa.')
            else:
                print(f'El número {num} no es capicúa.')
        case(19): # EJERCICIO 19 ---------------------------------------------------------
            chosen = False
            while(chosen is False):
                print("¿Qué operación desea realizar?"
                      +"\na) Convertir cadena a mayúsculas"
                      +"\nb) Convertir cadena a minúsculas"
                      +"\nc) Capitalizar cadena"
                      +"\nd) Cancelar")
                respuesta = input("Opción: ")
                match(respuesta):
                    case("a"):
                        print("Introduzca una cadena de texto.")
                        cadena = input("Cadena: ")
                        print("Cadena convertida a mayúsculas =",convertirMayus(cadena))
                        chosen = True
                    case("b"):
                        print("Introduzca una cadena de texto.")
                        cadena = input("Cadena: ")
                        print("Cadena convertida a minúsculas =",convertirMinus(cadena))
                        chosen = True
                    case("c"):
                        print("Introduzca una cadena de texto.")
                        cadena = input("Cadena: ")
                        print("Cadena capitalizada =",capitalizar(cadena))
                        chosen = True
                    case("d"):
                        print("Cancelando operación ...")
                        chosen = True
                    case _:
                        print("Opción introducida no válida, inténtelo de nuevo.")
        case(20): # APAGAR PROGRAMA ----------------------------------------------------
            print("Apagando programa ...")
        case _: # ERROR ----------------------------------------------------------------
            print("Opción introducida no válida, inténtelo de nuevo.")