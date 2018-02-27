#
# Lab02Ejercicio4.py
#
# DESCRIPCION: Dados tres valores enteros A, B y C con valores diferentes, \
# determinar el valor máximo de ellos.

# Autor: 
#	Kevin Mena

# Variables:
# a: entero      // ENTRADA: Primer valor
# b: entero      // ENTRADA: Segundo valor
# c: entero      // ENTRADA: Tercer valor
# maximo: entero // SALIDA: Valor del maximo

# Valores iniciales:
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
c = int(input("Ingrese el tercer valor: "))

# Precondicion:
assert(a != b and b != c and a != c)

# Calculos:

if a > b and a > c:
    maximo = a
elif b > a and b > c:
    maximo = b
else:
    maximo = c

# Postcondicion:
assert(
    (a > b and a > c and maximo == a) or 
    (b > a and b > c and maximo == b) or
    (c > a and c > b and maximo == c)
)

# Salida:
print("El valor maximo es", maximo)