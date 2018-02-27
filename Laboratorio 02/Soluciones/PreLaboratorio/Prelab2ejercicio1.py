#
# Prelab2ejercicio1.py
#
# DESCRIPCION: Programa que calcula el valor absoluto de a
#
# AUTOR: 	Kevin Mena

# Variables:
#    a: entero // ENTRADA: Valor a sacarle el absoluto
#    b: entero // Salida: Valor absoluto

# Valores iniciales:
a = int(input("Ingrese un valor: "))

# Precondicion:
assert(True)

# Calculos:
if a >= 0: 
    b = a
else: 
    b = -a

# Postcondicion:
assert(b == abs(a))

# Salida:
print("El valor absoluto es:", b)