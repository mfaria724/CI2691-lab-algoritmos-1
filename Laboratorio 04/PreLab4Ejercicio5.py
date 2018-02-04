#
# PreLab4Ejercicio5.py
#
# DESCRIPCION: Programa que dado el un número de estudiantes lee la edad, nombre
# e índice acamdémico de cada uno y los almacena en un arreglo llamando "grupo".
# Finalmente calcula el promedio de edad e índice académcico del grupo.
#
# Autor: 
#	Manuel Faria

# Variables:
# M: array[0,3)[0,3)// ENTRADA: Matriz a ser evaluada.
# diagonal: bool    // SALIDA: Variable donde se almacenara si la matriz es 
# 							   diagonal o no.
# i: int 			// Valor que servira par iterar sobre una dimensión del arreglo.
# j: int 			// Valor que servira par iterar sobre otra dimensión del arreglo.

# Valores Iniciales:
class Estudiante:
	edad = 0
	nombre = ""
	indice = 0.0
N = int(input("Ingrese el número de estudiantes del grupo a evaluar: "))
grupo = [ Estudiante() for x in range(N) ]
promedioIndice = 0.0
promedioEdad = 0.0

# Precondición:
assert( N>0 )

# Calculos:
for i in range(N):
	grupo[i].edad = int(input("Ingrese la edad del estudiante " + str(i) + ": "))
	grupo[i].nombre = str(input("Ingrese el nombre del estudiante "+ str(i) + ': '))
	grupo[i].indice = float(input("Ingrese el índice académcico del estudiante " + str(i) + ': '))

	# Postcondicion:
	assert( grupo[i].edad > 0 and len(grupo[i].nombre) > 0  and 1<=grupo[i].indice<=5)

for j in range(N):
	promedioEdad = promedioEdad + grupo[j].edad 

promedioEdad = promedioEdad / N

for k in range(N):
	promedioIndice = promedioIndice + grupo[k].indice 

promedioIndice = promedioIndice / N

# Salida:

print("El promedio de edad del Grupo es:", promedioEdad)
print("El promedio de índice del Grupo es:", promedioIndice)