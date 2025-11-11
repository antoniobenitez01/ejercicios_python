# //Clases - Ejercicio 2
# Programa que utiliza la clase Persona para almacenar un diccionario de Contactos
# Autor: Antonio Benítez Rodríguez
# Fecha: 11/11/2025

from ejercicio1 import Persona
from funciones import *

p1 = Persona("Antonio","Calle Flores",987656565)
p2 = Persona("Maria","Calle Dirección",524656565)
p3 = Persona("Carlos","Calle Velazquez",657656565)

contactos : dict = {
    p1.nombre.upper() : p1,
    p2.nombre.upper() : p2,
    p3.nombre.upper() : p3
}

opcion : int = 0
while(opcion != 6):
    opcion = menu("\n=== AGENDA DE CONTACTOS ==="+
               "\n1. Listado de Contactos por Orden Alfabético"+
               "\n2. Añadir un nuevo Contacto"+
               "\n3. Modificar un Contacto"+
               "\n4. Buscar un número de teléfono"+
               "\n5. Eliminar un contacto"+
               "\n6. Apagar el programa\n",1,6)
    match(opcion):
        case 1: # ---   LISTADO ALFABETICO

            if(len(contactos) == 0):
                print("La Agenda de Contactos está vacía.")
            else:
                print("\n--- Listado de Contactos por Orden Alfabético ---\n")
                sorted = dicByKey(contactos)
                for persona in sorted:
                    print(sorted[persona])
                    
        case 2: # ---   AÑADIR NUEVO CONTACTO

            print("Introduzca el nombre del nuevo Contacto")
            newNombre = input("Nombre: ").upper()
            if newNombre in contactos:
                if(booleanCheck("El nombre introducido ya está registrado, desea actualizar su teléfono? (SI/NO)")):
                    newTelefono = numCheck("Introduzca el teléfono del nuevo Contacto","Teléfono: ")
                    contactos[newNombre].telefono = newTelefono
                    print(contactos[newNombre])
                else:
                    print("Operación cancelada. Volviendo al Menú Principal ...")
            else:
                print("Introduzca la dirección del nuevo Contacto")
                newDireccion = input("Direccion: ")
                newTelefono = numCheck("Introduzca el teléfono del nuevo Contacto","Teléfono: ")
                try:
                    nuevoContacto = Persona(newNombre,newDireccion,newTelefono)
                    contactos[nuevoContacto.nombre.upper()] = nuevoContacto
                    print("Contacto introducido correctamente:")
                    print(contactos[nuevoContacto.nombre.upper()])
                except:
                    print("Ha ocurrido un error al crear el nuevo Contacto.")

        case 3: # ---   MODIFICAR CONTACTO

            if(len(contactos) == 0):
                print("La Agenda de Contactos está vacía.")
            else:
                for persona in contactos:
                    print(contactos[persona])
                print("\nIntroduzca el nombre del Contacto a modificar")
                nombreMod = input("Nombre: ").upper()
                if(nombreMod in contactos):
                    newDireccion = input("Direccion: ")
                    newTelefono = numCheck("Introduzca el nuevo teléfono del Contacto","Teléfono: ")
                    contactos[nombreMod].direccion = newDireccion
                    contactos[nombreMod].telefono = newTelefono
                else:
                    if(booleanCheck("El nombre introducido no está registrado. ¿Desea añadirlo?")):
                        print("Introduzca la Dirección del nuevo Contacto")
                        newDireccion = input("Direccion: ")
                        newTelefono = numCheck("Introduzca el Teléfono del nuevo Contacto","Teléfono: ")
                        try:
                            nuevoContacto = Persona(newNombre,newDireccion,newTelefono)
                            contactos[nuevoContacto.nombre.upper()] = nuevoContacto
                            print("Contacto introducido correctamente:")
                            print(contactos[nuevoContacto.nombre.upper()])
                        except:
                            print("Ha ocurrido un error al crear el nuevo Contacto.")
                    else:
                        print("Operación cancelada. Volviendo al Menú Principal ...")

        case 4: # ---   BUSCAR NUMERO TELEFONO

            if(len(contactos) == 0):
                print("La Agenda de Contactos está vacía.")
            else:
                telfBuscar = numCheck("Introduzca el Teléfono a buscar","Teléfono: ")
                contador = 0
                for persona in contactos:
                    if(contactos[persona].telefono == telfBuscar):
                        print(contactos[persona])
                        contador += 1
                if(contador == 0):
                    print("El teléfono introducido no se ha encontrado.")

        case 5: # ---   ELIMINAR CONTACTO

            if(len(contactos) == 0):
                print("La Agenda de Contactos está vacía.")
            else:
                for persona in contactos:
                    print(contactos[persona])
                print("\nIntroduzca el nombre del Contacto a eliminar")
                nombreEliminar = input("Nombre: ").upper()
                if nombreEliminar in contactos:
                    if(booleanCheck("¿Está seguro de que desea eliminar este Contacto? (SI/NO)")):
                        del contactos[nombreEliminar]
                    else:
                        print("Operación cancelada. Volviendo al Menú Principal ...")
                else:
                    print("El nombre introducido no está registrado.")

        case 6: # ---   APAGAR PROGAMA

            print("Apagando programa ...")