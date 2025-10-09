# Opciones para darle formato a la salida:
num = 5
if num % 2 == 0:
    print("El número",num,"es par")
else:
    print("El número",num,"es impar")
letra ='A'
if num % 2 == 0:
    print("El número {} es par y la letra {}".format(num,letra))
else:
    print("El número {} es impar".format(num))

if num % 2 == 0:
    print(f"El número {num} es par")
else:
    print(f"El número {num} es impar")

if num % 2 == 0:
    print("El número %d es par"%num)
else:
    print("El número %d es impar"%num)