#
# Lab04Ejercicio3.py
#
# DESCRIPCION: Programa que dados el nombre, edad, índice y nota de cuatro parciales
# de CI2611 de 25 ptos c/u y genera la nota total de cada estudiante, y el promedio,
# para cada parcial.
#
# Autor: 
#	Manuel Faria

# Variables:
# grupo: array[0,10) of Estudiante()// ENTRADA: Arreglo que contiene a todos los
#										estudiantes.
# edades: array[0,10) of int    	// ENTRADA: Arreglo de las edades.
# nombres: array[0,10) of string    // ENTRADA: Arreglo de los nombres. 
# indices: array[0,10) of float     // ENTRADA: Arreglo de los indices. 
# parciales: array[0,4)[0,10) of float   // ENTRADA: Matriz que contiene las notas
#										de todos los parciales para todos los estudiantes. 
# promedioIndice: float    			// SALIDA: Variable donde se almacena el 
#										promedio de los indices. 
# promedioEdad: float    			// SALIDA: Variable donde se almacena el
#										promedio de las edades. 
# promedios: array[0,4) of float    // SALIDA: Arreglo donde se almacenan los
#										promedios de los parciales.  
# sumaParciales: float    			// SALIDA: Variable donde se almacena la nota
#										sobre 100 de cada estudiante. 

# Valores Iniciales:
class Estudiante:
	edad = 0
	nombre = ""
	indice = 0.0
	nota1 = 0.0
	nota2 = 0.0
	nota3 = 0.0
	nota4 = 0.0
	notaFinal = 0

grupo = [ Estudiante() for x in range(10) ]
edades = [20,21,22,23,24,25,24,20,21,22]
nombres = ["Manuel",'Juan','Pedro','Maria','Valentina','Carolina','Samuel','Antonio', 'Valeria', 'Joaquin']
indices = [2.22,4.55,5,3.52,4.63,3.0000,3.0111,4.98,4.32,3.99]
parciales = [[24,23,25,21,2,2,4,6,8,24.5],[24,23,25,21,18,2,4,6,8,24.5],[24,23,25,21,18,2,4,6,8,24.5],[24,23,25,21,18,2,4,6,8,24.5]]
promedioIndice = 0.0
promedioEdad = 0.0
promedios=[0.0,0.0,0.0,0.0]

# Precondición:
assert(True)

# Calculos:
# Cota: 10 - i
# Invariante:
assert(True)

for x in range(10):
	# Guarda los datos personales.
	grupo[x].nombre = nombres[x]
	grupo[x].edad = edades[x]
	grupo[x].indice = indices[x]

	# Guarda las notas.
	grupo[x].nota1 = parciales[0][x] 
	grupo[x].nota2 = parciales[1][x] 
	grupo[x].nota3 = parciales[2][x] 
	grupo[x].nota4 = parciales[3][x] 

	#Calcula nota total sobre 100.
	sumaParciales = grupo[x].nota1 + grupo[x].nota2 + grupo[x].nota3 + grupo[x].nota4
	
	# Imprime valor de la nota sobre 5.
	if sumaParciales > 85:
		print("La nota de " + str(grupo[x].nombre) + " es 5.")
	elif sumaParciales < 85 and sumaParciales >=70:
		print("La nota de " + str(grupo[x].nombre) + " es 4.")
	elif sumaParciales < 70 and sumaParciales >=50:
		print("La nota de " + str(grupo[x].nombre) + " es 3.")
	elif sumaParciales < 50 and sumaParciales >=30:
		print("La nota de " + str(grupo[x].nombre) + " es 2.")
	elif sumaParciales < 30:
		print("La nota de " + str(grupo[x].nombre) + " es 1.")

	# Invariante:
	assert(True)

# Cota: 10-j
# Invariante: 
assert( promedios[0] >= 0 and promedios[1]>=0 and promedios[2]>=0 and promedios[3]>=0)
for j in range(10):

	# Suma el valor de todos los estudiantes al promedio.
	promedioEdad = promedioEdad + grupo[j].edad
	promedioIndice = promedioIndice + grupo[j].indice
	promedios[0] = promedios[0] + grupo[j].nota1
	promedios[1] = promedios[1] + grupo[j].nota2
	promedios[2] = promedios[2] + grupo[j].nota3
	promedios[3] = promedios[3] + grupo[j].nota4

	# Ivariante:
	assert( promedios[0] >= 0 and promedios[1]>=0 and promedios[2]>=0 and promedios[3]>=0)

promedioEdad = promedioEdad / 10
promedioIndice = promedioIndice / 10

# Cota: 10-z
# Invariante
assert(True)

for z in range(4):
	promedios[z] = promedios[z] / 10

	# Invariante:
	assert(True)

# Postcondición:
assert(promedios[0] == sum(grupo[i].nota1 for i in range(10)) / 10 and
	   promedios[1] == sum(grupo[i].nota2 for i in range(10)) / 10 and
	   promedios[2] == sum(grupo[i].nota3 for i in range(10)) / 10 and
	   promedios[3] == sum(grupo[i].nota4 for i in range(10)) / 10)

print("El promedio de edad del Grupo es:", promedioEdad)
print("El promedio de índice del Grupo es:", promedioIndice)

for j in range(4):
	print("El promedio del parcial " + str(j) + " es: " + str(promedios[j]))
