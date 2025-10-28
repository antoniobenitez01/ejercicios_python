# // Diccionarios
# Programa que muestra un menú con opciones para interactuar
# sobre una variable tipo Diccionario
# Autor: Antonio Benítez Rodríguez
# Fecha: 28/10/2025

from funciones import *

agenda : dict = {
  "Antonio" : 659454545,
  "María" : 953231245,
  "Jorge" : 652236798,
  "Marta" : 951985676,
  "Kevin" : 682232334,
  "Steven" : 986543235
}

opcion : int = 0
while(opcion != 8):
    opcion = menu("=== DICCIONARIOS ==="+
               "\n1. Listado de teléfonos, usando el orden por defecto"+
               "\n2. Listado de teléfonos por orden alfabético"+
               "\n3. Añadir un nuevo contacto"+
               "\n4. Modificar el teléfono de un contacto"+
               "\n5. Buscar un número de teléfono"+
               "\n6. Eliminar un contacto"+
               "\n7. Borrar el listín telefónico"+
               "\n8. Apagar el programa",1,8)
    match(opcion):
        case 1:
            if(len(agenda) <= 0):
                print("No se ha encontrado ningún registro en la agenda.")
            else:
                print("--- Agenda por defecto ---")
                for nombre,telefono in agenda.items():
                    print(nombre,":",telefono)
        case 2:
            if(len(agenda) <= 0):
                print("No se ha encontrado ningún registro en la agenda.")
            else:
                print("--- Agenda por nombre alfábetico ---")
                sorted = dicByKey(agenda)
                for nombre,telefono in sorted.items():
                    print(nombre,":",telefono)
        case 3:
            print("--- Añadir un nuevo contacto ---")
            print("Introduzca el nombre del nuevo contacto.")
            nombre = input("Nombre: ")
            if(nombre in agenda):
                print("El nombre introducido ya está registrado.")
            else:
                telefono = numCheck("Introduzca el teléfono del nuevo contacto","Teléfono: ")
                agenda[nombre] = telefono
                for nombre,telefono in agenda.items():
                    print(nombre,":",telefono)
        case 4:
            if(len(agenda) <= 0):
                print("No se ha encontrado ningún registro en la agenda.")
            else:
                print("--- Modificar el teléfono de un contacto ---")
                print("Introduzca el nombre del contacto a modificar.")
                nombre = input("Nombre: ")
                if(nombre in agenda):
                    newNum = numCheck(f"Introduzca el nuevo teléfono de {nombre}","Teléfono: ")
                    agenda[nombre] = newNum
                    for nombre,telefono in agenda.items():
                        print(nombre,":",telefono)
                else:
                    print("El contacto introducido no está registrado.")
        case 5:
            if(len(agenda) <= 0):
                print("No se ha encontrado ningún registro en la agenda.")
            else:
                print("--- Buscar un número de teléfono ---")
                print("Introduzca el nombre del contacto a modificar.")
                nombre = input("Nombre: ")
                if(nombre in agenda):
                    print(f"Contacto encontrado = {nombre} : {agenda[nombre]}")
                else:
                    print("El contacto introducido no está registrado.")
        case 6:
            if(len(agenda) <= 0):
                print("No se ha encontrado ningún registro en la agenda.")
            else:
                print("--- Eliminar un contacto ---")
                print("Introduzca el nombre del contacto a eliminar.")
                nombre = input("Nombre: ")
                if(nombre in agenda):
                    print(f"Contacto encontrado = {nombre} : {agenda[nombre]}")
                    respuesta = booleanCheck("¿Está seguro de que quiere borrar el contacto? Escriba SI o NO.")
                    if(respuesta is True):
                        del agenda[nombre]
                    else:
                        print("Cancelando operación ...")
                else:
                    print("El contacto introducido no está registrado.")
        case 7:
            print("Borrando listín telefónico ...")
            agenda = {}
        case 8:
            print("Apagando programa ...")
print("LOOP BORKEN ?")
