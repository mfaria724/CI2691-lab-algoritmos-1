#
# Lab06Ejercicio2.py
#
# DESCRIPCIÓN: Programa que dado un arreglo A de N números naturales produzca otro
# arreglo F con el número de Fibonacci de cada uno de los valores de A.
#
# Autor: 
#	Manuel Faria 15-10463
#
# Ultima modificacion: 08/03/2018
#

import sys    # Se importa la libreria sys para poder utilizar sys.exit()

# VARIABLES:
#	N: int    				 // ENTRADA: Número de elemntos de de la secuencia.
#	A: array [0,N) of int    // ENTRADA: Secuencia de elementos a verificar.
#	F: array [0,N) of int    // SALIDA: Secuencia de elementos a con Fibonacci.

def LecturaDatos() -> (list, int):

	# VARIABLES:
	#	N: int    				 // ENTRADA: Número de elemntos de de la secuencia.
	#	A: array [0,N) of int    // ENTRADA: Secuencia de elementos a verificar.

	# Precondición:
	assert(True)
	
	N = int(input("Ingrese el número de elementos que tendrá la secuencia: "))

	# Verifica que la secuancia no sea nula o unitaria.
	if N<2:
		print("La secuencia no puede ser unitaria o nula. El programa terminará.")
		sys.exit()

	A = [0]*N

	# Invariante: i<N
	# Cota: N - i
	for i in range(N):
		A[i] = int(input("Introduzca el elemento " + str(i) + ": "))

		# Invariante y cota:
		# Cota: N - i	
		assert(i<N)

	# Postcondición:
	assert(N>1)

	return A, N

def Fib(N: int) -> (int):

	# VARIABLES:
	#	N: int    // ENTRADA: Número de elemntos de de la secuencia.
	#	a: int    // Primer valor.	
	#	b: int    // Segundo valor.
	#	c: int    // Tercer valor.

	# Valores iniciales.
	c,a,b=0,1,0

	# Precondición:
	assert(a==1 and b==0 and N>-1)

	# Invariante: i<N
	# Cota: N - i
	for i in range(N+1):
		if i == 0:
			pass
		elif i!=0:
			c=a+b
			a=b
			b=c

		# Invariante y cota:
		# Cota: N - i	
		assert(i<=N)

	# Postcondición:
	assert(True) # La postcondición es una función recursiva, c==Fib(N)

	return c

def ImprimeResultados(A: list, F: list) -> 'void':

	# VARIABLES:
	#	A: int    // ENTRADA: Secuencia de números iniciales.
	#	F: int    // ENTRADA: Secuencia de números de Fibonacci.	

	print("El arreglo inicial era: " + str(A))
	print("El nuevo arreglo con los números de Fibonacci es: " + str(F))

A,N=LecturaDatos()
F = [0]*N

# Invariante: i<N
# Cota: N - i
for i in range(N):
	F[i]=Fib(A[i])

	# Invariante y cota:
	# Cota: N - i	
	assert(i<N)
	
ImprimeResultados(A,F)