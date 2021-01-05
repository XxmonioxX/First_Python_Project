misHijos = ["erika", "luis alfonso", "Ramón", "Alex", "kiwi",
            "Maria Unpajote", "Bernarda"]
for nombre in misHijos:
    print(f"Mi hij@ es: {nombre}")


misnumeritos = [1, 2, 123, -123, 123.323, 1]
for x in misnumeritos:
    print(f"Mi num. es: {x}")

for i in range(0, len(misnumeritos)):
    print(f"Mi hijo num.{i} es: {misnumeritos[i]}")

x = 0
while x < 10:
    print(x)
    # x = x + 1
    x += 1

squares = list(map(lambda x: x**2, range(10)))
squares2 = [x**2 for x in range(10)]
print(squares, squares2)
