#
# PreLab3Ejercicio1.py
#
# DESCRIPCION: Programa que dado un número N, calcula la sumatoria 
# de los factoriales desde 0 hasta N. El resultado de la suma es
# almacenado en la variable suma 
#
# Autor: 
#	Manuel Faria 15-10463
#
# Ultima modificacion: 26/01/2018
#

#
# VARIABLES:
#	N: int    // ENTRADA: Límite superior del rango de enteros de los cuales
#						  se sumará su respectivo factorial.
#	k: int    // Valor que permite recorrer los enteros entre 0 y N.
#	fact: int // Valor donde se guardará el factorial del valor que posea k
#	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine
#	suma: int // SALIDA: Valor de la sumatoria del factorial de los enteros 
#						 entre 0 y N-1.

# Definición de productoria
def prod( iterable ):
	p= 1
	for n in iterable:
		p *= n
	return p

# Valores iniciales:
N=int(input("Introduzca el valor de N: "))

# Precondicion: 
assert(N >= 0)

# Inicializaciones del ciclo
k,suma,fact=0,0,1
cota = N+1-k

# Verificacion de invariante y cota al inicio
assert( 0<=k<=N+1 and (suma == (sum ( prod ( j for j in range(1,i+1)) 
		for i in range(0,k)))) and (fact == prod ( j for j in range(1,k) )) )
assert( cota >= 0 )

while ( k <= N ):
   	
	if ( k > 0 ):
		fact = fact*k

	suma = suma + fact

	k = k + 1

	# Verificacion de invariante y cota en cada iteracion
	assert( 0<=k<=N+1 and (suma == (sum ( prod ( j for j in range(1,i+1)) 
			for i in range(0,k)))) and (fact == prod ( j for j in range(1,k) )) )
	assert( cota > N+1-k )
	cota = N+1-k

# Postcondicion: 
assert( suma == sum ( prod ( j for j in range(1,i+1) ) for i in range(0,N+1) ) )
 
# Salida:
print("La sumatoria de los factoriales de los enteros positivos entre 0 y",N,
	"es:", suma)