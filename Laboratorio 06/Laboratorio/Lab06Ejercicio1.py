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
	#	N: int    // ENTRADA: Límite superior del rango de enteros de los cuales
	#						  se sumará su respectivo factorial.

def LecturaDatos() -> (list, int):

	N = int(input("Ingrese el número de elementos que tendrá la secuencia: "))

	S = [0]*N

	for i in range(N):
		S[i] = int(input("Introduzca el elemento " + str(i) + ": "))


	return S, N

def DeterminaOrden(S: list, N: int) -> (int):

	esCreciente, esDecreciente = True, True

	for i in range(N-1):
		if S[i]>S[i+1]:
			esCreciente=False
		else:
			esDecreciente=False

	if esDecreciente==False and esCreciente==False:
		orden = 0
	elif esDecreciente==True:
		orden = -1
	elif esCreciente==True:
		orden = 1

	return orden

def ImprimeResultados(orden: int, S: list) -> 'void':
	if orden == 1:
		print("La secuencia " + str(S) + " es creciente.")
	elif orden == -1:
		print("La secuencia " + str(S) + " es decreciente.")
	else:
		print("La secuencia " + str(S) + " es desordenada.")


S, N = LecturaDatos()
orden = DeterminaOrden(S,N)
ImprimeResultados(orden, S)