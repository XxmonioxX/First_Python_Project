"""
Reto -> Hacer calculadora
La calculadora será por consola, 
operaciones simples de dos números


Necesitamos:
-   Métodos para hacer calculos <--- funciones de 2 parametros
-   Algo para que el usuario introduzca datos por consola
-   Mostar el resultado de la operación
-   Algo para que el usuario se capaz de elegir que hacer
"""

def add(num1: int, num2: int):
    resultado = num1 + num2
    print(f"El resultado de la suma es {resultado}")


def substract(num1: int, num2: int):
    resultado = num1 - num2
    print(f"El resultado de la resta es {resultado}")


def multiplication(num1: int, num2: int):
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es {resultado}")


def division(num1: int, num2: int):
    resultado = num1 / num2
    print(f"El resultado de la division es {resultado}")


add(4, 5)
substract(10, 5)
multiplication(9, 8)
division(50, 5)