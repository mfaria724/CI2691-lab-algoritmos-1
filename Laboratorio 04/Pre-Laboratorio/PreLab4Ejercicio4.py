#
# PreLab4Ejercicio4.py
#
# DESCRIPCION: Programa que dada una matriz cuadrara 3x3 determina si esta
# es diagonal o no.
#
# Autor: 
#	Manuel Faria

# Variables:
# M: array[0,3)[0,3)// ENTRADA: Matriz a ser evaluada.
# diagonal: bool    // SALIDA: Variable donde se almacenara si la matriz es 
# 							   diagonal o no.
# i: int 			// Valor que servira par iterar sobre una dimensión del arreglo.
# j: int 			// Valor que servira par iterar sobre otra dimensión del arreglo.

# Valores Iniciales:
diagonal=True
M = [ [int(input("M["+str(i)+","+str(j)+"]=")) for i in range(3)] for j in range(3)]

# Precondición
assert(True)

# Calculos:
for i in range(3):
	for j in range(3):
		if i!=j and M[i][j]!=0:
			diagonal=False

		assert(True)
	assert(True)
			
# Postcondicion:
assert( diagonal == all (all (M[x][y]==0 for x in range(3) if x!=y) for y in range(3)) )

# Salida:

if diagonal==True:
	print("La matriz SI es diagonal")
else: 
	print("La matriz NO es diagonal")