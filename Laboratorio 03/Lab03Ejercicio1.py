#
# Lab03Ejercicio1.py
#
# DESCRIPCION: Programa que presenta un menú con 3 opciones: 
#   1. Superficie de una habitacion: Se solicita el largo y ancho de una
#      habitación y muestra la superficie de la habitación con 4 decimales.
#   2. Área de una circunferencia: Se solicita el radio de la circunferencia
#      y muestra el el área de la misma.
#   3. Suma de cuadrados: Se solicita un número n y se muestra la sumatoria de 
#      todos los cuadrados entre 1 y n.
#
# Autor: 
#	Manuel Faria

# Variables:
# menu: int 		// ENTRADA: Variable que almacena el número del 
#								programa que se desea ejecutar.
# largo: flotante   // ENTRADA: Largo de la habitación.
# ancho: flotante   // ENTRADA: Ancho de la habitación. 
# radio: flotante   // ENTRADA: Radio de la cincunferencia.
# n: int 			// ENTRADA: Cota superior de la función 3 del programa.
# i: int 			// Iterador que servirá para salir del do.

# superficie: flotante // SALIDA: Variable que almacena el valor de la 
#								  superficie de una habitación cuando se
#								  ejecuta la opción 1 del programa.
# area: flotante	   // SALIDA: Variable que almacena el valor del area 
#								  de la circunferencia cuando se
#								  ejecuta la opción 2 del programa.
# suma: flotante	   // SALIDA: Variable que almacena el valor de la 
#								  suma de los cuadrados entre 1 y n cuando se
#								  ejecuta la opción 3 del programa.

# Valores Iniciales:
i=0
cota=3-i

# Calculos:
# Invariante y cota:
assert( 0<=i<=3 )
assert( cota>=0 )

while 3 > i:
	print("Para calcular la superficie de una habitación, ingrese 1.")
	print("Para calcular el área de una circunferencia, ingrese 2.")
	print("Para calcular la suma de los cuadrados entre 1 y un valor, ingrese 3.")
	menu = int(input("Ingrese el valor(1,2 ó 3): "))

	if menu==1:

		# Valores Iniciales:
		largo = float(input("Ingrese el largo de la habitación: "))
		ancho = float(input("Ingrese el ancho de la habitación: "))

		# Precondición:
		assert(largo>0 and ancho>0)

		# Calculos:
		superficie=round(largo*ancho,4)

		# Postcondición:
		assert(superficie==round(largo*ancho,4))

		# Salida:
		print("La superficie de la habitación es:", superficie)

	elif menu==2:

		# Valores Iniciales:
		radio = float(input("Ingrese el radio de la circunferencia: "))

		# Precondición:
		assert(radio>0)

		# Calculos:
		area=3.1416*(radio**2)

		# Postcondición:
		assert(area==3.1416*(radio**2))

		# Salida:
		print("El área de la circunferencia es:", area)

	elif menu==3:

		# Valores Iniciales:
		n = int(input("Ingrese el valor de n: "))

		# Precondición:
		assert(n>0)

		# Calculos:
		suma = sum (i**2 for i in range(1,n+1))

		# Postcondición:
		assert(suma == sum (i**2 for i in range(1,n+1)))

		# Salida:
		print("La suma de los cuardados entre 1 y",n,"es:", suma)

	i=i+1

	#Verifica el invariante y modifica la cota.
	assert( 0<=i<=3 )
	cota=3-i


# Postcondicion:
assert( 0<=i<=3 )