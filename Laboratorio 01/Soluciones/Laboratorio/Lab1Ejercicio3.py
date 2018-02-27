#
# Lab1Ejercicio3.py
#
# DESCRIPCION: Programa que dado un entero b dice si b es par
#
# Autor: 
#	Prof. Rosseline Rodriguez
#
# Ultima modificacion: 13/01/2018
#
# VARIABLES:
#   B: int       // ENTRADA: valor entero 
#	esPar: bool  // SALIDA: resultado

# Valores iniciales:
B = int(input("Introduzca el valor de B:"))
	
# Precondicion: ninguna

# Calculos:
esPar = (B%2 == 0)	

# Postcondicion: 
assert(esPar == (B%2 == 0))

# Salida:
print("B es par? ")
print(esPar)
