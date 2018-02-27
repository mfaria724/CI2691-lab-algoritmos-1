#
# Lab02Ejercicio6.py
#
# DESCRIPCION: Dados 2 valores enteros verifica diferentes condiciones

# Autor: 
#	Kevin Mena

# Variables:
# m: entero    // ENTRADA: Primer valor
# n: entero    // ENTRADA: Segundo valor
# resp: entero // SALIDA: Resultado

# Valores iniciales:
m = int(input("Ingrese el primer valor: "))
n = int(input("Ingrese el segundo valor: "))

# Precondicion:
assert(n!=0)

# Calculos:
if m == 10:
    resp = m // n
elif m == 5:
    resp = m * n
elif m == 3:
    resp = m + n
elif m == 2:
    resp = m ** n
else:
    resp = m

# Postcondicion:
assert(
    (m == 10 and resp == m // n) or
    (m == 5 and resp == m * n) or
    (m == 3 and resp == m + n) or
    (m == 2 and resp == m**n) or
    (m != 10 and m != 5 and m != 3 and m != 2 and resp == m)
)

# Salida:
print("El resultado es:", resp)
