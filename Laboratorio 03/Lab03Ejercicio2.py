#
# Lab03Ejercicio2.py
#
# DESCRIPCION: Programa que dado un entero positivo n, determina si n
# es primo. El programa imprime los divisores de n que son distintos de 1 y n.
#
# Autor: 
#	Manuel Faria

# Variables:
# n: int 			// ENTRADA: Número que se desea verificar si es primo.
# i: int 			// Iterador que servirá para salir del do.
# esPrimo: bool		// SALIDA: Variable donde se almacena si n es primo o no.

# Valores Iniciales:
n = int(input("Ingrese el número que desea verificar: "))
i=1
esPrimo=True
cota=n-i

# Precondicion
assert( n>0 )

# Calculos:
# Invariante y cota:
assert( 1<=i<=n )
assert( cota>=0 )

while i!=n:
	
	if n%i == 0 and i!=1:
		esPrimo=False
		print(i)
	
	i=i+1

	#Verifica el invariante y modifica la cota.
	assert( 1<=i<=n )
	cota=n-i


# Postcondicion:
assert( 1<=i<=n )

# Salida:
if esPrimo==False:
	print("El número",n,"NO es primo.")
elif esPrimo==True:
	print("El número",n,"es primo.")