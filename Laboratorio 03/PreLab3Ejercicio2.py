#
# PreLab3Ejercicio2.py
#
# DESCRIPCION: Programa que dado un número N, cuenta la cantidad de divisores
# que tiene N. El resultado es almacenado en la variable cuenta.
#
# Autor: 
#	Manuel Faria 15-10463
#
# Ultima modificacion: 28/01/2018
#

#
# VARIABLES:
#	N: int    // ENTRADA: Número al cual se le contará la cantidad de 
#						  divisores que posee.
#	cuenta: int // SALIDA: Valor donde se almacena la cantidad de divisores de N.
#	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine.
#	i: int // Valor que se usa para iterar sobre los números naturales entre 1 y N.

# Valores iniciales:
N=int(input("Introduzca el valor de N: "))

# Precondicion: 
assert(N > 0)

# Inicializaciones del ciclo
cuenta,i=0,1
cota = N-i+2

# Verificacion de invariante y cota al inicio
assert( 0<i<=N+1 and (cuenta == (sum ( 1 for j in range(1,i) if N % j == 0 ))))
assert( cota >= 0 )

while ( i <= N ):
   	
	if ( N % i == 0 ):
		cuenta = cuenta + 1

	i = i + 1

	# Verificacion de invariante y cota en cada iteracion
	assert( 0<i<=N+1 and (cuenta == (sum ( 1 for j in 
			range(1,i) if N % j == 0 ))) )
	assert( cota > N-i+2 )
	cota = N-i+2

# Postcondicion: 
assert( cuenta == (sum ( 1 for j in range(1,N+1) if N % j == 0 )) )
 
# Salida:
print("El número",N,
	"tiene", cuenta, "divisores")