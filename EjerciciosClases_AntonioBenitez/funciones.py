# MENÚ - Función de menú modular con valor mínimo y máximo
def menu(menu : str, min : int, max : int) -> int:
    print(menu)
    opcion = min - 1
    while((opcion < min) or (opcion > max)):
        opcion = numCheck("Elija una opción a continuación.","Opción:")
        if((opcion < min) or (opcion > max)):
            print("Respuesta no válida, inténtelo de nuevo.")
    return opcion

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

# DICTIONARY BY KEY - Ordena un objeto Diccionario por su llave
def dicByKey(dic:dict) -> dict:
    lista = list(dic.keys())
    lista.sort()
    sorted = {i: dic[i] for i in lista}
    return sorted

# BOOLEAN CHECK - Devuelve true si la respuesta es SI y false si la respuesta es NO
def booleanCheck(mensaje:str) -> bool:
    resultado : bool = False
    flag : bool = False
    while(flag is False):
        print(mensaje)
        respuesta = input("Respuesta: ")
        if((respuesta.lower() == "si") or (respuesta.lower() == "sí")):
            resultado = True
            flag = True
        elif(respuesta.lower() == "no"):
            resultado = False
            flag = True
        else:
            print("Respuesta no válida, inténtelo de nuevo.")
            flag = False
    return resultado