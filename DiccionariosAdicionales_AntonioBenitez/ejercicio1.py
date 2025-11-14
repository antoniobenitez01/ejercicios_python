# // Diccionarios Adicionales - Ejercicio 1
# Programa que pregunta la usuario sus datos para luego
# guardarlo en un Diccionario y mostrarlo por pantalla
# Autor: Antonio Benítez Rodríguez
# Fecha: 14/11/2025

from funciones import numCheck

# --- PERSONA           // Creamos la clase Persona para guardar datos facilmente
class Persona():
    def __init__(self,nombre:str,edad:int,direccion:str,telefono:int):
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion
        self.__telefono = telefono

    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @property
    def direccion(self):
        return self.__direccion
    @property
    def telefono(self):
        return self.__telefono

    def __str__(self):
        return f"{self.nombre}\t- Edad: {self.edad} Dirección: {self.direccion}\tTelefono: {self.telefono}"

# ---   PROGRAMA

# * Introducción Valores Teclado

print("Introduzca su Nombre.")
nombre = input("Nombre: ")
edad = numCheck("Introduzca su Edad","Edad: ")
print("Introduzca su Dirección")
direccion = input("Dirección: ")
telefono = numCheck("Introduzca su Teléfono","Teléfono: ")

# * Creación Objeto y Diccionario
persona = Persona(nombre,edad,direccion,telefono)
personas : dict = {
    persona.nombre : persona
}
for nombre in personas:
    print(personas[nombre])

