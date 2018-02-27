#
# Prelab3Ejercicio1.py
#
# Descripcion: El programa calcula la suma de los factoriales
#             de 0 a N
#
# Autor:
#        Rosseline Rodriguez
#
# Ultima modificacion: 03/02/2018


# Variables: 
#     N : int    // ENTRADA: natural que limita la suma
#     suma : int // SALIDA: suma de los factoriales
#     fact : int // auxiliar para el calculo del factorial 
#     cota : int // valor de la cota del ciclo
#     k : int    // variable de control del ciclo

# Definicion del cuantificador productoria
def prod( iterable ):
	p = 1
	for n in iterable:
		p *= n
	return p

# Valores iniciales:
N = int(input("Introduzca un entero positivo: "))

# Precondicion:
assert( N >= 0 )

# Calculos
suma,fact,k = 0,1,0
cota = N + 1 - k

# Verificacion de invariante y cota al inicio del ciclo
assert(0<=k<=N+1 and (fact == prod( j for j in range(1,k) ) ) and suma == sum( prod( j for j in range(1,i+1) ) for i in range(0,k) ) )
assert(cota >= 0)

while(k<=N):
	if( k>0 ):
		fact = fact*k
	else:
		pass
	suma = suma+fact
	k = k + 1
	
        # Verificacion de invariante y cota en cada iteracion:
	assert( 
	   0<=k<=N+1 and fact == prod ( j for j in range(1,k) ) and suma == sum ( prod ( j for j in range(1,i+1) ) for i in range(0,k) ) 
	)
	assert( cota > N+1-k )
	cota = N+1-k
	assert(cota >= 0)

# Postcondicion:
assert( suma == sum ( prod( j for j in range(1,i+1) ) for i in range(0,N+1) ) )

# Salida:
print("la suma de los factoriales de cero a", N ,"es:")
print(suma)
