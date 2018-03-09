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

	#import sys    # Se importa la libreria sys para poder utilizar sys.exit()

	#
	# VARIABLES:
	#	N: int    // ENTRADA: Límite superior del rango de enteros de los cuales
	#						  se sumará su respectivo factorial.

def LecturaDatos() -> (list, int):

	N = int(input("Ingrese el número de elementos que tendrá la secuencia: "))

	A = [0]*N

	for i in range(N):
		A[i] = int(input("Introduzca el elemento " + str(i) + ": "))


	return A, N

def Fib(N: int) -> (int):

	a,b=0,1
	for i in range(N):
		c=a+b
		a=b
		b=c

	return c

def ImprimeResultados(A: list, F: list) -> 'void':
	print("El arreglo inicial era: " + str(A))
	print("El nuevo arreglo con los números de Fibonacci es: " + str(F))

A,N=LecturaDatos()
F = [0]*N
for i in range(N):
	F[i]=Fib(A[i])
ImprimeResultados(A,F)