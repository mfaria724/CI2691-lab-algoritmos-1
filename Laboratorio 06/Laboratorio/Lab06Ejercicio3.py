#
# Lab06Ejercicio3.py
#
# DESCRIPCIÓN: Programa que dados dos números naturales N y M, produce la
# lista de los factores primos de M que son menores o iguales a N,
# indicando por cada uno su exponente en la factorización de M. 
#
# Autor: 
#	Manuel Faria 15-10463
#
# Ultima modificacion: 08/03/2018
#

import sys    # Se importa la libreria sys para poder utilizar sys.exit()

# VARIABLES:
#	N: int    // ENTRADA: Divisor máximo.
#	M: int    // ENTRADA: Ńúmero que se desea descomponer en factores primos

def LecturaDatos() -> (list, int):

	# VARIABLES:
	#	N: int    // ENTRADA: Divisor máximo.
	#	M: int    // ENTRADA: Número al cual se le desean calcular los divisores.

	# Precondición:
	assert(True)
	
	M = int(input("Ingrese el número del cuál desea obtener sus divisores: "))

	# Verifica que la secuancia no sea nula o unitaria.
	N = int(input("Ingrese el divisor máximo del número que acaba de ingresar: "))

	# Postcondición:
	assert(N>1 and M>1)

	return M, N

def verificaImprime(M: int, N: int) -> 'void':

	# VARIABLES:
	# i: int // Iterador

	# Precondición: 
	assert( N >= 0 and M >= 0)

	# Invariante: N >= 0 and M >=0 
	# Cota: N - i
	for i in range(2,N+1):
		if esPrimo(i) == True:
			if M % i == 0:
				print("El número " + str(i) + " es divisor primo de M")
				print(str(i) + " divide exactamente a " + str(M) + " " + str(calcularExponente(M,i)) + " veces.")

		# Invariante y cota:
		# Cota: N - i	
		assert(N >= 0 and M >= 0 )

	# Postcondición:
	assert(True)

def esPrimo(i: int) -> bool:

	# Precondición: 
	assert( i > 0 )

	# VARIABLES:
	# esPrimo: bool // Valor que será devuelto.
	
	esPrimo = True

	# Invariante: all (i % x != 0 for x in range(2,j+1)) == esPrimo
	# Cota: i - x
	for j in range(2,i):
		if i % j == 0:
			esPrimo = False
		# Invariante y cota:
		# Cota: i - x

		assert(all (i % x != 0 for x in range(2,j+1)) == esPrimo)

	# Postcondición:
	assert(all (i % x != 0 for x in range(2,i)) == esPrimo)

	return esPrimo

def calcularExponente(M: int, i: int) -> (int):

	# VARIABLES:
	# k: int // Contador

	# Precondición:
	assert(M >= 0 and i >= 0)
	k = 0

	cota = M -k
	# Cota: 
	assert(M - k >= 0)

	# Invariante:
	assert(True)

	while M % i == 0:
		M = M//i
		k += 1

		# Cota decreciente: 
		assert(cota > M - k)

		cota = M - k

		# Cota acotada inferiormente: 
		assert(M - k >= 0)

		# Invariante:
		assert(True)

	# Postcondición:
	assert(True)

	return k

M, N = LecturaDatos()
verificaImprime(M,N)