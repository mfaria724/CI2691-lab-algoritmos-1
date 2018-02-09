#
# Lab04Ejercicio2.py
#
# DESCRIPCION: Programa que lee los valores de una matriz de 
# dimensiones NxM dadas, e imprime la suma de todos sus elementos.
#
# Autor: 
#	Manuel Faria

# Variables:
# N: int 				// ENTRADA: Número de filas de la matriz.
# M: int 				// ENTRADA: Número de columnas de la matriz.
# A: array[0,N)x[0,M)   // ENTRADA: Matriz de N columnas y M filas.

# Valores Iniciales:
N = int(input("Ingrese el número de filas de la matriz: "))
M = int(input("Ingrese el número de columnas de la matriz: ")) 
A = [[0]*(M) for x in range(N)]

# Precondición:
assert( N>0 and M>0)

# Cálculos:
i,suma=0,0.0

# Invariante y cota:
# Cota: N - i
assert(i<=N)

for i in range(0,N):
	
	j=0

	# Invariante y cota:
	# Cota: M - j	
	assert(j<=M)

	for j in range(0,M):
	
		A[i][j] = float(input("Ingrese el valor del elemeto E" + str(i) + str(j) + ": "))
		suma = suma + A[i][j]

		# Invariante: 
		assert(j<=M)

	# Invariante:
	assert(i<=N)

# Postcondición:
assert( suma == sum ( sum (A[k][h] for h in range(0,M)) for k in range(0,N) ))

# Salida:
print("La suma de los elementos de la matríz es:", suma)