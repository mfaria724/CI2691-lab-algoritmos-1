#
# Lab05Ejercicio2r.py
#
# DESCRIPCION: Programa que dado un número 
#
# Autor: 
#	Manuel Faria 15-10463
#
# Ultima modificacion: 20/02/2018
#

import sys    # Se importa la libreria sys para poder utilizar sys.exit()

	# CONSTANTES:
	#	maximo: int // Número máximo de elementos de la secuencia.

	# VARIABLES:
	#	cantidad: int   // Cantidad de elementos de la secuencia.
	#	ordenado: bool  // SALIDA: Valor que almacena si la secuencia está ordenada crecientemente. 
	#	anterior: int 	// ENTRADA: Valor que almacena el último elemento de la secuencia. 
	#	N: int 			// ENTRADA: Valor del elemento de la secuencia que ingresa el usuario.

N = int(input('Ingrese un número natural: '))

i=N
intentos = 0

assert(True)

while i!=4:
	anterior=i
	if i%2==0:
		i=i//2
	else:
		i=i*3+1
	intentos+= 1
	print('Intentos: ' + str(intentos))
	print('Valor de x: ' + str(i))