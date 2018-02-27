#
# Lab1Ejercicio1.py
#
# DESCRIPCION: Programa que calcula el area de un circunferencia
#
# Autor: 
#	Prof. Rosseline Rodriguez
#
# Ultima modificacion: 13/01/2018
#

# VARIABLES:
#   PI: float    // Constante PI
#	R: float     // ENTRADA: radio de la circunferencia
#	area: float  // SALIDA: area de la circunferencia

# Valores iniciales:
PI = 3.14
R = float(input("Introduzca el radio de la circunferencia:"))
	
# Precondicion: 
assert(r > 0)

# Calculos:
area = PI * R * R	

# Postcondicion: 
assert(area == PI*R*R)

# Salida:
print("El area es ")
print(area)