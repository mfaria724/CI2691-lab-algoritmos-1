#
# Lab04Ejercicio1.py
#
# DESCRIPCION: Programa que lee los coeficientes de hasta que se introduzca el
# valor cero, y los alamacena en un arreglo. Muestra el grado del polinomio y 
# luego escribe el polinomio en notación polinomial. El grado del polinomio no
# puede ser mayor que un valor M dado inicialmente por el usuario.  
#
# Autor: 
#	Manuel Faria

# Variables:
# M: int 			// ENTRADA: Grado máximo del polinomio.
# A: array[0,M+1)   // ENTRADA: Arreglo que contiene los coeficientes.

# Valores Iniciales:
M = int(input("Ingrese el grado máximo del polinomio: "))
A = [0]*(M+1)

# Precondición:
assert(M>=0)

# Calculos:
# Invariante y cota:
# Cota: N - i
assert(True)

for i in range(0,M+1):
	A[i]=int(input("Ingrese el valor del coeficiente C" + str(i) + ": "))

	assert(True)

print("Grado del polinomio:" + str(M))
print("P(x)=", end='')

# Invariante y cota:
# Cota: N - i
assert(True)

for j in range(0,M+1):
	if A[j]!=0:
		print(str(A[j]) + "x^" + str(j), end='')
		if j!=M and A[i]!=0:
			print("+", end='')

	assert(True)

print("")

# Postcondición:
assert(True)