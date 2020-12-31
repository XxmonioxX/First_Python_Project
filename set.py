miSet = {"Pepe", "Juan", "Erika", "Luis"}
miSet2 = {"Juan", "Luis", "Lucas", "Nieves", "Maria"}
misNumero = {1, 5, 19, 123}

# Esto da error ya que los sets no tienen indices
# print(miSet[0])

PepeisPresent = "Pepe" in miSet
print(PepeisPresent)

miSet.add("Alejandro")
miSet.add("Luis")
miSet.add("luis")
print(miSet)

miSet.remove("luis")
print(miSet)

miSet.pop()
print(miSet)

miSet.update(miSet2)
print(miSet)

miSet = miSet.union(miSet2, misNumero)
print(miSet)

"""
Lista -> Tiene indices y está ordenada, se puede editar
Tupla -> Tiene indices y está ordenada, no se puede editar
Set -> No tiene indices y no está ordenada, se puede editar

Todas son listas pero con diferentes caracteríscas
"""
