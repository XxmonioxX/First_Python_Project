'''
Operadores:
    Mayor que '>'
    1 > 10 => False
    1 > -1 => True
    1 > 1 => False

    Menor que '<'
    1 < 10 => True
    1 < -1 => False
    1 < 1 => False

    Igual a '=='
    1 = 10 => False
    1 = -1 => False
    1 = 1 => True

    Mayor o Igual que '>='
    1 >= 10 => False
    1 >= -1 => True
    1 >= 1 => True

    Menor o Igual que '<='
    1 <= 10 => True
    1 <= -1 => False
    1 <= 1 => True

    and
    Necesita que TODAS las expresiones sean True sino es False
    1 <= 10 and 10 == 20 => False
    True and True and True and False => False
    True and True and True and True => True

    or
    Conque una sola expresión sea True el resultado es True sino False
    1 <= 10 or 10 == 20 => True
    True or True or True or False => True
    True or True or True or True => True

    not
    Invierte el resultado de la expresión
    not 1 <= 10 => False
    not 1 == 10 => True
    not (1 == 1 and 10 == 20) => True
    not(not (10 == 10) and ((50 > 49 or 12/4 == 3) or 50 < 144/12)) => True

'''

x = 10
usuario = "Luis Alfonso"
# True / False
if x > 10:
    print("x es mayor que 10")
    if usuario == "Erika":
        print("el usuario es 'Erika'")
else:
    print("x es menor o igual que 10 o el usuario no es 'Erika'")

texto = input("Texto a evaluar: ")
print(f"El texto introducido tiene {len(texto)} caracteres")
if len(texto) > 10:
    print("El texto es largo")
elif len(texto) > 5:
    print("El texto es ni mu largo ni mu corto")
else:
    print("El texto es corto")


TextoPorPantalla = input("Me he clavado el lapiz?\nPresione S\\N\n")
if TextoPorPantalla.lower() == "s" or TextoPorPantalla.lower() == "n":
    if TextoPorPantalla.lower() == "s":
        print("Me morio")
    else:
        print("toy vivo")
else:
    print(f"Tecla '{TextoPorPantalla.lower()}' incorrecta")
    print("Ejecute el programa de nuevo")
