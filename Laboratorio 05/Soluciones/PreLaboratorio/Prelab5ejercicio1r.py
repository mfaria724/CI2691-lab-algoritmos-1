#
# Prelab5ejercicio1r.py
#
# DESCRIPCION: Ejercicio del Prelaboratorio 2 modificado con acciones que verifican las aserciones.
#              El programa para calcular las raices del polinomio AX^2 + BX + C. Versión robusta
#
# AUTOR: 	Kevin Mena y Rosseline Rodriguez

# Variables:
#    A: entero // ENTRADA: Primer coeficiente
#    B: entero // ENTRADA: Segundo coeficiente
#    C: entero // ENTRADA: Tercer coeficiente
#    x1: float // SALIDA: Primera raiz
#    x2: float // SALIDA: Segunda raiz

import sys

# Valores iniciales:
x1 = 0.0
x2 = 0.0
   
while True:

   A = int(input("Indique el primer coeficiente: "))
   B = int(input("Indique el segundo coeficiente: "))
   C = int(input("Indique el tercer coeficiente: "))

   # Precondicion:
   try:
      assert(A != 0 and 4 * A * C <= B * B)
      break
   except:
      print("La precondicion no se cumple: primer coeficiente nulo o discriminante negativo ")
      print("Vuelva a intentar")

# Calculos:
x1 = (-B + (B*B - 4*A*C)**0.5) / (2*A)
x2 = (-B - (B*B - 4*A*C)**0.5) / (2*A)

# Postcondicion:
try:
   assert(
      (A * x1 * x1 + B * x1 + C == 0.0) and
      (A * x2 * x2 + B * x2 + C == 0.0)
   )
except:
   print("Error en los calculos no se cumple la postcondicion ")
   print("El programa terminara")
   sys.exit()

# Salida:
print("Las raices son: ", x1, " y ", x2)
