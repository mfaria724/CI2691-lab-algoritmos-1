#
# examenP2_1510463.py
#
# DESCRIPCION: Programa que calcula la cantidad de ascensos en una secuencia.
#
# Autor: Manuel Faria 15-10463
#
# Ultima modificacion: 27/02/2018
#

# VARIABLES:
#   numasc: int     // SALIDA: Valor que almacena el número de ascensos en la secuencia.
#	continuar: bool // Valor para determinar si se seguirán ingresando valores en la secuencia.
# 	anterior: int 	// Valor del elemento anterior de la secuencia para poder ser comparado.
#	i: int 			// Valor para verificar la cantidad de elementos de la secuencia.
# 	S: int 			// ENTRADA: Valor del elemento actal de la secuencia.

# Valores iniciales:
numasc,continuar,anterior,i=0,True,0,0

# Cota: N-i (Donde N es el máximo de elementos de la secuencia)
while continuar==True:

	S = int(input("Ingrese el siguiente elemento de la secuencia: "))

	# Precondición:
	if S==0:
		assert(i>1)
		continuar=False

	if anterior<S and anterior!=0:
		numasc+=1

	anterior=S

	i+=1

# Postcondición:
# No se puede revisar la postcondición porque no guardamos los valores anteriores en memoria
# y no podemos comparar los elementos nuevamente.

# Salida:
print("El número de ascensos es: ")
print(numasc)