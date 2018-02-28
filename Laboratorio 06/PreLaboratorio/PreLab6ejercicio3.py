#
# PreLab5Ejercicio3.py
#
# DESCRIPCION: Programa que dado un número N, cuenta la cantidad de divisores
# que tiene N. El resultado es almacenado en la variable cuenta.
#
# Autor: 
#	Manuel Faria 15-10463
#
# Ultima modificacion: 28/02/2018
#

#
# VARIABLES:
#	N: int    // ENTRADA: Número al cual se le contará la cantidad de 
#						  divisores que posee.
#	cuenta: int // SALIDA: Valor donde se almacena la cantidad de divisores de N.

# Subprogramas:

def numeroDivisores(N: [int]) -> int:
	
	# PRECONDICION; N>0
	# POSTCONDICION: cuenta == (sum ( 1 for j in range(1,N+1) if N % j == 0 )) 

	#	cuenta: int // SALIDA: Valor donde se almacena la cantidad de divisores de N.
	#	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine.
	#	i: int // Valor que se usa para iterar sobre los números naturales entre 1 y N.


	# Inicializaciones del ciclo
	cuenta,i=0,1
	cota = N-i+2

	# Verificacion de invariante antes del ciclo:
	try:
		assert( 0<i<=N+1 and (cuenta == (sum ( 1 for j in range(1,i) if N % j == 0 ))))
	except:
		print("Hubo un error en el invariante para los siguientes valores:")
		print("i= " + str(i) + " cuenta= " + str(cuenta))
		sys.exit()

	# Verificación de la cota al inicio del ciclo:
	try:
		assert( cota >= 0 )
	except:
		print("Error: Cota no positiva:")
		print("cota= " + str(cota))
		sys.exit()

	while ( i <= N ):
	   	
		if ( N % i == 0 ):
			cuenta = cuenta + 1

		i = i + 1

		# Verificacion de invariante en cada iteración:
		try:
			assert( 0<i<=N+1 and (cuenta == (sum ( 1 for j in 
				range(1,i) if N % j == 0 ))) )
		except:
			print("Hubo un error en el invariante para los siguientes valores:")
			print("i= " + str(i) + " cuenta= " + str(cuenta))
			sys.exit()
		# Verificación de la decreciente en cada iteración:
		try:
			assert( cota > N-i+2 )
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

		cota = N-i+2

	return cuenta


# Precondicion: 
while True:
	try:
		N=int(input("Introduzca el valor de N: "))
		assert(N > 0)
		break
	except:
		print("Error en los datos, debe volver a introducirlos")
		print("El valor de N debe ser mayor que cero")

cuenta = numeroDivisores(N)

# Postcondicion: 
try:
	assert( cuenta == (sum ( 1 for j in range(1,N+1) if N % j == 0 )) )
except:
	print("Error en los calculos") 
	print("No se cumple la postcondicion con los valores ")
	print("  cuenta = " + str(cuenta))
	print("  N = " + str(N))
	sys.exit() # Se aborta el programa, pues no cumple la postcondicion
 
# Salida:
print("El número",N,
	"tiene", cuenta, "divisores")