#
# Lab05Ejercicio3r.py
#
# DESCRIPCIÓN: Programa que dada una secuencia de N números naturales
# pertenecientes al conjunto {1,2,3,4} devuelve el número de ocurrencias
# de cada elemento del conjunto en la secuencia dada.
#
# Autor: 
#	Manuel Faria 15-10463
#
# Ultima modificacion: 22/02/2018
#

import sys    # Se importa la libreria sys para poder utilizar sys.exit()

# VARIABLES:
#	N: int   		// ENTRADA: Número actual de la secuencia.

# Valores iniciales:
ocurrencias = [0,0,0,0]

while True:

	while True: # Verificación del valor cuando es introducido.
		
		try:
			N = int(input("Ingrese un número que pertenezca al conjunto {1,2,3,4}: "))
			assert(0<=N<5)
			break
		
		except:
			print("Debe introducir un número que pertenezca al conjunto {1,2,3,4}")
			print("Ingrese otro número")
		
	if N == 0: # Termina el programa.
		break
	elif N == 1:
		ocurrencias[0] += 1
	elif N == 2:
		ocurrencias[1] += 1
	elif N == 3:
		ocurrencias[2] += 1
	elif N == 4:
		ocurrencias[3] += 1

# Salida:

print("Las ocurrencias del numero 1 son: " + str(ocurrencias[0]))
print("Las ocurrencias del numero 2 son: " + str(ocurrencias[1]))
print("Las ocurrencias del numero 3 son: " + str(ocurrencias[2]))
print("Las ocurrencias del numero 4 son: " + str(ocurrencias[3]))