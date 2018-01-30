#
# Lab03Ejercicio3.py
#
# DESCRIPCION: Programa que dado un entero positivo n, determina si n
# es perfecto.
#
# Autor: 
#	Manuel Faria

# Variables:
# n: int 			// ENTRADA: Número que se desea verificar si es primo.
# i: int 			// Iterador que servirá para salir del do.
# k: int 			// Valor donde se almacenará la suma de los divisores.
# esPerfecto: bool	// SALIDA: Variable donde se almacena si n es perfecto o no.

# Valores Iniciales:
n = int(input("Ingrese el número que desea verificar: "))
i,k=1,0
cota=n-i

# Precondicion
assert( n>0 )

# Calculos:
# Invariante y cota:
assert( n>=i )
assert( cota>=0 )

while n>i:
	
	if n%i == 0:
		k=k+i
	
	i=i+1

	#Verifica el invariante y modifica la cota.
	assert( n>=i )
	cota=n-i

if n==k:
	esPerfecto=True
else:
	esPerfecto=False


# Postcondicion:
assert( (n!=k or esPerfecto==True) and (n==k or esPerfecto==False) )

# Salida:
if esPerfecto==False:
	print("El número",n,"NO es perfecto.")
else:
	print("El número",n,"es perfecto.")