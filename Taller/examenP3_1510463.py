#
# examenP3_1510463.py
#
# DESCRIPCION: Programa que lee determinados valores de los paises participantes en 
# las olimpiadas de invierno, y retorna el pais con la maxima cantidad de medallas
# y el número total de medallas de oro, plata y bronce.
#
# Autor: Manuel Faria 15-10463
#
# Ultima modificacion: 27/02/2018
#

# CONSTANTES:
# 	MAX: int // Número máximo de países.
# VARIABLES:
#	totaloro: int // Número total de medallas de oro.
#	totalpla: int // Número total de medallas de plata.
#	totalbro: int // Número total de medallas de bronce.
#	k: int 		  // Variable para iterar en el ciclo.
# 	Paises: array [0,MAX)x[0,MAX) of Pais() // Arreglo que almacena los atributos de cada país.

# Definicion de la clase País
class Pais:
  nombre = ""
  numatl = 0
  numoro = 0
  numpla = 0
  numbro = 0

# Valores iniciales
MAX=2
totaloro=0
totalpla=0
totalbro=0
k=0

Paises = [Pais() for x in range(0,MAX)]

# Precondición:
assert(MAX>0)

while True:
	try:
		# Cota: MAX-k
		for k in range(0,MAX):
			Paises[k].nombre = str(input("Ingrese el nombre del país: "))
			Paises[k].numatl = int(input("Ingrese el número de atletas participantes: "))
			Paises[k].numoro = int(input("Ingrese el número de medallas de oro: "))
			Paises[k].numpla = int(input("Ingrese el número de medallas de plata: "))
			Paises[k].numbro = int(input("Ingrese el número de medallas de bronce: "))

			# Si no hay valores anteriores, asgina los valores del primer país.
			if k==0:
				masMedallas=Paises[k].nombre
				masMedallasOro=Paises[k].numoro
				masMedallasPla=Paises[k].numpla
				masMedallasBro=Paises[k].numbro
			else:
				if (Paises[k-1].numoro + Paises[k-1].numpla + Paises[k-1].numbro) <= (Paises[k].numoro + Paises[k].numpla + Paises[k].numbro):
					masMedallas=Paises[k].nombre
					masMedallasOro=Paises[k].numoro
					masMedallasPla=Paises[k].numpla
					masMedallasBro=Paises[k].numbro

			totaloro+=Paises[k].numoro
			totalpla+=Paises[k].numpla
			totalbro+=Paises[k].numbro

		break

	except:
		print("El nombre debe ser de tipo string.")
		print("El número de atletas participantes debe ser de tipo entero.")
		print("El número de medallas de oro debe ser de tipo entero.")
		print("El número de medallas de plata debe ser de tipo entero.")
		print("El número de medallas de bronce debe ser de tipo entero.")

# Postcondición:
assert(totaloro==sum(Paises[x].numoro for x in range(0,MAX)) and totalpla==sum(Paises[x].numpla for x in range(0,MAX))
	and totalbro==sum(Paises[x].numbro for x in range(0,MAX)) and max (Paises[x].numoro for x in range(0,MAX)) == masMedallasOro
	and max (Paises[x].numpla for x in range(0,MAX)) == masMedallasPla and max (Paises[x].numbro for x in range(0,MAX)) == masMedallasBro)

print("PAIS CON MAXIMO NUMERO DE MEDALLAS: " + str(masMedallas))
print("ORO = " + str(masMedallasOro) + " PLATA = " + str(masMedallasPla) + " BRONCE = " + str(masMedallasBro))

print("TOTAL DE MEDALLAS OTORGADAS: ")
print("ORO = " + str(totaloro) + " PLATA = " + str(totaloro) + " BRONCE = " + str(totaloro))