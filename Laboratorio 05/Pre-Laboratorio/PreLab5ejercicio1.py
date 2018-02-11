#
# Prelab5ejercicio1.py
#
# DESCRIPCION: Programa para calcular las raices del polinomio 
# AX^2 + BX + C.
#
# AUTOR: Manuel Faria
#
# Última modifiación: 11/02/2018
#
# Variables:
#    A: entero // ENTRADA: Primer coeficiente
#    B: entero // ENTRADA: Segundo coeficiente
#    C: entero // ENTRADA: Tercer coeficiente
#    x1: float // SALIDA: Primera raiz
#    x2: float // SALIDA: Segunda raiz

import sys # Se importa la libreria sys para poder utilizar sys.exit()

# Valores iniciales:
x1 = 0.0
x2 = 0.0

# Verificación de la Precondición:
while True: # Se permite que el usuario pueda introducir nuevos datos.
	try:
		# Precondicion:
		A = int(input("Indique el primer coeficiente: "))
		B = int(input("Indique el segundo coeficiente: "))
		C = int(input("Indique el tercer coeficiente: "))
		assert(A != 0 and 4 * A * C <= B * B)
		break
	except:
		print("Error en los datos, debe volver a introducirlos")
		print("El valor del coeficiente de término cuadrático no puede ser 0 y el discriminante debe ser positivo")

# Calculos:
x1 = (-B + (B*B - 4*A*C)**0.5) / (2*A)
x2 = (-B - (B*B - 4*A*C)**0.5) / (2*A)

# Postcondicion:
try:
	assert(
	    (A * x1 * x1 + B * x1 + C == 0.0) and
	    (A * x2 * x2 + B * x2 + C == 0.0)
	)
except:
	print("Error en los calculos") 
	print("No se cumple la postcondicion con los valores ")
	print("  A = " + str(A))
	print("  B = " + str(B))
	print("  C = " + str(C))
	print("  x1 = " + str(x1))
	print("  x2 = " + str(x2))
	sys.exit() # Se aborta el programa, pues no cumple la postcondicion

# Salida:
print("Las raices son: ", x1, " y ", x2)