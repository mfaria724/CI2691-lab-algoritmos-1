#
# Lab06Ejercicio1.py
#
# DESCRIPCIÓN: Programa que dado un número N, verifica que una secuencia
# de largo N introducida por el usuario es creciente, decreciente, o está
# desordenada.
#
# Autor: 
#	Manuel Faria 15-10463
#
# Ultima modificacion: 08/03/2018
#

import sys    # Se importa la libreria sys para poder utilizar sys.exit()

#
# VARIABLES:
#	N: int    				// ENTRADA: Número de elementos de la secuencia.
#	S: array [0,N) of int   // ENTRADA: Secuencia a verificar.
#	orden: int    			// SALIDA:  Valor que devuelve 0 si está desordenada, 1 si es creciente
#							   y -1 si es decreciente.

# Subprogramas:

def LecturaDatos() -> (list, int):

	# VARIABLES:
	#	N: int    				 // ENTRADA: Número de elemntos de de la secuencia.
	#	S: array [0,N) of int    // ENTRADA: Secuencia de elementos a verificar.

	# Precondición:
	assert(True)

	N = int(input("Ingrese el número de elementos que tendrá la secuencia: "))

	# Verifica que la secuancia no sea nula o unitaria.
	if N<2:
		print("La secuencia no puede ser unitaria o nula. El programa terminará.")
		sys.exit()

	S = [0]*N

	# Invariante: i<N
	# Cota: N - i
	for i in range(N):
		S[i] = int(input("Introduzca el elemento " + str(i) + ": "))

		# Invariante y cota:
		# Cota: N - i	
		assert(i<N)

	# Postcondición:
	assert(N>1)

	return S, N

def DeterminaOrden(S: list, N: int) -> (int):

	# CONSTANTES:
	#	N: int    				// ENTRADA: Número de elemntos de de la secuencia.
	#	S: array [0,N) of int   // ENTRADA: Secuencia de elementos a verificar.
	# VARIABLES:
	#	esCreciente: bool		// Valor que almacena si la secuencia es creciente.
	#	esDecreciente: bool		// Valor que almacena si la secuencia es decreciente.
	#	orden: int 				// SALIDA: Valor que devuelve 0 si está desordenada, 1 si es creciente
	#							   y -1 si es decreciente.

	# Valores iniciales:
	esCreciente, esDecreciente = True, True

	# Precondición:
	assert(N>1)

	# Invariante: i<N
	# Cota: N - i
	for i in range(N-1):
		if S[i]>S[i+1]:
			esCreciente=False
		else:
			esDecreciente=False

		# Invariante y cota:
		# Cota: N - i	
		assert(i<N)

	if esDecreciente==False and esCreciente==False:
		orden = 0
	elif esDecreciente==True:
		orden = -1
	elif esCreciente==True:
		orden = 1

	# Postcondición:
	assert(((esDecreciente==True or esCreciente==True) or orden==0) and
		(esDecreciente==False or orden==-1) and (esCreciente==False or orden==1))

	return orden

def ImprimeResultados(orden: int, S: list) -> 'void':

	# CONSTANTES:
	#	orden: int    				// ENTRADA: Número de elemntos de de la secuencia.
	#	S: array [0,N) of int   	// ENTRADA: Secuencia de elementos a verificar.
	
	# Precondición:
	assert(True)

	if orden == 1:
		print("La secuencia " + str(S) + " es creciente.")
	elif orden == -1:
		print("La secuencia " + str(S) + " es decreciente.")
	else:
		print("La secuencia " + str(S) + " es desordenada.")

	# Postcondición:
	assert(True)

# Programa principal:
S, N = LecturaDatos()
orden = DeterminaOrden(S,N)
ImprimeResultados(orden, S)