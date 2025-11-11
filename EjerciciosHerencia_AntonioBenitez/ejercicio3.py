# //Herencia - Ejercicio 3
# Programa que define una clase Cuenta Joven que hereda de la clase Cuenta
# Autor: Antonio Benítez Rodríguez
# Fecha: 11/11/2025

from ejercicio2 import Cuenta
from ejercicio1 import Persona

class CuentaJoven(Cuenta):
    def __init__(self, titular:Persona, cantidad:float=0,bonificacion:int=0):
        super().__init__(titular,cantidad)
        if (bonificacion > 100) or (bonificacion < 0): raise Exception("El campo bonificación debe estar entre 0 y 100")
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    def mostrar(self):
        nombre = self.titular.nombre # type: ignore
        print(f"Titular: {nombre} - Cantidad: {self.cantidad}€ - Bonificación: {self.bonificacion}%")