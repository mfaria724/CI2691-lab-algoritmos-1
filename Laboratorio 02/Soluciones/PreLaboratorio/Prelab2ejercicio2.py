#
# Prelab2ejercicio2.py
#
# DESCRIPCION: Programa para calcular las raices del polinomio AX^2 + BX + C.
#
# AUTOR: 	Kevin Mena

# Variables:
#    A: entero // ENTRADA: Primer coeficiente
#    B: entero // ENTRADA: Segundo coeficiente
#    C: entero // ENTRADA: Tercer coeficiente
#    x1: float // SALIDA: Primera raiz
#    x2: float // SALIDA: Segunda raiz

# Valores iniciales:
A = int(input("Indique el primer coeficiente: "))
B = int(input("Indique el segundo coeficiente: "))
C = int(input("Indique el tercer coeficiente: "))
x1 = 0.0
x2 = 0.0

# Precondicion:
assert(A != 0 and 4 * A * C <= B * B)

# Calculos:
x1 = (-B + (B*B - 4*A*C)**0.5) / (2*A)
x2 = (-B - (B*B - 4*A*C)**0.5) / (2*A)

# Postcondicion:
assert(
    (A * x1 * x1 + B * x1 + C == 0.0) and
    (A * x2 * x2 + B * x2 + C == 0.0)
)

# Salida:
print("Las raices son: ", x1, " y ", x2)