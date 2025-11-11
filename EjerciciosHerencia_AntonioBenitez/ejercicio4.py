# //Herencia - Ejercicio 4
# Programa que hace uso de todas las clases creadas anteriormente
# Autor: Antonio Benítez Rodríguez
# Fecha: 11/11/2025

from ejercicio1 import Persona
from ejercicio2 import Cuenta
from ejercicio3 import CuentaJoven

persona = Persona("Antonio","Benítez Rodríguez",23,"26265454R")
cuenta = Cuenta(persona, 50)
joven = CuentaJoven(persona, 50, 50)

persona.mostrar()
cuenta.mostrar()
joven.mostrar()