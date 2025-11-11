# //Herencia - Ejercicio 2
# Programa que define una clase Cuenta
# Autor: Antonio Benítez Rodríguez
# Fecha: 11/11/2025

from ejercicio1 import Persona

class Cuenta():

    # ---   CONSTRUCTOR

    def __init__(self, titular:Persona, cantidad:float=0):
        self.__titular = titular
        self.__cantidad = cantidad

    # ---   GETTERS

    @property
    def titular(self):
        return self.__titular
    @property
    def cantidad(self):
        return self.__cantidad
    
    # ---   SETTERS

    @titular.setter
    def titular(self,titular:str):
        self.__titular = titular

    # ---   MÉTODOS

    def ingresar(self,cantidad:float):
        self.__cantidad += cantidad
    def retirar(self, cantidad:float):
        self.__cantidad -= cantidad
    def mostrar(self):
        nombre = self.titular.nombre # type: ignore
        print(f"Titular: {nombre} - Cantidad: {self.cantidad}€")