number = 1998
floatNumber = 10.51
double = 10.1231231391287391827391837918

print(f"suma -> {number + 2}")
print(f"resta -> {number - 2}")
print(f"multiplicacion -> {number * 2}")
print(f"potencia {number ** 2}")
print(f"division -> {number / 2}")
print(f"division con resultado entero -> {number // 2}")
print(f"modulo -> {number % 2}")

print(int(floatNumber))
print(float(number))

manoloAge = int(input("Cuantos años tiene Manolo?\n "))

print(manoloAge)
"""
Orden de operaciones
1º Parentesis
2º Potencia
3º Multiplicacion y division
4º suma y resta
"""
print(10 + 20 * 5 / 2**3)
