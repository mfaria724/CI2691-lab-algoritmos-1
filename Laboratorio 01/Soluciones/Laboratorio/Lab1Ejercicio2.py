#
# Lab1Ejercicio2.py
#
# DESCRIPCION: Programa que  dados tres valores enteros a,b,c que cumplen 
#              a>=b>=c, intercambie los valores de manera que cumplan a<=b<=c
#
# Autor: 
#	Prof. Rosseline Rodriguez
#
# Ultima modificacion: 13/01/2018
#

# VARIABLES:
#   a: int  // Entrada y salida
#	b: int  // Entrada y salida
#	c: int  // Entrada y salida

# Valores iniciales:
a = int(input("Introduzca el valor de a:"))
b = int(input("Introduzca el valor de b:"))
c = int(input("Introduzca el valor de c:"))
	
# Precondicion: 
assert(a >= b >= c)

# Calculos:
a,b,c = c,b,a	

# Postcondicion: 
assert(a <= b <= c)

# Salida:
print("a = ")
print(a)
print("b = ")
print(b)
print("c = ")
print(c)