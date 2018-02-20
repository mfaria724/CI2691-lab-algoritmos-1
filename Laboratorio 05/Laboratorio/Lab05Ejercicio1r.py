#
# Lab05Ejercicio1r.py
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
		while True:
			try:
				N = int(input("Indique el próximo número, si desea terminar ingrese 0: "))
				
				assert(N>0)
				break
			except: # Si es nula, reinicia el ciclo.
				print('Solo se admiten números no negativos')
				print('La secuencia no puede ser nula')
				print('Ingrese una nueva secuencia')

	elif cantidad==1: # Verificación de que no sea unitaria
		while True:
			try:
				N = int(input("Indique el próximo número, si desea terminar ingrese 0: "))
				
				assert(N>0)
				break
			except: # Si es unitaria, inicia el ciclo nuevamente.
				print('Solo se admiten números no negativos')
				print('La secuencia no puede ser unitaria')
				print('Ingrese una nueva secuencia')
				cantidad=-1
				cota=100
				break
	else:
		while True: # Ingresa todos los demás números y si son validos los compara.
			try:
				N = int(input("Indique el próximo número, si desea terminar ingrese 0: "))
				
				assert(N>=0)

				if N==0: # Si es cero sale del ciclo.
					break

				if anterior>=N:
					ordenado=False
				break
			except: # Vuelve a pedir un número hasta que ingrese uno válido.
				print('Solo se admiten números no negativos')

		if N==0: # Si es cero termina el programa.
			break	

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

# Salida:
if ordenado==True:
	print("La secuencia está ordenada de forma creciente")
else:
	print("La secuencia NO está ordenada de forma creciente")