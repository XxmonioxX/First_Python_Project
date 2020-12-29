miLista = ["red", "green", "blue"]
misNumero = [1, 2, 3, 4, 5, 102]
miListraRandom = [[1, "hola"], miLista, misNumero, (1, "pepe")]

print(miLista)
# miLista = ["ahora", "ya", "no hay colores"]
# print(miLista)
miLista[1] = "verde"
print(miLista)
print(miLista[0])
print(miListraRandom[0][1])

miLista.append("purple")
miLista.extend(["morado", "agua"])
print(miLista)

miLista.pop(0)
print(miLista)

print(miLista.index("morado"))
miLista.pop(miLista.index("morado"))
print(miLista)

miLista.sort()
miLista.sort(reverse=True)
print(miLista)

# listilla = list((1, 2))

print("morado" in miLista)
print("agua" in miLista)
print("1" in misNumero)
