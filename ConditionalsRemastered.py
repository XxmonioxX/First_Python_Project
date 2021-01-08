aux = 53
aux2 = 36

"""
> < == >= <=
not or and

not true => false
not false => true

true and true => true
true and false => false
false and false => false

true or true => true
true or flase => true
false or false => false


"""
def validacionDeNombre(nombre: str):
    resultado = False
    miListaDeNombresAdmitidos = ["Luis Alfonso", "Erika", "Alejandro", "Ana", "Marcos"]
    for nom in miListaDeNombresAdmitidos:
        if(nombre.lower() == nom.lower()):
            resultado = True
    return resultado



usuario = input("Cual es tu nombre de usuario?")
tamanyoPito = int(input("Cual es el tamaño de tu pito?"))

# validacionDeNombre(usuario) => True/False
if validacionDeNombre(usuario) and tamanyoPito > 12:
    print("Bienvenido")
    apellido = input("Cual es tu primer apellido?")
    if not apellido == "Goanzalez":
        print("Como has burlado mi seguridad?¿?¿?¿?¿?¿?")
elif tamanyoPito > 12:
    print("No estás admitido")
else:
    print("Tienes el pito peuqueño")
