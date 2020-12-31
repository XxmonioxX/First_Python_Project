miCoshe = {
    "marca": "Ford",
    "model": "Focus",
    "año": 1964
}

caracteriscas = {
    "año": 2020,
    "color": "Negro"
}

# print(miCoshe.keys())
# print(miCoshe.values())
print(miCoshe)

miCoshe["marca"] = "Audi"
print(miCoshe)

miCoshe.update(caracteriscas)
print(miCoshe)

miCoshe["dueño"] = "Perico palotes lvl. 18"
print(miCoshe)

miCoshe.pop("año")
print(miCoshe)

miCoshe.popitem()
print(miCoshe)
