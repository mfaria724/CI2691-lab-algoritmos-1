#
# Lab3Ejemplo1.py
#
# DESCRIPCION: Programa que dado un número N,
# calcula la sumatoria de los números pares positivos menores a N. 
# Dicho sumatoria es almacenada en suma.
#
# Versión de: 
#	Manuel Faria
#
# Ultima modificacion: 20/04/2015
#

#
# VARIABLES:
#	N: int    // ENTRADA: Límite superior del rango de enteros pares a sumar
#	k: int    // Valor que permite recorrer los enteros entre 0 y N-1
#	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine
#	suma: int // SALIDA: Valor de la sumatoria de los enteros pares entre 0 y N-1

# Valores iniciales:
N=int(input("Introduzca número N: "))

def prod(iterable):
	p=1
	for n in iterable:
		p*=n
	return p

# Precondicion: 
assert(N > 0)

# Inicializaciones del ciclo
e,i,fact=0,0,1
cota = N-i

# Verificacion de invariante y cota al inicio
assert(e == sum (1/(prod (t for t in range(1,k))) for k in range(1,i+1)))
print("E",e)
print("cuant", sum (1/(prod (t for t in range(1,k))) for k in range(1,i+1)))
assert( cota >= 0 )

while ( i < N ):
   
	print("Este es el valor de i", i)
	if i!=0:
		fact=fact*i
	print("Valor de e antes:",e)
	print("Valor de fact antes:",fact)
	e=e+(1/fact)
	print("Valor de e despues:",e)
	

	# Verificacion de invariante y cota en cada iteracion
	print("E",e)
	print("cuant", sum (1/(prod (t for t in range(1,k))) for k in range(1,i+1)))
	assert(e == sum (1/(prod (t for t in range(1,k))) for k in range(1,i+1)))
	
	i=i+1
	assert( cota > N-i )
	cota = N-i   
# Postcondicion: 
print("E",e)
print("cuant", sum (1/(prod (t for t in range(1,k))) for k in range(1,i)))
assert(e == sum (1/(prod (t for t in range(1,k))) for k in range(1,i)))

# Salida:
print("La aproximación de e hasta ",N," es: ")
print(e)
