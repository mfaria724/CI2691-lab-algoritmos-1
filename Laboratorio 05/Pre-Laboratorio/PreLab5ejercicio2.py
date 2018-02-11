#
# PreLab5Ejercicio2.py
#
# DESCRIPCION: Programa que dado un número N, calcula la sumatoria 
# de los factoriales desde 0 hasta N. El resultado de la suma es
# almacenado en la variable suma 
#
# Autor: 
#	Manuel Faria 15-10463
#
# Ultima modificacion: 11/02/2018
#

import sys    # Se importa la libreria sys para poder utilizar sys.exit()

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



# Verificación de la precondición: 
while True:
	try:
		N=int(input("Introduzca el valor de N: "))
		assert(N >= 0)
		break
	except:
		print("Error en los datos, debe volver a introducirlos")
		print("N debe ser un valor no negativo")

# Inicializaciones del ciclo
k,suma,fact=0,0,1
cota = N+1-k

# Verificacion de invariante antes del ciclo:
try:
	assert( 0<=k<=N+1 and (suma == (sum ( prod ( j for j in range(1,i+1)) 
		for i in range(0,k)))) and (fact == prod ( j for j in range(1,k) )) )
except:
	print("Hubo un error en el invariante para los siguientes valores:")
	print("k= " + str(k) + " suma= " + str(suma))
	sys.exit()

# Verificación de la cota al inicio del ciclo:
try:
	assert( cota >= 0 )
except:
	print("Error: Cota no positiva:")
	print("cota= " + str(cota))
	sys.exit()

while ( k <= N ):
   	
	if ( k > 0 ):
		fact = fact*k

	suma = suma + fact

	k = k + 1

	# Verificacion de invariante en cada iteración:
	try:
		assert( 0<=k<=N+1 and (suma == (sum ( prod ( j for j in range(1,i+1)) 
			for i in range(0,k)))) and (fact == prod ( j for j in range(1,k) )) )
	except:
		print("Hubo un error en el invariante para los siguientes valores:")
		print("k= " + str(k) + " suma= " + str(suma))
		sys.exit()
	
	# Verificación de la decreciente en cada iteración:
	try:
		assert( cota > N+1-k )
	except:
		print("Error: Cota no decreciente:")
		print("cota= " + str(cota))
		sys.exit()

	# Verificación de la cota positiva en cada iteración:
	try:
		assert( cota >= 0 )
	except:
		print("Error: Cota no positiva:")
		print("cota= " + str(cota))
		sys.exit()

	cota = N+1-k

# Postcondicion: 
try:
	assert( suma == sum ( prod ( j for j in range(1,i+1) ) for i in range(0,N+1) ) )
except:
	print("Error en los calculos") 
	print("No se cumple la postcondicion con los valores ")
	print("  k = " + str(k))
	print("  N = " + str(N))
	print("  suma = " + str(suma))
	sys.exit() # Se aborta el programa, pues no cumple la postcondicion

# Salida:
print("La sumatoria de los factoriales de los enteros positivos entre 0 y",N,
	"es:", suma)