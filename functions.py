def escribeHola(usuario="Usuario"):
    print(f"Hola {usuario}.\nQue tal estás?")


escribeHola("Monio")
escribeHola()


def sumaLista(miLista):
    result = 0
    for i in miLista:
        result += i
    print(f"El resultado es {result}")
    return result


def isSmallNumber(number):
    if number > 1000:
        print("Es un numero mu grande")
    else:
        print("Es un número pequeñico")


def compareNumber(number1, number2):
    if number1 > number2:
        print(f"{number1} es mayor que {number2}")
    elif number1 == number2:
        print(f"{number1} es igual que {number2}")
    else:
        print(f"{number2} es mayor que {number1}")


sumaLista([1, 100, -100.5, 500])

x = sumaLista([1, 100, -100.5, 500])

isSmallNumber(x)

compareNumber(x, 100)
compareNumber(x, 1000)
