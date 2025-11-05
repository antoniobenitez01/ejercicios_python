#FUNCIONES =========================================================================

# NUM CHECK - Comprueba que el dato introducido por teclado es un número
def numCheck(mensaje:str, variable:str) -> int:
    isNum = False
    while(isNum is False):
        try:
            print(mensaje)
            num = int(input(variable))
            isNum = True
        except ValueError:
            print("No se ha introducido un número, inténtelo de nuevo.")
    return num

# REEMPLAZAR VOCALES - Recoge un mensaje String y lo devuelve sin vocales
def reemplazarVocales(mensaje:str) -> str:
    resultado = ""
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',
               'á','é','í','ó','ú','Á','É','Í','Ó','Ú']
    for c in mensaje:
        if c in vocales:
            resultado += "*"
        else:
            resultado += c
    return resultado

# PALABRA MÁS LARGA - Recoge un mensaje String y devuelve la palabra más larga
def palabraMasLarga(mensaje:str) -> str:
    resultado = ""
    palabras = mensaje.split(" ")
    for palabra in palabras:
        if len(palabra) > len(resultado):
            resultado = palabra
    return resultado

# RECTÁNGULO IMPAR - Imprime por consola un rectángulo de números impares desde 100 segun el número de filas y columnas introducidos por parámetro
def rectanguloImpar(filas:int,columnas:int):
    numero = 100
    for i in range(0,filas):
        for j in range(0,columnas):
            while(numero % 2 == 0):
                numero -= 1
            print(numero,end=" ")
            numero -= 1
        print()

# CONTAR CARACTERES - Cuenta cuantas veces ha aparecido cada caracter en un mensaje String
def contarCaracteres(mensaje:str):
    caracteres = []
    for c in mensaje:
        if c.isalpha():
            if ((c in caracteres) == False):
                caracteres.append(c.lower())
    veces = []
    for i in range(0,len(caracteres)):
        veces.append(0)
    for c in mensaje:
        if (c.lower() in caracteres):
            veces[caracteres.index(c.lower())] += 1
    for c in caracteres:
        print(f"'{c}' : {veces[caracteres.index(c)]}")    

#PROGRAMA =========================================================================

respuesta = ""
while(respuesta.lower() != "f"):
    print("\n=== EXÁMEN PYTHON - Menú de Opciones ===\n"
                  +"\na) Reemplazar vocales de una frase"
                  +"\nb) Mensaje cuando el número introducido no sea mayor que el primero"
                  +"\nc) Encontrar la palabra más larga"
                  +"\nd) Mostrar rectángulo con números impares entre 0 y 100"
                  +"\ne) Contar la aparición de cada carácter en una palabra"
                  +"\nf) Salir del programa")
    print("Introduzca la opción a ejecutar")
    respuesta = input("Opción: \n")
    match(respuesta.lower()):
        case("a"):          # REEMPLAZAR VOCALES        ---------------------
            print("Introduzca una frase por teclado")
            frase = input("Frase: ")
            print("FRASE SIN VOCALES:",reemplazarVocales(frase))
        case("b"):          # NUMERO MAYOR QUE PRIMERO  ---------------------
            veces = numCheck("Introduzca las veces que se van a introducir números","Número de veces: ")
            anterior = 0
            for n in range(0,veces):
                num = numCheck("Introduzca un número para comprobar si es mayor que el anterior","Número: ")
                if(num < anterior):
                    print(f"El número introducido no es mayor que el anterior (${anterior})")
                anterior = num
        case("c"):          # PALABRA MAS LARGA         ---------------------
            print("Introduzca una frase por teclado")
            frase = input("Frase: ")
            print("Palabra más larga:",palabraMasLarga(frase));
        case("d"):          # RECTANGULO IMPAR          ---------------------
            filas = numCheck("Introduzca el número de filas","Filas: ")
            columnas = numCheck("Introduzca el número de columnas","Columnas: ")
            rectanguloImpar(filas,columnas)
        case("e"):          # CONTAR CARACTERES         ---------------------      
            print("Introduzca una frase por teclado")
            frase = input("Frase: ")
            contarCaracteres(frase)
        case("f"):          # APAGAR PROGRAMA           ---------------------
            print("Apagando el programa ...")
        case _:             # INPUT ERROR               ---------------------
            print("Opción introducida no válida, inténtelo de nuevo.")