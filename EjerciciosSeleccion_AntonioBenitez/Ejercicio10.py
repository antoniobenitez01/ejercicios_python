# //Sentencias de Selección - Ejercicio 10
# Programa que a partir de la información de un donante
# determina si el paciente puede donar sangre o no
# Autor: Antonio Benítez Rodríguez
# Fecha: 16/09/2025

# ========= ENTRADA DE DATOS ==============

print("Evaluación de donación de sangre")
print("¿Está usted en ayunas? S/N")
teclado = input("Ayunas: ")
if teclado.lower() == "s":
    ayunas = True
else:
    ayunas = False

print("Introduza su edad")
edad = int(input("Edad: "))

print("Introduzca su peso")
peso = float(input("Peso: "))

print("¿Tiene usted la tensión alta? S/N")
teclado = input("Tensión alta: ")
if teclado.lower() == "s":
    alta = True
else:
    alta = False

print("Introduzca su tensión arterial")
tension = float(input("Tensión: "))
tensionbool = False
if alta is False and (tension > 50 and tension < 100):
    tensionbool = True
elif alta is True and (tension > 90 and tension < 180):
    tensionbool = True

print("Introduzca su frecuencia cardiaca en pulsos por minuto")
pulso = int(input("Pulsos: "))

print("¿Es usted varón? S/N")
teclado = input("Varón: ")
if teclado.lower() == "s":
    varon = True
else:
    varon = False

print("Introduzca sus valores de hemoglobina en gramos por litro")
hemo = float(input("Hemoglobina: "))
if varon is True and hemo > 13.5:
    hemobool = True
elif varon is False and hemo > 12.5:
    hemobool = True
else:
    hemobool = False

print("Introduzca su nivel de plaquetas")
plaquetas = float(input("Plaquetas: "))

print("Introduzca su índice de proteína total")
proteina = float(input("Proteínas: "))

# ======== CALCULOS Y RESULTADO =========

resultado = False
if ayunas is False:
    if edad > 18 and edad < 64:
        if peso > 50:
            if tensionbool is True:
                if pulso > 50 and pulso < 110:
                    if hemobool is True:
                        if plaquetas > 150000:
                            if proteina > 6:
                                resultado = True
if resultado is True:
    print("Usted puede donar sangre.")
else:
    print("Usted NO puede donar sangre.")