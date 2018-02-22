#
# Lab05Ejercicio1c.py
#
# DESCRIPCION: Programa que dada una secuencia de enteros no negativos 
# provista por el usuario, verifica si dicha secuencia está ordenada.
#
# Autor: 
#	Manuel Faria 15-10463
#
# Ultima modificacion: 20/02/2018
#

import sys    # Se importa la libreria sys para poder utilizar sys.exit()

# CONSTANTES:
#	maximo: int // Número máximo de elementos de la secuencia.

# VARIABLES:
#	cantidad: int   // Cantidad de elementos de la secuencia.
#	ordenado: bool  // SALIDA: Valor que almacena si la secuencia está ordenada crecientemente. 
#	anterior: int 	// ENTRADA: Valor que almacena el último elemento de la secuencia. 
#	N: int 			// ENTRADA: Valor del elemento de la secuencia que ingresa el usuario.

# Valores iniciales:
cantidad,ordenado,anterior,N,maximo=0,True,0,1,100
cota = maximo-cantidad

# Invariante
try:
	assert(0<=cantidad<=maximo)
except:
	print("Error en los calculos") 
	print("No se cumple el invariante con los valores: ")
	print("  cantidad = " + str(cantidad))
	print("  maximo = " + str(maximo))
	sys.exit() # Se aborta el programa, pues no cumple el invariante

# Cota acotada por cero
try:
	assert(maximo-cantidad>=0)
except:
	print("Error en los calculos") 
	print("No se cumple la cota estrictamente decreciente con los valores: ")
	print("  cantidad = " + str(cantidad))
	print("  maximo = " + str(maximo))
	print("  cota = " + str(cota))
	sys.exit() # Se aborta el programa, pues no cumple la condición de cota estrictamente decreciente.


while (cantidad<100):
	if cantidad==0: # Verificación de que no sea nulo
		try:
			N = int(input("Indique el próximo número, si desea terminar ingrese 0: "))
			assert(N>0)
		except: # Si es nula, reinicia el ciclo.
			print('Solo se admiten números no negativos')
			print('La secuencia no puede ser nula')
			sys.exit() # Se aborta el programa, pues no cumple la condición.

	elif cantidad==1: # Verificación de que no sea unitaria
		try:
			N = int(input("Indique el próximo número, si desea terminar ingrese 0: "))
			
			assert(N>0)
		except: # Si es unitaria, inicia el ciclo nuevamente.
			print('Solo se admiten números no negativos')
			print('La secuencia no puede ser unitaria')
			sys.exit() # Se aborta el programa, pues no cumple la condición.

	else:
			try:
				N = int(input("Indique el próximo número, si desea terminar ingrese 0: "))
				
				assert(N>=0)
				
				if anterior>=N:
					ordenado=False

				if N==0: # Si es cero sale del ciclo.
					break

			except: # Vuelve a pedir un número hasta que ingrese uno válido.
				print('Solo se admiten números no negativos')
				sys.exit() # Se aborta el programa, pues no cumple la condición.


	cantidad+=1
	anterior=N

	# Invariante
	try:
		assert(0<=cantidad<=maximo)
	except:
		print("Error en los calculos") 
		print("No se cumple el invariante con los valores: ")
		print("  cantidad = " + str(cantidad))
		print("  maximo = " + str(maximo))
		sys.exit() # Se aborta el programa, pues no cumple el invariante

	# Cota estrictamente decreciente
	try:
		assert(cota>=maximo-cantidad)
	except:
		print("Error en los calculos") 
		print("No se cumple la cota con los valores: ")
		print("  cantidad = " + str(cantidad))
		print("  maximo = " + str(maximo))
		print("  cota = " + str(cota))
		sys.exit() # Se aborta el programa, pues no cumple el invariante
	
	# Actualiza el valor de la cota
	cota= maximo-cantidad

	# Cota acotada por cero
	try:
		assert(maximo-cantidad>=0)
	except:
		print("Error en los calculos") 
		print("No se cumple la cota estrictamente decreciente con los valores: ")
		print("  cantidad = " + str(cantidad))
		print("  maximo = " + str(maximo))
		print("  cota = " + str(cota))
		sys.exit() # Se aborta el programa, pues no cumple la condición de cota estrictamente decreciente.

# Postcondición:
try:
	assert(True)
except:
	print("La postcondición no se cumple") 

# Salida:
if ordenado==True:
	print("La secuencia está ordenada de forma creciente")
else:
	print("La secuencia NO está ordenada de forma creciente")