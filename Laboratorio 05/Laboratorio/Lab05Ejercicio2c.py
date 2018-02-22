#
# Lab05Ejercicio2c.py
#
# DESCRIPCIÓN: Programa que dado un número natural N determina la 
# cantidad de intentos que se deben hacer para llegar al número 4 
# utilizando la siguiente conjetura de secuencias de números naturales:
# 	1. Si el número es par el siguiente número será igual al número anterior 
# 	entre 2.
#	2. Si es impar, el siguiente número será el número anterior multiplicado
#	por 3 más 1.
#
# Autor: 
#	Manuel Faria 15-10463
#
# Ultima modificacion: 22/02/2018
#

import sys    # Se importa la libreria sys para poder utilizar sys.exit()

# VARIABLES:
#	N: int   		// ENTRADA: Número incial de la secuencia.
#	i: int 			// Iterador del ciclo. 
#	intentos: int 	// SALIDA: Valor que almacena la cantidad de intentos 
#						necesarios para llegar a la secuencia 4,2,1 usando la 
#						conjetura.  
#	N: int 			// ENTRADA: Valor del elemento de la secuencia que ingresa el usuario.

# Verificación del valor de entrada de por parte del usuario.
try:
	N = int(input('Ingrese un número natural: '))
	assert(N>0)

except:
	print("Debe ingresar un número natural")
	sys.exit() # Se aborta el programa, pues no cumple el invariante



# Valores iniciales
i,intentos=N,0

# Invariante
try:
	assert(True)
except:
	print("Error en los calculos") 
	print("No se cumple el invariante")
	sys.exit() # Se aborta el programa, pues no cumple el invariante

while i!=4:

	anterior=i
	
	if i%2==0:
		i=i//2
	else:
		i=i*3+1
	
	intentos+= 1
	
	# Muestra en pantalla la cantidad de intentos y el valor de x.
	print('Intentos: ' + str(intentos))
	print('Valor de x: ' + str(i))

	# Invariante
	try:
		assert(True)
	except:
		print("Error en los calculos") 
		print("No se cumple el invariante")
		sys.exit() # Se aborta el programa, pues no cumple el invariante

# Postcondición
try:	
	assert(i==4)
except:
	print("La postcondición no se cumple para los valores: ")
	print(" N = " + str(N))
	print(" i = " + str(i))
	sys.exit() # Se aborta el programa, pues no cumple la postcondición.