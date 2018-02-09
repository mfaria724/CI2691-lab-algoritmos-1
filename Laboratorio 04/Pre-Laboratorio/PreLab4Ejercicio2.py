#
# PreLab4Ejercicio2.py
#
# DESCRIPCION: Programa que dado un arreglo A de N elementos calcula la suma
# de ellos. Dicho resultado es almacenado en la variable "suma"
#
# Autor: 
#	Manuel Faria

# Variables:
# N: int 			// ENTRADA: Numero de elementos del arreglo A.
# A: array[0,N) 	// ENTRADA: Arreglo donde se almacenan los números a sumar.
# suma: flotante    // SALIDA: Variable donde se alamacenara el valor de la
# 							   suma de los elementos de A.			 
# i: int 			// Valor que servira par iterar sobre el arreglo.

# Valores Iniciales:
i,suma=0,0
N = int(input("Ingrese el número de elementos que tendrá el arreglo: "))
A = [ int(input( "A[" + str(i) + "]=")) for i in range(N) ]

# Precondición:
assert( N > 0 )

# Cota: N-i
# Invariante: 
assert ( 0<=i<=N )

# Calculos:
for i in range(N):
	suma = suma + A[i]

	assert( 0<=i<=N )

# Postcondicion:
assert( suma == sum (A[x] for x in range(N)) )

# Salida:
print("La suma de los numeros del arreglo es:", suma)