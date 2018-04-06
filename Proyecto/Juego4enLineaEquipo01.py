 #   Juego4enLineaEquipo01.py

#   DESCRIPCIÓN: Juego realizado en gcl para luego ser implementado de python.
#   La finalidad es que los jugadores logren colocar 4 fichas de manera consecutiva,
#   en cualquiera de las posiciones vertical, horizontal o diagonal. Al momento de
#   seleccionar la jugada el jugador deberá seleccionar una columna, puesto que no 
#   podrá jugar en una casilla a menos que se encuentre en la fila inferior, o que
#   en la fila de abajo se encuentre alguna fichas.

#   El juego tendrá dos niveles de dificultad, básico e intermedio.

#   	1. En la dificultad básica la computadora hará jugadas aleatorias hasta que la
#   	   la partida se acabe.

#   	2. En la dificultad intermedia la computadora intentará generar una linea usando,
#   	   alguna de las estrategias, que es seleccionada cada vez que la computadora se 
#   	   ve obligada a realizar una jugada aleatoria.

#   Al finalizar cada partida se muestran los resultados en la pantalla, es decir, el 
#   ganador de la partida que acaba de terminar.

#   Finalmente, se consulta con el usuario si desea jugar otra partida, en caso de 
#   que no lo desee, se muestran en pantalla la cantidad de partidas ganadas por la
#   persona, por el computador y la cantidad de empates. De igual manera se muestra
#   la cantidad de partidas realizadas.

#   Autores: 
#  	  Manuel Faria 15-10463
#  	  Juan Oropeza 15-11041


#	DECLARACIÓN DE VARIABLES
# 
# 	CONST
# 		filas:int;										// Numero de filas del tablero
# 		columnas: int;									// Numero de columnas del table
# 		maxPartidas: int;								// Numero maximo de partidas a jugar
#		NEGRO: list;									// Color utilizado en la parte grafica del programa	
#		BLANCO: list;									// Color utilizado en la parte grafica del programa
#		ROJO: list;										// Color utilizado en la parte grafica del programa
#		AZUL: list;										// Color utilizado en la parte grafica del programa
#		AMARILLO: list;									// Color utilizado en la parte grafica del programa
#		ALTO: int          							    // Alto de la ventana
#		ANCHO: int    							        // Ancho de la ventana
#
# 	VAR
# 		tablero: list [0,filas) x [0,columnas) of int;	// Matriz del tablero de juego
# 		dificultad: int;								// Variable que almacena la dificultad seleccionada por el jugador (0 basico, 1 medio)
# 		ultimoGanador: int;								// Variable que almacena el ganador de la partida anterior
# 		jugador: int;									// Variable que almacena el jugador del turno actual
# 		numPartidas: int;								// Variable que almacena la cantidad de partidas jugadas
# 		jugada: int;									// Variable que almacena la columna donde se desea jugar
# 		ultimaJugada: list;								// Variable que almacena la fila y columna de la ultima jugada de la computadora
# 		continuar: bool;								// Variable que determina si una partida ha finalizado o no
# 		numJugadas: int;								// Variable que almacena el numero de jugadas de la partida actual
# 		numJugadasPC: int;								// Variable que almacena el numero de jugadas de la computadora en la partida actual
# 		numEmpates: int;								// Variable que almacena el numero de empates de todos los juegos
# 		partidasGanadasPersona: int;					// Variable que almacena la cantidad de veces que ha ganado el jugador
# 		partidasGanadasPC: int;							// Variable que almacena la cantidad de veces que ha ganado la computadora
# 		ganador: int;									// Variable que almacena el ganador de la partida actual
# 		validacion: bool;								// Variable que determina si una jugada es valida o no
# 		quiereSeguirJugando: bool;						// Variable que determina si el usuario desea jugar otra partia o no
# 		ingresaJugada: bool;							// Variable utilizada en el ciclo de cada jugada para en caso de no ser valida, poder ingresar otra jugada
#		nombre: str;									// Variable que almacena el nombre del jugador
#		estrategia: int;								// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media

# Se importa la librería random para generar las jugadas aleatorias.
import random
# Se importa la libreria pygame para generar la grafica del juego.
import pygame
# Se importa la libreria sys para realizar una programacion robusta, y poder finalizar el programa
import sys

def seguirPartida(nombre: str) -> bool:

	# Precondición: 
	assert(True)

	# Pregunta al jugador si desea continuar con la partida actual o no.

	# VAR
	#	confirmacion: int;				// Variable que almacena la respuesta del jugador
	#	validacion: bool;				// Variable que retornara la funcion, dependiendo de la respuesta del jugador
	#	nombre: str;					// Variable que almacena el nombre del jugador

	# Le pregunta al usuario si quiere seguir con la partida.
	# print("Le pregunta al usuario si quiere seguir con la partida.")

	while True:
		try:
			confirmacion = int(input("Por favor " + nombre +", ingrese 1 si desea continuar con la partida, en caso contrario ingrese 0: "))

			assert(0 <= confirmacion <= 1)

			if confirmacion == 1: 
				validacion = True
			elif confirmacion == 0:
				validacion = False

			break
		except:
			print("Por favor " + nombre +", ingrese una opción válida.")
	
	# Postcondición: 
	assert((confirmacion == 1 and validacion == True) or (confirmacion == 0 and validacion == False))

	return validacion

def entregaResultados(partidasGanadasPersona: int, partidasGanadasPC: int, numEmpates: int, nombre: str) -> 'void':
	# Precondición: 
	assert(partidasGanadasPersona >= 0 and partidasGanadasPC >= 0 and numEmpates >= 0)

	# Imprime la cantidad de partidas ganadas por el jugador, PC y el numero de empates

	# VAR
	# 	partidasGanadasPersona: int; 				// Variable que almacena el numero de partidas ganadas por el jugador
	# 	partidasGanadasPC: int; 					// Variable que almancena el numero de partidas ganadas por la computadora
	# 	numEmpates: int; 							// Variable que almacena el numero de empates

	# print("Se imprime la cantidad de partidas ganadas por el Jugador, PC y numero de empates")

	print("Número de partidas ganadas por " + nombre+ ": " + str(partidasGanadasPersona))
	print("Número de partidas ganadas por la computadora: " + str(partidasGanadasPC))
	print("Número de empates: " + str(numEmpates))

	# Postcondición: 
	# Se imprime la cantidad de partidas ganadas por el Jugador, PC y numero de empates
	assert(True)

def entregaGanadorPartida(ganador: int, nombre: str) -> 'void':
	# Precondición: 
	assert(0 <= ganador <= 2)

	# Entrega los resultados de la partida que acaba de finalizar
	
	# VAR
	# 	ganador: int;								// Variable que almacena el ganador de la partida actual
	#	nombre: str; 								// Variable que almacena el nombre del jugador

	# print("Entrega los resultados de la partida que acaba de finalizar")

	if ganador == 1:
		print(nombre+ " ha ganado la partida.")
	elif ganador == 2:
		print("La computadora ha ganado la partida.")
	else:
		print("Empate")
	
	# Postcondición: 
	# Se imprime el ganador de la partida
	assert(True)

def quiereSeguir(nombre: str) -> bool:
	# Precondición: 
	assert(True)

	# Le pregunta al jugador si desea jugar otra partida cuando ha finalizado una.

	# VAR
	# 	confirmacion: int; 						// Variable que almacena la respuesta del jugador
	# 	validacion: bool; 						// Varibale que retorna la funcion, dependiendo de la respuesta del jugador

	# print("El jugador ingresa si desea jugar otra partida")

	while True:
		try:
			confirmacion = int(input("Por favor " + nombre +", ingrese 1 si desea jugar otra partida, en caso contrario ingrese 0: "))

			assert(0 <= confirmacion <= 1)

			if confirmacion == 1:
				validacion = True
			elif confirmacion == 0:
				validacion = False

			break
		except:
			print("Por favor " + nombre +", ingrese una opción válida.")

	
	# Postcondición: 
	assert((confirmacion == 1 and validacion == True) or (confirmacion == 0 and validacion == False))

	return validacion

def inicializarPartida(numPartidas: int, ultimoGanador: int, filas: int, columnas: int,tablero: list, BLANCO: list, NEGRO: list, nombre: str, partidasGanadasPersona: int, partidasGanadasPC: int) -> (int, int, int, int, str) :
	# Precondición: 
	assert(numPartidas >= 0 and 0 <= ultimoGanador <= 2 and filas >= 0 and columnas >= 0)

	# Inicializa el tablero y los valores necesarios para poder jugar

	# VAR
	# 	numPartidas: int; 						// Variable que almacena la cantidad de partidas jugadas
	# 	ultimoGanador: int; 					// Variable que almacena el ganador de la partida anterior
	# 	filas: int;								// Numero de filas del tablero
	# 	columnas: int;							// Numero de columnas del tablero
	# 	tablero: list;							// Matriz del tablero de juego
	# 	BLANCO: list;							// Color utilizado en la parte grafica del programa
	# 	NEGRO: list;							// Color utilizado en la parte grafica del progama
	# 	nombre: str;							// Variable que almacena el nombre del jugador
	# 	jugador: int;							// Variables que almacena el jugador del turno actual
	# 	dificultad: int;						// Variable que almacena la dificultad seleccionada por el jugador

	# print("Inicializa el tablero y los valores necesarios para poder jugar")

	inicializarTablero(filas, columnas, tablero)
	if numPartidas == 0:	# Si es la primera partida, pide al jugador su nombre
		nombre = pedirNombre()
	dibujarTablero(BLANCO, NEGRO, nombre, partidasGanadasPersona, partidasGanadasPC, numEmpates)
	dificultad = escogerDificultad(nombre)
	jugador = definirPrimero(numPartidas, ultimoGanador)

	# Inicializa las variables para la partida
	numJugadas = 0
	numJugadasPC = 0
	ultimaJugada = [-1,-1]

	# Postcondición: 
	assert(all ( all (tablero[i][j] == 0 for i in range(filas)) for j in range(columnas)) and 0 <= dificultad <= 1 and 
		(numPartidas != 0 or jugador == 1) and (numPartidas == 0 or jugador == ultimoGanador))

	return dificultad, jugador, numJugadas, numJugadasPC, nombre

def inicializarTablero(filas: int,columnas: int,tablero: list) -> 'void':

	# Precondición: 
	assert(filas >= 4 and columnas >= 4)

	# print("Inicializa el tablero de manera que esté vacío")

	# Inicializa el tablero de manera que esté vacío

	# VAR
	# 	filas: int;								// Numero de filas del tablero
	# 	columnas: int;							// Numero de columnas del tablero
	# 	tablero: list;							// Matriz del tablero de juego
	# 	i: int;									// Variable auxiliar para iterar
	# 	j: int;									// Variable auxiliar para iterar
	#	cota1: int;								// Variable que permite finalizar la iteracion externa
	#	cota2: int;								// Varibale que permite finalizar la segunda interna

	# Inicialización de variables
	i = 0

	# Recorre las filas
	# Cota T:
	# Verificación de cota acotada por 0.
	cota1 = filas - i
	assert(cota1 >= 0)
	while i != filas:

		# Inicialización de variables
		j = 0

		# Recorre las columnas
		# Cota t2:
		# Verificación de cota acotada por 0.
		cota2 = columnas - j
		assert(cota2 >= 0)
		while j != columnas:

			# Rellena el tablero con 0's
			tablero[i][j] = 0

			j = j + 1

			# Cota estrictamente decreciente
			assert(cota2 > columnas - j)

			# Cambio de valor de la cota
			cota2 = columnas - j

			# Verificación de cota acotada por 0.
			assert(cota2 >= 0)


		i = i + 1

		# Cota estrictamente decreciente
		assert(cota1 > filas - i)

		# Cambio de valor de la cota
		cota1 = filas - i

		# Verificación de cota acotada por 0.
		assert(cota1 >= 0)


	# Postcondición: 
	assert(all ( all (tablero[i][j] == 0 for i in range(filas)) for j in range(columnas)))

def escogerDificultad(nombre: str) -> (int):
	# Se le solicita al usuario que ingrese la dificultad de la partida que va a jugar. Siendo 0 para básico y 1 para medio.

	# print("Se solicita al usuario que ingrese una dificultad hasta que ingrese una correctamente.")

	# Precondición: 
	assert(True)
	
	# VAR
	# 	nombre: str;								// Variable que almacena el nombre del jugador
	# 	dificulat: int;								// Variable que almacena la dificultad seleccionada por el jugador	

	while True:
		try:
			dificultad = int(input("Por favor " + nombre +", ingresa el tipo de dificultad que deseas para esta partida. 0 para básico, 1 para medio: "))
			
			# Postcondición:
			assert(0 <= dificultad <= 1)
			break

		except:
			# En caso de error le solicita al usuario que ingrese otro valor:
			print("Por favor " + nombre +", verifique que la dificultad que escogió sea un entero entre 0 y 1.")
			print("Por favor " + nombre +", ingrese la dificultad de la partida de nuevo.")

	# Postcondición:
	assert(0 <= dificultad <= 1)

	return dificultad

def definirPrimero(numPartidas: int, ultimoGanador: int) -> (int):
	# Precondición: 
	assert(numPartidas >= 0 and 0 <= ultimoGanador <= 2)

	# Función que devuelve el primer jugador dependiendo de la partida en que se encuentren.
	# print("Función que devuelve el primer jugador dependiendo de la partida en que se encuentren.")

	# VAR 
	# 	primerJugador: int;							// Variable que almacena quien sera el primer jugador de cada partida
	#	numPartidas: int; 							// Variable que almacena la cantidad de partidas jugadas
	#	ultimoGanador: int;							// Variable que almacena el ganador de la partida anterior

	if numPartidas == 0:	# Si es la primera partida, comienza el jugador, en caso contrario comienza el jugador que haya ganado la anterior
		primerJugador = 1
	else:
		primerJugador = ultimoGanador

	# Postcondición: 
	assert((numPartidas != 0 or primerJugador == 1) and (numPartidas == 0 or primerJugador == ultimoGanador))

	return primerJugador

def obtenerJugada(filas: int, columnas: int, numJugadasPC: int, tablero: int, ultimaJugada: list, jugador: int, dificultad: int, estrategia: int, nombre: str) -> (int, int):
	
	# Precondición: 
	assert(columnas >= 4 and 1 <= jugador <= 2 and 0 <= dificultad <= 1)

	# VAR
	#	filas: int;									// Numero de filas del tablero
	#	columnas: int;								// Numero de columnas del tablero
	#	numJugadasPC: int;							// Variable que almacena el numero de jugadas realizas por la computadora en la partida actual
	#	tablero: list;								// Matriz del tablero de juego
	#	ultimaJugada: list;							// Variable que almacena la fila y columna de la ultima jugada de la computadora
	#	jugador: int;								// Variable que almacena el jugador del turno actual
	#	dificultad: int;							// Variable que almacena la dificultad seleccionada por el jugador
	#	estrategia: int;							// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media
	#	jugada: int;								// Variable que almacena la columna donde se desea jugar
	#	nombre: str;								// Variable que almacena el nombre del jugador
	#	tranca: 
	
	# Devuelve la columna donde se desea jugar

	tranca = False
	if jugador == 2: # Verifica quien debe ingresar la jugada y la obtiene
			# Verifica la dificultad
		if dificultad == 0:
			# Jugada aleatoria
			jugada = randomJugadaPC(columnas)
		
		elif dificultad == 1:
			# Busca una jugada con una estrategia
			jugada, estrategia, tranca = jugadaPC(filas, columnas, numJugadasPC, tablero, ultimaJugada, estrategia)
	
	elif jugador == 1: # Turno del jugador
		jugada = jugadaPersona(columnas, nombre)

	# Postcondición: 
	assert(0 <= jugada <= columnas)
	
	return jugada, estrategia, tranca

def jugadaPersona(columnas: int, nombre: str) -> int:
	# VAR:
	#	columnas: int; 								// Número de columnas del tablero, la jugada no puede estar fuera del rango [0,columnas).
	#	jugada: int;								// Variable que almacena la columna donde se desea jugar
	#	nombre: str;								// Variable que almacena el nombre del jugador

	# print("Solicita entrada de una jugada válida a la persona hasta que se introduzca una correctamente.")
	#	Solicita entrada de una jugada válida a la persona hasta que se introduzca una correctamente.

	# Precondición:
	assert(columnas > 4)

	while True:
		try:
			jugada = int(input("Por favor "+nombre+", ingresa el número de la columna donde desea jugar: "))
			
			# Postcondición:
			assert(0 <= jugada < columnas)

			break
		except:
			# En caso de error le solicita al usuario que ingrese otro valor:
			print("Por favor " + nombre +", verifique que la columna donde desea jugar sea un entero entre 0 y " + str(columnas - 1) + ".")
			print("Por favor " + nombre +", ingrese el número donde desea jugar de nuevo.")

	return jugada


def validarJugada(jugada: int, filas: int, columnas: int, tablero: list) -> bool:
	# Precondición: 
	assert(0 <= jugada < columnas and filas >= 4 and columnas >= 4)

	# Verifica si una jugada es posible o no
	# print("Valida que la jugada sea válida")

	# VAR		
	# 	i: int;										// Variable auxiliar para iterar
	#	jugada: int;								// Variable que almacena la columna donde se desea jugar
	#	filas: int;									// Numero de filas del tablero
	#	columnas: int;								// Numero de columnas del tablero
	#	tablero: int;								// Matriz del tablero de juego
	#	validacio: int;								// Variable que determina si la jugada se puede realizar o no

	i = filas - 1

	validacion = False
	
	# Cota:
	cota = i + 1
	assert(cota >= 0)

	while i != -1:	# El ciclo var recorriendo las filas en la columna de la jugada deseada en busca de algun cero que verifique que se puede jugar
		if tablero[i][jugada] == 0:
			validacion = True	# Si alguna casilla es igual a cero la validacion se hace postiva

		i = i - 1

		# Verificacion de cota estrictamente decreciente.
		assert(cota > i)

		cota = i + 1

		# Verificacion de cota acotada por 0.
		assert(cota >= 0)

	# Postcondición: 
	assert(any (tablero[i][jugada] == 0 for i in range(filas)) == validacion)

	return validacion

def reflejarJugada(jugada: int, jugador: int, filas: int, columnas:int, tablero: list, ultimaJugada: list, numJugadasPC: int, tranca: bool) -> (int, int):
	# Precondición: 
	assert(1 <= jugador <= 2 and 0 <= jugada < columnas and filas >= 4 and columnas >= 4)

	# Guarda una jugada en el tablero
	print("Guarda la jugada en el tablero")

	# VAR
	# 	i: int;										// Variable auxiliar para iterar
	#	continua: boolean;							// Variable auxiliar para finalizar el ciclo y evitar seguir modificando el tablero
	#	jugada: int;								// Variable que almacena la columna donde se desea jugar
	#	jugador: int;								// Variable que almacena el jugador del turno actual
	#	filas: int;									// Numero de filas del tablero
	#	columnas: int;								// Numero de columnas del tablero
	#	tablero: list;								// Matriz del tablero de juego
	#	ultimaJugada: list:							// Variable que almacena la fila y la columna de la ultima jugada de la computadora
	#	numJugadasPC: int;							// Variable que almacena el numero de jugadas realizadas por la computadora
	#	cota: int;									// Variable que permite finalizar el ciclo

	i = filas - 1
	continua = True

	# Cota:
	cota = i + 1
	assert(cota >= 0)

	while i != -1 and continua == True: # El ciclo va recorriendo el las filas de abajo hacia arriba en la columna a jugar.
		if tablero[i][jugada] == 0:		# Al encontrarse con la primera casilla con cero, asigna en esta el numero del jugador correspondiente
			tablero[i][jugada] = jugador
			if jugador == 2:
				numJugadasPC = numJugadasPC + 1
				dibujarJugada(i, jugada, AZUL)
				if tranca == False:
					ultimaJugada = [i,jugada] # Se asigna como ultima jugada la jugada que acabade realizarse
			else:
				dibujarJugada(i, jugada, ROJO)
			continua = False 	# Cambia la variable continuar para evitar seguir modificando la matriz
			pygame.display.flip()	# Se actualiza el tablero
				
		i = i - 1

		# Verificacion de cota estrictamente decreciente.
		assert(cota >= i + 1)

		cota = i + 1

		# Verificacion de cota acotada por 0.
		assert(cota >= 0)

	# Postcondición: 
	assert(any (tablero[i][jugada] == jugador for i in range(filas)))

	return ultimaJugada, numJugadasPC

def cambiarTurno(jugador: int) -> int:
	# Precondición:
	assert(1 <= jugador <= 2)

	# Pasa el turno al siguiente jugador
	# print("Pasa el turno al siguiente jugador")

	# VAR
	#	jugador: int;									// Variable que almacena el jugador del turno actual

	if jugador == 1:
		jugador = 2
	elif jugador == 2:
		jugador = 1

	# Postcondición: 
	assert(jugador == 1 or jugador == 2)

	return jugador

def verificar4enLinea(filas: int, columnas: int, tablero: list) -> (int, int):
	# Precondicion: 
	assert(filas >= 4 and columnas >= 4 and 
			all ( all (0 <= tablero[i][j] <= 2 for j in range(columnas)) for i in range(filas)))

	# Verifica si alguno de los jugadores realizó un 4 en línea
	# print("Verifica si alguno de los jugadores realizó un 4 en línea")
	
	# VAR
	# 	ganadores: array[0,4) of int;							// Arreglo utilizado para verificar si se cumple alguna de las verificaciones de 4 en linea
	# 	i: int;													// Variable auxiliar para iterar
	#	filas: int;												// Numero de filas del tablero
	#	columans: int;											// Numero de columnas del tablero
	#	tablero: int;											// Matriz del tablero de juego
	#	continuar: bool;										// Variable que determina si una partida ha finalizado o no
	#	ganador: int; 											// Variable donde se almacena el jugador que realizo el 4 en linea

	continuar = True
	ganador = 0
	ganadores = [verificarHorizontal(filas, columnas, tablero), verificarVertical(filas, columnas, tablero), verificarDiagonalDerecha(filas, columnas, tablero), verificarDiagonalIzquierda(filas, columnas, tablero)]

	i = 0

	# Cota 
	cota = 4 - i
	# Verificacion de cota acotada por 0.
	assert(cota >= 0)

	while i != 4:	# El ciclo reccore el arreglo ganadores, donde se almacena si algun jugador logro realizar un 4 en linea
		if ganadores[i] != 0:
			ganador = ganadores[i] # En caso de conseguir una casilla que sea distinto de cero, asigna a ganador el jugador que realizo el 4 en linea
			continuar = False 	# Se cambia el valor de continar para confirmar que la partida ha finalizador, ya que ha ganado algun jugador
		i = i + 1

		# Verificacion de cota estrictamente decreciente
		assert(cota > 4 - i)

		# Actualiza valor de la cota
		cota = 4 - i

		# Verificacion de cota acotada por 0.
		assert(cota >= 0)

	# Postcondición: 
	assert(any (ganadores[i] != 0 and ganador == ganadores[i] for i in range(4)) == (continuar == False))

	return continuar, ganador

def verificarHorizontal(filas: int, columnas:int, tablero: list) -> int:
	# Precondición: 
	assert(filas >= 4 and columnas >= 4 and 
			 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si existe una linea horizontal
	# print("Verifica si existe una linea horizontal")

	# VAR
	# 	i: int;													// Variable auxiliar para iterar
	# 	j: int;													// Variable auxiliar para iterar
	# 	hay4enLinea: boolean;									// Variable que determina si hay 4 en linea
	# 	ganador: int;											// Variable que al almacena el ganador de la partida actual, (en caso de ser distinto de 0)
	#	filas: int;												// Numero de filas del tablero
	#	columnas: int;											// Numero de columnas del tablero
	#	tablero: list;											// Matriz del tablero de juego
	#	cota1: int;												// Variable que permite finalizar la iteracion exterior
	#	cota2: int;												// Varible que permite finalizar la iteracion interior

	i = 0
	hay4enLinea = False
	ganador = 0
	# Cota1:
	cota1 = filas - i
	# Verificacion de cota acotada por 0.
	assert(cota1 >= 0)

	while i != filas:
	
		j = 0

		# Cota2:
		cota2 = columnas - 3 - j
		# Verificacion de cota acotada por 0.
		assert(cota2 >= 0)

		while j != columnas - 3 and ganador == 0:	# El programa recorre la matriz sin tomar en cuenta las ultimas 3 columnas

			if (tablero[i][j] == tablero[i][j+1] == tablero[i][j+2] == tablero[i][j+3]) and tablero[i][j] != 0: # Si encuentra 3 casillas a la dechera tales
				ganador = tablero[i][j];																		# que tienen el mismo valor que la actual y es distinto de cero se
				resaltarGanador(i, j, AMARILLO)																	# asigna como ganador el jugador de dichas casillas
				resaltarGanador(i, j+1, AMARILLO)
				resaltarGanador(i, j+2, AMARILLO)
				resaltarGanador(i, j+3, AMARILLO)	# Se resaltan las casillas ganadoras
				hay4enLinea = True

			j = j + 1

			# Verificacion de cota estrictamente decreciente
			assert(cota2 > columnas - 3 - j)

			# Actualizacion del valor de la cota
			cota2 = columnas - 3 - j

			# Verificacion de cota acotada por 0.
			assert(cota2 >= 0)

		i = i + 1
		
		# Verificacion de cota estrictamente decreciente
		assert(cota1 > filas - i)

		# Actualizacion del valor de la cota
		cota1 = filas - i

		# Verificacion de cota acotada por 0.
		assert(cota1 >= 0)

	# Postcondición: 
	assert(any ( any (tablero[i][j] == tablero[i][j+1] == tablero[i][j+2] == tablero[i][j+3] and tablero[i][j] != 0 for i in range(filas)) 
		     for j in range(columnas - 3)) == hay4enLinea)
	
	return ganador

def verificarVertical(filas: int, columnas:int, tablero: list) -> int:
	# Precondición: 
	assert(filas >= 4 and columnas >= 4 and 
		     all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(filas - 3)))

	# Verifica si  existe una linea vertical
	print("Verifica si  existe una linea vertical")

	# VAR
	# 	i: int;													// Variable auxiliar para iterar
	# 	j: int;													// Variable auxiliar para iterar
	# 	hay4enLinea: boolean;									// Variable que determina si hay 4 en linea
	# 	ganador: int;											// Variable que al almacena el ganador de la partida actual, (en caso de ser distinto de 0)
	#	filas: int;												// Numero de filas del tablero
	#	columnas: int;											// Numero de columnas del tablero
	#	tablero: list;											// Matriz del tablero de juego
	#	cota1: int;												// Variable que permite finalizar la iteracion exterior
	#	cota2: int;												// Varible que permite finalizar la iteracion interior

	i = 0
	hay4enLinea = False
	ganador = 0

	# Cota1:
	cota1 = columnas - i
	# Verificacion de cota acotada por 0.
	assert(cota1 >= 0)	
			
	while i != columnas:
		j = 0		
		
		# Cota2:
		cota2 = filas - 3 - j
		# Verificacion de cota acotada por 0.
		assert(cota2 >= 0)

		while j != filas - 3 and ganador == 0: # El promgrama recorre la matriz sin tomar en cuenta las 3 ultimas filas, 

			if (tablero[j][i] == tablero[j+1][i] == tablero[j+2][i] == tablero[j+3][i]) and tablero[j][i] != 0: # Si encuentra 3 casillas por debajo tales que
				ganador = tablero[j][i]																			# tienen el mismo valor que la actual y es distinto de cero
				resaltarGanador(j, i, AMARILLO)																	# se asigna como ganador el jugador de dichas casillas
				resaltarGanador(j+1, i, AMARILLO)
				resaltarGanador(j+2, i, AMARILLO)
				resaltarGanador(j+3, i, AMARILLO)	# Se resaltan las casillas ganadoras
				hay4enLinea = True


			j = j + 1

			# Verificacion de cota estrictamente decreciente
			assert(cota2 > filas - 3 - j)

			# Actualizacion del valor de la cota
			cota2 = filas - 3 - j

			# Verificacion de cota acotada por 0.
			assert(cota2 >= 0)

		i = i + 1

		# Verificacion de cota estrictamente decreciente
		assert(cota1 > columnas - i)

		# Actualizacion del valor de la cota
		cota1 = columnas - i

		# Verificacion de cota acotada por 0.
		assert(cota1 >= 0)

	# Postcondición: 
	assert(any (any (tablero[j][i] == tablero[j+1][i] == tablero[j+2][i] == tablero[j+3][i] and tablero[j][i] != 0 for i in range(columnas)) 
		 for j in range(filas - 3)) == hay4enLinea)
	
	return ganador

def verificarDiagonalDerecha(filas: int, columnas:int, tablero: list) -> int:
	# Precondicion: 
	assert(filas >= 4 and columnas >= 4 and 
		     all( all(0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si existe una linea diagonal derecha
	print("Verifica si existe una linea diagonal derecha")

	# VAR
	# 	i: int;													// Variable auxiliar para iterar
	# 	j: int;													// Variable auxiliar para iterar
	# 	hay4enLinea: boolean;									// Variable que determina si hay 4 en linea
	# 	ganador: int;											// Variable que al almacena el ganador de la partida actual, (en caso de ser distinto de 0)
	#	filas: int;												// Numero de filas del tablero
	#	columnas: int;											// Numero de columnas del tablero
	#	tablero: list;											// Matriz del tablero de juego
	#	cota1: int;												// Variable que permite finalizar la iteracion exterior
	#	cota2: int;												// Varible que permite finalizar la iteracion interior

	i = 0
	hay4enLinea = False
	ganador = 0

	# Cota1:
	cota1 = filas - 3 - i
	# Verificacion de cota acotada por 0.
	assert(cota1 >= 0)	
	
	while i != filas - 3:
		j = 0

		# Cota2:
		cota2 = columnas - 3 - j
		# Verificacion de cota acotada por 0.
		assert(cota2 >= 0)

		while j != columnas - 3 and ganador == 0:	# El programa recorre la matriz sin tomar en cuenta las ultimas 3 filas y las ultimas 3 columas

			if (tablero[i][j] == tablero[i+1][j+1] == tablero[i+2][j+2] == tablero[i+3][j+3]) and tablero[i][j] != 0:	# Si encuentra 3 casillas adyacentes hacia la diagonal inferior
				ganador = tablero[i][j]																					# derecha tales que tienen el mismo valor de la actual y es distinto de
				resaltarGanador(i, j, AMARILLO)																			# cero, se asigna como ganador al jugador de dichas casillas
				resaltarGanador(i+1, j+1, AMARILLO)
				resaltarGanador(i+2, j+2, AMARILLO)
				resaltarGanador(i+3, j+3, AMARILLO)		# Se resaltan las casillas ganadoras
				hay4enLinea = True

			j = j + 1

			# Verificacion de cota estrictamente decreciente
			assert(cota2 > columnas - 3 - j)

			# Actualizacion del valor de la cota
			cota2 = columnas - 3 - j

			# Verificacion de cota acotada por 0.
			assert(cota2 >= 0)

		i = i + 1

		# Verificacion de cota estrictamente decreciente
		assert(cota1 > filas - 3 - i)

		# Actualizacion del valor de la cota
		cota1 = filas - 3 - i

		# Verificacion de cota acotada por 0.
		assert(cota1 >= 0)

	# Postcondición: 
	assert(any (any (tablero[i][j] == tablero[i+1][j+1] == tablero[i+2][j+2] == tablero[i+3][j+3] and tablero[i][j] != 0 for j in range(columnas - 3))
	 		 for i in range(filas - 3)) == hay4enLinea)
	
	return ganador

def verificarDiagonalIzquierda(filas: int, columnas:int, tablero: list) -> int:
	# Precondición: 
	assert(filas >= 4 and columnas >= 4 and 
			 all( all(0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si existe una linea diagonal izquierda
	print("Verifica si existe una linea diagonal izquierda")

	# VAR
	# 	i: int;													// Variable auxiliar para iterar
	# 	j: int;													// Variable auxiliar para iterar
	# 	hay4enLinea: boolean;									// Variable que determina si hay 4 en linea
	# 	ganador: int;											// Variable que al almacena el ganador de la partida actual, (en caso de ser distinto de 0)
	#	filas: int;												// Numero de filas del tablero
	#	columnas: int;											// Numero de columnas del tablero
	#	tablero: list;											// Matriz del tablero de juego
	#	cota1: int;												// Variable que permite finalizar la iteracion exterior
	#	cota2: int;												// Varible que permite finalizar la iteracion interior

	i = 3
	hay4enLinea = False
	ganador = 0

	# Cota1:
	cota1 = columnas - i
	# Verificacion de cota acotada por 0.
	assert(cota1 >= 0)	

	while i != columnas:

		j = 0

		# Cota2:
		cota2 = filas - 3 - j
		# Verificacion de cota acotada por 0.
		assert(cota2 >= 0)

		while j != filas - 3 and ganador == 0: # El programa recorre la matriz sin tomar en cuenta las primeras 3 columnas y las ultimas 3 filas

			if (tablero[j][i] == tablero[j+1][i-1] == tablero[j+2][i-2] == tablero[j+3][i-3]) and tablero[j][i] != 0: # Si encuntra 3 casillas adyacentes hacia la diagonal izquierda
				ganador = tablero[j][i]																				  # inferior tales que su valor sea igual al de la casilla actual y es distinto
				resaltarGanador(j, i, AMARILLO)																		  # de cero, se asigna como ganador al jugador de dichas casillas
				resaltarGanador(j+1, i-1, AMARILLO)
				resaltarGanador(j+2, i-2, AMARILLO)
				resaltarGanador(j+3, i-3, AMARILLO)		# Se resaltan las casillas ganadoras
				hay4enLinea = True

			j = j + 1

			# Verificacion de cota estrictamente decreciente
			assert(cota2 > filas - 3 - j)

			# Actualizacion del valor de la cota
			cota2 = filas - 3 - j

			# Verificacion de cota acotada por 0.
			assert(cota2 >= 0)

		i = i + 1

		# Verificacion de cota estrictamente decreciente
		assert(cota1 > columnas - i)

		# Actualizacion del valor de la cota
		cota1 = columnas - i

		# Verificacion de cota acotada por 0.
		assert(cota1 >= 0)

	# Postcondición:
	assert(any( any(tablero[j][i] == tablero[j+1][i-1] == tablero[j+2][i-2] == tablero[j+3][i-3] and tablero[j][i] != 0 for i in range(columnas))
			 for j in range(filas - 3)) == hay4enLinea) 
	
	return ganador

def verificarTablero(numJugadas: int, filas: int, columnas:int) -> bool:
	# Precondición: 
	assert(filas >= 4 and columnas >= 4 and numJugadas <= filas * columnas)

	# Verifica si el tablero está lleno
	print("Verifica si el tablero está lleno")

	# VAR 
	# 	continuar: boolean;								// Variable que determina si la partida ha finalizado o no
	#	numJugadas: int;								// Variable que almacena el numero de jugadas de la partida actual
	#	filas: int;										// Numero de filas del tablero
	#	columnas: int;									// Numero de columnas del tablero

	if numJugadas == filas * columnas:	# Verifica si el numero de jugadas es igual al producto de las filas por las columnas, pues asi se confirma que ya el tablero esta lleno
		continuar = False 	# En caso de que ocurra se da la partida por finalizada
	else:
		continuar = True

	# Postcondición: 
	assert((numJugadas != filas * columnas or continuar == False) and (numJugadas == filas * columnas or continuar == True))
	
	return continuar

def jugadaPC(filas: int, columnas: int, numJugadasPC: int, tablero: int, ultimaJugada: list, estrategia: int) -> (int, int):

	# Inteligencia Artificial del computador
	# Toma una estrategia y la sigue mientras sea posible, en caso de no serlo
	# En caso de que el jugador tenga una fila vertical de 3 fichas, la tranca
	# toma una nueva estrategia aleatoriamente.

	# print("Genera una jugada que tenga cierto nivel de dificultad.")

	# CONST
	# 	intentosMaximos: int;									// Numero maximo de intentos que puede hacer la computadora de intentar con varias estrategias antes de jugar random 

	# VAR
	# 	puedeJugar: boolean;									// Variable que determina si las estrategias comprobadas pueden llevarse a cabo
	# 	estrategia: int;										// Variable que almacena la estrategia a llevar a cabo por la computadora
	# 	jugada: int;											// Variable que almacena la columna en la que se desea jugar	
	# 	i: int;													// Variable auxiliar para realizar la iteracion
	#	filas: int;												// Numero de filas del tablero
	#	columnas: int;											// Numero de columnas del tablero
	#	numJugadasPC: int;										// Variable que almacena el numero de jugadas realizadas por la computadora
	#	tablero: int;											// Matriz del tablero de juego
	#	ultimaJugada: int;										// Variable que almacena la fila y columna de la ultima jugada de la computadora
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media
	#	cota: int;												// Variable que permite finalizar la iteracion
		
	# Precondición: 
	assert(filas >= 4 and columnas >= 4 and numJugadas >= 0 and 
		all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))
	
	intentosMaximos = 50
	puedeJugar = False
	i = 0
	tranca = False

	if numJugadasPC == 0: 	# Si es la primera jugada de la computadora, se asigna una jugada y una estrategia random
		jugada = randomJugadaPC(columnas)
		estrategia = randomEstrategia()
	else:

		# Verifica antes de jugar que haya una fila vertical de tres fichas de jugador para trancarla
		if any (any (tablero[j][i] == tablero[j+1][i] == tablero[j+2][i] == 1 and tablero[j-1][i] == 0 for i in range(columnas)) 
		 for j in range(1, filas - 2)):
		 	for i in range(columnas):
		 		for j in range(filas - 2):
		 			if tablero[j][i] == tablero[j+1][i] == tablero[j+2][i] == 1 and tablero[j-1][i] == 0:
		 				jugada = i
		 				tranca = True
		# Sigue que con su estrategia
		else:
			# Cota:
			cota = intentosMaximos - i

			# Verificacion de cota acotada por 0.
			assert(cota >= 0)

			while puedeJugar == False and i != intentosMaximos:
				if estrategia == 0: # Vertical

					jugada, puedeJugar, estrategia = compruebaJugadaVertical(ultimaJugada, tablero, estrategia)

				elif estrategia == 1: # Horizontal Derecha

					jugada, puedeJugar, estrategia = compruebaJugadaHorizontalDerecha(ultimaJugada, tablero, columnas, filas, estrategia)

				elif estrategia == 2: # Horizontal Izquierda

					jugada, puedeJugar, estrategia = compruebaJugadaHorizontalIzquierda(ultimaJugada, tablero, columnas, filas, estrategia)	

				elif estrategia == 3: # Diagonal derecha abajo
					
					jugada, puedeJugar, estrategia = compruebaJugadaDiagonalDerechaAbajo(ultimaJugada, tablero, columnas, filas, estrategia)
				
				elif estrategia == 4: # Diagonal izquierda arriba

					jugada, puedeJugar, estrategia = compruebaJugadaDiagonalIzquierdaArriba(ultimaJugada, tablero, estrategia)

				elif estrategia == 5: # Diagonal izquierda abajo

					jugada, puedeJugar, estrategia = compruebaJugadaDiagonalIzquierdaAbajo(ultimaJugada, tablero, filas, estrategia)

				elif estrategia == 6: # Diagonal derecha arriba

					jugada, puedeJugar, estrategia = compruebaJugadaDiagonalDerechaArriba(ultimaJugada, tablero, columnas, estrategia)


				i = i + 1

				# Verificacion de cota estrictamente decreciente.
				assert(cota > intentosMaximos - i)

				cota = intentosMaximos - i

				# Verificacion de cota acotada por 0.
				assert(cota >= 0)

			if jugada == -1:		# En caso de que se se salga del ciclo sin haber escogido ninguna estrategia (debido al numero de intentos maximos), se asigna una jugada y estrategia random
				jugada = randomJugadaPC(columnas)
				estrategia = randomEstrategia()

	# Postcondición: 
	assert(0 <= jugada < columnas)
	
	return jugada, estrategia, tranca


def compruebaJugadaVertical(ultimaJugada: list, tablero: list, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
		     (all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas))))
	
	# Verifica si puede jugar en la casilla de arriba
	# print("Verifica si puede jugar en la casilla de arriba")

	# VAR
	#	ultimaJugada: list;										// Variable que almacena la fila y columna de la ultima jugada realizada por la computadora
	#	tablero: list;											// Matriz del tablero de juego
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media
	#	puedeJugar: bool 										// Variable que determina si las estrategias comprobadas pueden llevarse a cabo
	#	jugada: int;											// Variable que almacena la columna donde se desea jugar

	if ultimaJugada[0] != 0:	# Verifica que la ultima jugada no haya sido en la primera fila
		if tablero[ultimaJugada[0] - 1][ultimaJugada[1]] == 0: 	# Verifica que la casilla encima de la ultima jugada este libre
			jugada = ultimaJugada[1]	# Si esta libre, asigna su jugada la misma columna
			puedeJugar = True
		else:	# Si no esta libre, cambia de estrategia
			jugada = -1
			estrategia = randomEstrategia()
			puedeJugar = False
	else:	# Si esta en la primera fila, cambia de estrategia
		jugada = -1
		estrategia = randomEstrategia()
		puedeJugar = False

	# Postcondición: 
	assert((ultimaJugada[0] == 0 or (( tablero[ultimaJugada[0] - 1][ultimaJugada[1]] != 0 or (puedeJugar == True and jugada == ultimaJugada[1])) and
	 	 	 (tablero[ultimaJugada[0] - 1][ultimaJugada[1]] == 0 or (puedeJugar == False and jugada == -1)))) and (ultimaJugada[0] != 0 or (jugada == -1 and puedeJugar == False)))

	return jugada, puedeJugar, estrategia

def compruebaJugadaHorizontalDerecha(ultimaJugada: list, tablero: list, columnas:int, filas: int, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
			all (all (0 <= tablero[i][j] <= 2 for j in range(columnas)) for i in range(filas)))

	# Verifica si puede jugar en la casilla de la dereccha
	# print("Verifica si puede jugar en la casilla de la derecha")

	# VAR
	#	ultimaJugada: list;										// Variable que almacena la fila y columna de la ultima jugada realizada por la computadora
	#	tablero: list;											// Matriz del tablero de juego
	#	columnas: int;											// Numero de columnas del tablero
	#	filas: int;												// Numero de filas del tablero
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media
	#	puedeJugar: bool 										// Variable que determina si las estrategias comprobadas pueden llevarse a cabo
	#	jugada: int;											// Variable que almacena la columna donde se desea jugar

	if ultimaJugada[1] != columnas - 1:		# Verifica que la ultima jugada no haya sido en la ultima columnas
		if tablero[ultimaJugada[0]][ultimaJugada[1] + 1] == 0: 	# Verifica que la casilla de la derecha este libre
			if ultimaJugada[0] != filas - 1:			# Verifica que la ultima jugada no haya sido en la ultima fila
				if tablero[ultimaJugada[0] + 1][ultimaJugada[1] + 1] != 0:	# En caso de haber sido en la ultima fila, verifica que la casilla debajo de la casilla de la derecha este ocupada por alguna ficha
					jugada = ultimaJugada[1] + 1 # En caso de estarlo, asigna la jugada en la columna de la derecha
					puedeJugar = True
				else:
					jugada = -1		# Si no esta ocupada por ninguna ficha, cambia de estrategia
					estrategia = randomEstrategia()
					puedeJugar = False
			else:
				jugada = ultimaJugada[1] + 1		# Si esta en la ultima fila, asigna la jugada en la columna de la derecha
				puedeJugar = True
		else:
			jugada = -1
			estrategia = randomEstrategia()		# Si la casilla de la derecha esta ocupada, cambia de estrategia
			puedeJugar = False
	else:
		jugada = -1
		estrategia = randomEstrategia()			# Si la ultima jugada fue en la ultima columna, cambia de estrategia
		puedeJugar = False

	# Postcondición: 
	assert(
		(puedeJugar == True and 0 <= jugada <= columnas - 1) or
		(puedeJugar == False and jugada == -1)
	)

	return jugada, puedeJugar, estrategia

def compruebaJugadaHorizontalIzquierda(ultimaJugada: list, tablero: list, columnas: int, filas: int, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	 		 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si puede jugar en la casilla de la izquierda
	# print("Verifica si puede jugar en la casilla de la izquierda")

	# VAR
	#	ultimaJugada: list;										// Variable que almacena la fila y columna de la ultima jugada realizada por la computadora
	#	tablero: list;											// Matriz del tablero de juego
	#	columnas: int;											// Numero de columnas del tablero
	#	filas: int;												// Numero de filas del tablero
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media
	#	puedeJugar: bool 										// Variable que determina si las estrategias comprobadas pueden llevarse a cabo
	#	jugada: int;											// Variable que almacena la columna donde se desea jugar

	if ultimaJugada[1] != 0:	# Verifica que la ultima jugada no haya sido en la primera columna
		if tablero[ultimaJugada[0]][ultimaJugada[1] - 1] == 0:	# Verifica que la casilla de la izquierda este vacia
			if ultimaJugada[0] != filas - 1:		# Verifica que la ultima jugada no haya sido en la ultima fila
				if tablero[ultimaJugada[0] + 1][ultimaJugada[1] - 1] != 0:		# Si no lo fue, verifica que la casilla debajo de la casilla izquierda este ocupada por alguna ficha
					jugada = ultimaJugada[1] - 1	# En caso de estarlo, asigna la jugada en la columna de la izquierda
					puedeJugar = True
				else:
					jugada = -1		# En caso de no estar ocupada, cambia de estrategia
					estrategia = randomEstrategia()
					puedeJugar = False
			else:
				jugada = ultimaJugada[1] - 1	# Si esta en la ultima fila, asigna la jugada en la columna de la izquierda
				puedeJugar = True
		else:
			jugada = -1				# Si la casilla de la izquierda no esta vacia, cambia de estrategia
			estrategia = randomEstrategia()
			puedeJugar = False
	else:
		jugada = -1				# Si la ultima jugada se realizo en la primera columna, cambia de estrategia
		estrategia = randomEstrategia()
		puedeJugar = False

	# Postcondición: 
	assert(
		(puedeJugar == True and 0 <= jugada <= columnas - 1) or
		(puedeJugar == False and jugada == -1)
	)
	
	return jugada, puedeJugar, estrategia


def compruebaJugadaDiagonalDerechaAbajo(ultimaJugada: list, tablero: list, columnas:int, filas:int, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	   	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si puede jugar en la casilla inferior derecha
	# print("Verifica si puede jugar en la casilla inferior derecha")

	# VAR
	#	ultimaJugada: list;										// Variable que almacena la fila y columna de la ultima jugada realizada por la computadora
	#	tablero: list;											// Matriz del tablero de juego
	#	columnas: int;											// Numero de columnas del tablero
	#	filas: int;												// Numero de filas del tablero
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media
	#	puedeJugar: bool 										// Variable que determina si las estrategias comprobadas pueden llevarse a cabo
	#	jugada: int;											// Variable que almacena la columna donde se desea jugar

	if ultimaJugada[0] == filas - 1 or ultimaJugada[1] == columnas - 1:		# Si la ultima jugada se realizo en la ultima fila o en la ultima columna, cambia de estrategia
		jugada = -1
		estrategia = randomEstrategia()
		puedeJugar = False
	else:
		if tablero[ultimaJugada[0] + 1][ultimaJugada[1] + 1] == 0:	# Verifica que si la casilla inferior derecha esta vacia
			if ultimaJugada[0] != filas - 2:				# En caso de estarlo, verifica si la ultima jugada no se realizo en la penultima fila
				if tablero[ultimaJugada[0] + 2][ultimaJugada[1] + 1] != 0:	# Si no se realizo en la penultima fila, verifica que la casilla inferior a la inferior derecha este ocupada por alguna ficha
					jugada = ultimaJugada[1] + 1 # En caso de que este ocupada, asigna la jugada en la columna derecha
					puedeJugar = True
				else:
					jugada = -1						# En caso de que no este ocupada, cambia de estrategia
					estrategia = randomEstrategia()
					puedeJugar = False
			else:
				jugada = ultimaJugada[1] + 1		# Si la ultima jugada se realizo en la penultima fila, asigna la jugada en la columna derecha
				puedeJugar = True
		else:
			jugada = -1			# Si la casilla inferior derecha no esta vacia, cambia de estrategia
			estrategia = randomEstrategia()
			puedeJugar = False

	# Postcondición: 
	assert(
		(puedeJugar == True and 0 <= jugada <= columnas - 1) or
		(puedeJugar == False and jugada == -1)
	)

	return jugada, puedeJugar, estrategia

def compruebaJugadaDiagonalIzquierdaArriba(ultimaJugada: list, tablero: list, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	   	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si puede jugar en la casilla superior izquierda
	# print("Verifica si puede jugar en la casilla superior izquierda")

	# VAR
	#	ultimaJugada: list;										// Variable que almacena la fila y columna de la ultima jugada realizada por la computadora
	#	tablero: list;											// Matriz del tablero de juego
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media
	#	puedeJugar: bool 										// Variable que determina si las estrategias comprobadas pueden llevarse a cabo
	#	jugada: int;											// Variable que almacena la columna donde se desea jugar
	
	if ultimaJugada[0] == 0 or ultimaJugada[1] == 0:	# Si la ultima jugada se realizo en la primera fila o en la primera columna, cambia de estrategia
		jugada = -1
		estrategia = randomEstrategia()
		puedeJugar = False
	else:
		if tablero[ultimaJugada[0] - 1][ultimaJugada[1] - 1] == 0:	# Verifica que la casilla superior izquierda este vacia
			if tablero[ultimaJugada[0]][ultimaJugada[1] - 1] != 0:	# En caso de estarlo, verifica que la casilla de la izquierda este ocupada por alguna ficha
				jugada = ultimaJugada[1] - 1	# Si esta ocupada, asigna la jugada en la columna izquierda
				puedeJugar = True
			else:
				jugada = -1		# Si la casilla izquierda no esta ocupada, cambia de estrategia
				estrategia = randomEstrategia()
				puedeJugar = False	
		else:			# Si la casilla superior izquierda no esta vacia, cambia de estrategia
			jugada = -1
			estrategia = randomEstrategia()
			puedeJugar = False

	# Postcondición: 
	assert(
		(puedeJugar == True and 0 <= jugada <= columnas - 1) or
		(puedeJugar == False and jugada == -1)
	)

	return jugada, puedeJugar, estrategia

def compruebaJugadaDiagonalIzquierdaAbajo(ultimaJugada: list, tablero: list, filas:int, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	   	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si puede jugar en la casilla inferior izquierda
	# print("Verifica si puede jugar en la casilla inferior izquierda")

	# VAR
	#	ultimaJugada: list;										// Variable que almacena la fila y columna de la ultima jugada realizada por la computadora
	#	tablero: list;											// Matriz del tablero de juego
	#	filas: int;												// Numero de filas del tablero
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media
	#	puedeJugar: bool 										// Variable que determina si las estrategias comprobadas pueden llevarse a cabo
	#	jugada: int;											// Variable que almacena la columna donde se desea jugar


	if ultimaJugada[0] == filas - 1 or ultimaJugada[1] == 0:	# Si la ultima jugada se realizo en la ultima fila o en la primra columna, cambia de estrategia
		jugada = -1
		estrategia = randomEstrategia()
		puedeJugar = False
	else:
		if tablero[ultimaJugada[0] + 1][ultimaJugada[1] - 1] == 0:		# Verifica que la casilla inferior izquierda este vacia
			if ultimaJugada[0] != filas - 2:		# En caso de estarlo, verifica si la ultima jugada no se realizo en la penultima fila
				if tablero[ultimaJugada[0] + 2][ultimaJugada[1] - 1] != 0: 	# Si no se realizo en la penultima fila, verifica que la casilla inferior a la inferior izquierda este ocupada por alguna ficha
					jugada = ultimaJugada[1] - 1				# En caso de que este ocupada, asigna la jugada en la columna izquierda
					puedeJugar = True
				else:
					jugada = -1
					estrategia = randomEstrategia()				# En caso de que no este ocupada, cambia de estrategia
					puedeJugar = False
			else:
				jugada = ultimaJugada[1] - 1					# Si la ultima jugada se realizo en la penultima fila, asigna la jugada en la columna derecha
				puedeJugar = True
		else:
			jugada = -1
			estrategia = randomEstrategia()				# Si la casilla inferior izquierda no esta vacia, cambia de estrategia
			puedeJugar = False

	# Postcondición: 
	assert(
		(puedeJugar == True and 0 <= jugada <= columnas - 1) or
		(puedeJugar == False and jugada == -1)
	)

	return jugada, puedeJugar, estrategia

def compruebaJugadaDiagonalDerechaArriba(ultimaJugada: list, tablero: list, columnas: int, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	   	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si puede jugar en la casilla superior derecha
	# print("Verifica si puede jugar en la casilla superior derecha ")

	# VAR
	#	ultimaJugada: list;										// Variable que almacena la fila y columna de la ultima jugada realizada por la computadora
	#	tablero: list;											// Matriz del tablero de juego
	#	columnas: int;											// Numero de columnas del tablero
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media
	#	puedeJugar: bool 										// Variable que determina si las estrategias comprobadas pueden llevarse a cabo
	#	jugada: int;											// Variable que almacena la columna donde se desea jugar


	if ultimaJugada[0] == 0 or ultimaJugada[1] == columnas - 1:				# Si la ultima jugada se realizo en la primera fila o en la ultima columna, cambia de estrategia
		jugada = -1
		estrategia = randomEstrategia()
		puedeJugar = False
	else:
		if tablero[ultimaJugada[0] - 1][ultimaJugada[1] + 1] == 0:		# Verifica que la casilla superior derecha este vacia
			if tablero[ultimaJugada[0]][ultimaJugada[1] + 1] != 0:		# En caso de estarlo, verifica que la casilla de la derecha este ocupada por alguna ficha
				jugada = ultimaJugada[1] + 1				# Si esta ocupada, asigna la jugada en la columna derecha
				puedeJugar = True
			else:
				jugada = -1
				estrategia = randomEstrategia()		# Si la casilla derecha no esta ocupada, cambia de estrategia
				puedeJugar = False
		else:
			jugada = -1
			estrategia = randomEstrategia()			# Si la casilla superior derecha no esta vacia, cambia de estrategia
			puedeJugar = False

	# Postcondición: 
	assert(
		(puedeJugar == True and 0 <= jugada <= columnas - 1) or
		(puedeJugar == False and jugada == -1)
	)

	return jugada, puedeJugar, estrategia

def randomEstrategia() -> int:

	# print("Devuelve una estrategia aleatoria.")
	# Devuelve una estrategia aleatoria de las 7 disponibles

	# VAR
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media
	
	# Precondición: 
	assert(True)
	
	estrategia = random.randrange(7)
	# print("Estrategia seleccionada: " + str(estrategia))
	
	# Postcondición: 
	assert(0 <= estrategia < 7)

	return estrategia 

def randomJugadaPC(columnas: int) -> int:
	# Precondición:
	assert(True)
	# print("Devuelve una columna aleatoriamente para generar la jugada de la computadora.")
	# Devuelve una columna aleatoriamente para generar la jugada de la computadora

	# VAR
	#	columnas: int;											// Numero de columnas del tablero
	#	jugada: int;											// Variable que almacena la columna donde se deasea jugar

	jugada = random.randrange(columnas)
	# print("Columna seleccionada: " + str(jugada))

	# Postcondición
	assert(0 <= jugada < columnas)

	return jugada

def dibujarTablero(colorlineas: list, colorfondo: list, nombre: str, partidasGanadasPersona: int, partidasGanadasPC: int, numEmpates: int) -> 'void':
	# Precondición: 
	assert(True)

	# Dibuja el tablero que sera utilizado para el juego

	# VAR
	#	colorlineas: list;										// Variable que almacena el color de las lineas del tablero
	#	colorfondo: list;										// Variable que almacena el color del fondo del tablero

	# Fondo
	pantalla.fill(colorfondo)
	# Cuadrado exterior
	pygame.draw.line(pantalla, colorlineas, (130, 90), (130, 620))
	pygame.draw.line(pantalla, colorlineas, (1120, 90), (1120, 620))
	pygame.draw.line(pantalla, colorlineas, (130, 90), (1120, 90))
	pygame.draw.line(pantalla, colorlineas, (130, 620), (1120, 620))

	# Filas
	pygame.draw.line(pantalla, colorlineas, (130, 178), (1120, 178))
	pygame.draw.line(pantalla, colorlineas, (130, 266), (1120, 266))
	pygame.draw.line(pantalla, colorlineas, (130, 354), (1120, 354))
	pygame.draw.line(pantalla, colorlineas, (130, 442), (1120, 442))
	pygame.draw.line(pantalla, colorlineas, (130, 530), (1120, 530))

	# Columnas
	pygame.draw.line(pantalla, colorlineas, (272, 90), (272, 620))
	pygame.draw.line(pantalla, colorlineas, (414, 90), (414, 620))
	pygame.draw.line(pantalla, colorlineas, (556, 90), (556, 620))
	pygame.draw.line(pantalla, colorlineas, (698, 90), (698, 620))
	pygame.draw.line(pantalla, colorlineas, (840, 90), (840, 620))
	pygame.draw.line(pantalla, colorlineas, (982, 90), (982, 620))

	# Inicializa la fuente
	fuente = pygame.font.Font(None, 75)

	# Variables a printear en pantalla
	uno = fuente.render("0", True, NEGRO)
	dos = fuente.render("1", True, NEGRO)
	tres = fuente.render("2", True, NEGRO)
	cuatro = fuente.render("3", True, NEGRO)
	cinco = fuente.render("4", True, NEGRO)
	seis = fuente.render("5", True, NEGRO)
	siete = fuente.render("6", True, NEGRO)
	printNombre = fuente.render(nombre + ": " + str(partidasGanadasPersona), True, NEGRO)
	printPC = fuente.render("Computadora: " + str(partidasGanadasPC), True, NEGRO)
	printEmpates = fuente.render("Empates: " + str(numEmpates), True, NEGRO)

	# Dibuja las variables en la pantalla
	pantalla.blit(uno, [185, 40])
	pantalla.blit(dos, [330, 40])
	pantalla.blit(tres, [470, 40])
	pantalla.blit(cuatro, [610, 40])
	pantalla.blit(cinco, [750, 40])
	pantalla.blit(seis, [900, 40])
	pantalla.blit(siete, [1040, 40])
	pantalla.blit(printNombre, [100, 650])
	pantalla.blit(printPC, [400, 650])
	pantalla.blit(printEmpates, [850, 650])
	

	pygame.display.flip()			# Actualiza el tablero

	# print("Se dibuja el tablero en la interfaz gráfica")

	# Postcondición: 
	# Se dibuja en una ventana gráfica un tablero con "filas" filas y "columnas" columnas de color "color"

def cargarTablero(colorlineas: list, colorfondo: list, colorpc: list, colorjugador: list, filas: int, columas: int, tablero: list, nombre: str, 
	partidasGanadasPersona: int, partidasGanadasPC: int, numEmpates: int) -> 'void':
	# Precondición: 
	assert(True)

	# Carga el tablero usando la informacion cargada el archivo donde se guardo la partida.

	# VAR
	# 	colorlineas: list;										// Variable que almacena el color de las lineas del tablero
	# 	colorfondo: list;										// Varibale que almacena el color del fondo del tablero
	#	colorpc: list;											// Variable que almacena el color de las fichas de la computadora
	#	colorjugador: list;										// Variable que almacena el color de las fichas del jugador
	#	filas: int;												// Numero de filas del tablero
	#	columnas: int;											// Numero de columnas del tablero
	#	tablero: list;											// Matriz del tablero de juego


	dibujarTablero(colorlineas, colorfondo, nombre, partidasGanadasPersona, partidasGanadasPC, numEmpates)

	for i in range(filas):			# El ciclo va recorriendo la matriz en busca de fichas, si encuentra un 1 en la matriz dibuja la ficha de color rojo en la posicion correspondiente, 
		for j in range(columas):	# si encuentra un 2 la dibuja de color azul,
			if tablero[i][j] == 1:
				pygame.draw.circle(pantalla, colorjugador, (201 + j*142, 134 + i*88), 30, 0)
			elif tablero[i][j] == 2:
				pygame.draw.circle(pantalla, colorpc, (201 + j*142, 134 + i*88), 30, 0)

	pygame.display.flip()		# Actualiza el tablero

def dibujarJugada(i: int, jugada: int, color: list) -> 'void':
	# Precondición: 
	assert(True)
	# print("Dibuja en el tablero la jugada luego de haberla reflejado en la matriz")
	# Dibuja en el tablero la jugada luego de haberla reflejado en la matriz

	# VAR
	#	i: int;													// Variable que almacena la fila donde se debe dibujar la ficha
	#	jugada: int;											// Variable que almacena la columna donde se debe dibujar la ficha
	#	color: list;											// Variable que almacena el color de la ficha

	pygame.draw.circle(pantalla, color, (201 + jugada*142, 134 + i*88), 30, 0)
	# Postcondición: 
	# Se dibuja un circulo de color "color" en la casilla posicionada en la fila "i" y columna "jugada" del tablero

def resaltarGanador(i: int, j: int, color: list) -> 'void':
	# Precondición: 
	assert(True)
	# print("Resalta las fichas que se encuentran en 4 en linea")
	# Resalta las fichas que se encuentran en 4 en linea

	# VAR
	#	i: int;													// Variable que almacena la fila donde se encuentra la ficha a resaltar
	#	j: int;													// Variable que almacena la columna donde se encuentra la ficha a resaltar
	#	color: int;												// Variable que almacena el color con el que se resaltara la ficha


	pygame.draw.circle(pantalla, color, (201 + j*142, 134 + i*88), 25, 0)
	pygame.display.flip()

	# Postcondición: 
	# Se resalta el circulo de la casilla posicionada en la fila "i" y columna "j" del tablero de color "color" }

def pedirNombre() -> str:
	# Solicita el nombre del jugador.
	# Precondicion:
	assert(True)

	# VAR
	#	nombre: str;											// Variable que almacena del nombre del jugador

	nombre = str(input("Por favor, ingrese su nombre: "))
	print("Hola "+ nombre)

	# Postcondicion:
	assert(True)

	return nombre

def guardarPartida(nombre: str, filas: int, columnas: int, tablero: list, dificultad: int, ultimoGanador: int, jugador: int,
	numPartidas: int, ultimaJugada: list, numJugadas: int, numJugadasPC: int, numEmpates: int, partidasGanadasPersona: int,
	partidasGanadasPC: int, estrategia: int) -> bool:

	# Pregunta al jugador si desea guardar la partida. Si desea guardarla escribe un archivo con toda la informacion de la partida actual y los resultados de las partidas
	# anteriores

	# VAR
	#	nombre: str;											// Variable que almacena el nombre del jugador
	#	filas: int;												// Numero de filas del tablero
	#	columnas: int;											// Numero de columnas del tablero
	#	tablero: list;											// Matriz del tablero de juego
	#	dificultad: int;										// Variable que almacena la dificultad seleccionada por el jugador
	#	ultimoGanador: int;										// Variable que almacena el ganador de la partida anterior
	#	jugador: int;											// Varibale que almacena el jugador del turno actual
	#	numPartidas: int;										// Variable que almacena la cantidad de partidas jugadas
	#	ultimaJugada: list;										// Variable que almacena la fila y la columna de la ultima jugada realizada por la computadora
	#	numJugadas: int;										// Variable que almacena el numero de jugadas realizadas en la partida actual
	#	numJugadasPC: int;										// Variable que almacena el numero de jugadas realizadas por la computadora en la partida actual
	#	numEmpates: int;										// Variable que almacena el numero de empates de todos los juegos
	#	partidasGanadasPersona: int;							// Variable que almacena las partidas ganadas por el jugadora
	#	partidasGanadasPC: int;									// Variable que almacena las partidas ganadas por la computadora
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media
	#	guarda: bool;											// Variable que determina si el jugador desea guardar la partida o no

	while True:
		try:
			confirmacion = int(input("Por favor " + str(nombre) + ", ingrese 1 si desea guardar la partida, en caso contrario ingrese 0: "))

			# Precondición: 
			assert(
				filas >= 4 and columnas >= 4 and all ( all ( 0 <= tablero[x][y] <= 2 for x in range(filas)) for y in range(columnas))
				and 0 <= dificultad <= 1 and 0 <= ultimoGanador <= 2 and 0 <= jugador <= 2 and numPartidas >= 0 and 0 <= ultimaJugada[0] < filas
				and 0 <= ultimaJugada[1] < columnas and 0 <= numJugadas < filas*columnas and 0 <= numJugadasPC < (filas*columnas)/2 and 
				numEmpates >= 0 and partidasGanadasPersona >= 0 and partidasGanadasPC >= 0 and 0 <= estrategia <= 6
				)

			if confirmacion == 1:
				guardar = True
				escribeArchivo(nombre, filas, columnas, tablero, dificultad, ultimoGanador, jugador, numPartidas,
					ultimaJugada, numJugadas, numJugadasPC, numEmpates, partidasGanadasPersona, partidasGanadasPC, estrategia)
			elif confirmacion == 0:
				guardar = False

			break
		except:
			print("Por favor " + nombre + ", ingrese una opción válida.")

	# Postcondición: 
	assert((confirmacion == 1 and guardar == True) or (confirmacion == 0 and guardar == False))

	return guardar

def escribeArchivo(nombre: str, filas: int, columnas: int, tablero: list, dificultad: bool, ultimoGanador: int, jugador: int,
	numPartidas: int, ultimaJugada: list, numJugadas: int, numJugadasPC: int, numEmpates: int, partidasGanadasPersona: int,
	partidasGanadasPC: int, estrategia: int) -> 'void':

	# Precondición:
	assert(
		filas >= 4 and columnas >= 4 and all ( all ( 0 <= tablero[x][y] <= 2 for x in range(filas)) for y in range(columnas))
		and 0 <= dificultad <= 1 and 0 <= ultimoGanador <= 2 and 1 <= jugador <= 2 and numPartidas >= 0 and 0 <= ultimaJugada[0] < filas
		and 0 <= ultimaJugada[1] < columnas and 0 <= numJugadas < filas*columnas and 0 <= numJugadasPC < (filas*columnas)/2 and 
		numEmpates >= 0 and partidasGanadasPersona >= 0 and partidasGanadasPC >= 0 and 0 <= estrategia <= 6
	)

	# Guarda los datos de la partida actual y los resultados anteriores en un archivo.

	# VAR
	#	nombre: str;											// Variable que almacena el nombre del jugador
	#	filas: int;												// Numero de filas del tablero
	#	columnas: int;											// Numero de columnas del tablero
	#	tablero: list;											// Matriz del tablero de juego
	#	dificultad: int;										// Variable que almacena la dificultad seleccionada por el jugador
	#	ultimoGanador: int;										// Variable que almacena el ganador de la partida anterior
	#	jugador: int;											// Varibale que almacena el jugador del turno actual
	#	numPartidas: int;										// Variable que almacena la cantidad de partidas jugadas
	#	ultimaJugada: list;										// Variable que almacena la fila y la columna de la ultima jugada realizada por la computadora
	#	numJugadas: int;										// Variable que almacena el numero de jugadas realizadas en la partida actual
	#	numJugadasPC: int;										// Variable que almacena el numero de jugadas realizadas por la computadora en la partida actual
	#	numEmpates: int;										// Variable que almacena el numero de empates de todos los juegos
	#	partidasGanadasPersona: int;							// Variable que almacena las partidas ganadas por el jugadora
	#	partidasGanadasPC: int;									// Variable que almacena las partidas ganadas por la computadora
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media


	with open('guardarPartida.txt', 'w') as f:
		f.write('Nombre\n')
		f.write(str(nombre) + '\n')
		f.write('Filas\n')
		f.write(str(filas) + '\n')
		f.write('Columnas\n')
		f.write(str(columnas) + '\n')
		f.write('Tablero\n')
		f.write(str(tablero) + '\n')
		f.write('Dficultad\n')
		f.write(str(dificultad) + '\n')
		f.write('ultimoGanador\n')
		f.write(str(ultimoGanador) + '\n')
		f.write('Jugador\n')
		f.write(str(jugador) + '\n')
		f.write('numPartidas\n')
		f.write(str(numPartidas) + '\n')
		f.write('ultimaJugada\n')
		f.write(str(ultimaJugada) + '\n')
		f.write('numJugadas\n')
		f.write(str(numJugadas) + '\n')
		f.write('numJugadasPC\n')
		f.write(str(numJugadasPC) + '\n')
		f.write('numEmpates\n')
		f.write(str(numEmpates) + '\n')
		f.write('partidasGanadasPersona\n')
		f.write(str(partidasGanadasPersona) + '\n')
		f.write('partidasGanadasPC\n')
		f.write(str(partidasGanadasPC) + '\n')
		f.write('estrategia\n')
		f.write(str(estrategia) + '\n')
	f.closed

	# Postcondición:
	assert(
		True
		)

def leeArchivo() -> (str, int, int, list, int, int, int, int, list, int, int, int, int, int, int):

	# Precondición:
	assert(True)

	# VAR
	#	nombre: str;											// Variable que almacena el nombre del jugador
	#	filas: int;												// Numero de filas del tablero
	#	columnas: int;											// Numero de columnas del tablero
	#	tablero: list;											// Matriz del tablero de juego
	#	dificultad: int;										// Variable que almacena la dificultad seleccionada por el jugador
	#	ultimoGanador: int;										// Variable que almacena el ganador de la partida anterior
	#	jugador: int;											// Varibale que almacena el jugador del turno actual
	#	numPartidas: int;										// Variable que almacena la cantidad de partidas jugadas
	#	ultimaJugada: list;										// Variable que almacena la fila y la columna de la ultima jugada realizada por la computadora
	#	numJugadas: int;										// Variable que almacena el numero de jugadas realizadas en la partida actual
	#	numJugadasPC: int;										// Variable que almacena el numero de jugadas realizadas por la computadora en la partida actual
	#	numEmpates: int;										// Variable que almacena el numero de empates de todos los juegos
	#	partidasGanadasPersona: int;							// Variable que almacena las partidas ganadas por el jugadora
	#	partidasGanadasPC: int;									// Variable que almacena las partidas ganadas por la computadora
	#	estrategia: int;										// Variable que almacena la estrategia a utilizar por la computadora en la dificultad media

	try:
		archivo = open('guardarPartida.txt')
		
		datos = archivo.readlines()

		for i in range(len(datos)):
			datos[i] = datos[i].rstrip('\n')

		print("Nombre: " + str(datos[1]))
		nombre = datos[1]
		filas = int(datos[3])
		columnas = int(datos[5])
		tablero = eval(datos[7])
		print("Dificultad: " + str(datos[9]))
		dificultad = int(datos[9])
		ultimoGanador = int(datos[11])
		jugador = int(datos[13])
		numPartidas = int(datos[15])
		ultimaJugada = eval(datos[17])
		numJugadas = int(datos[19])
		numJugadasPC = int(datos[21])
		print("Número de empates: " + str(datos[23]))
		numEmpates = int(datos[23])
		print("Partidas ganadas por " + str(nombre) + " " + str(datos[25]))
		partidasGanadasPersona = int(datos[25])
		print("Partidas ganadas por la computadora: " + str(datos[27]))
		partidasGanadasPC = int(datos[27])
		estrategia = int(datos[29])

		cargarTablero(NEGRO, BLANCO, AZUL, ROJO, filas, columnas, tablero, nombre, partidasGanadasPersona, partidasGanadasPC, numEmpates)

	except:
		print("Verifique que existe el archivo guardarPartida.txt, si no existe, no puede cargar una partida.")
		sys.exit()

	# Postcondición:
	assert(
			filas >= 4 and columnas >= 4 and all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)) and
			0 <= dificultad <= 1 and 0 <= ultimoGanador <= 2 and 1 <= jugador <= 2 and numPartidas >= 0 and
			0 <= ultimaJugada[0] <= filas and 0 <= ultimaJugada[1] <= columnas and numJugadas >= 0 and numJugadasPC >= 0 and 
			numEmpates >= 0 and partidasGanadasPersona >= 0 and partidasGanadasPC >= 0 and 0 <= estrategia <= 6
		)

	return nombre, filas, columnas, tablero, dificultad, ultimoGanador, jugador, numPartidas, ultimaJugada, numJugadas, numJugadasPC, numEmpates, partidasGanadasPersona, partidasGanadasPC, estrategia



def cargarPartida() -> bool:

	# VAR
	# cargar: bool;												// Variable que determina si el jugador desea guardar la partida o no

	while True:
		try:
			confirmacion = int(input("Por favor, ingrese 1 si desea cargar una partida, en caso contrario ingrese 0: "))

			assert(0 <= confirmacion <= 1)

			if confirmacion == 1:
				cargar = True
			elif confirmacion == 0:
				cargar = False

			break
		except:
			print("Por favor, ingrese una opción válida.")

	return cargar

# CONSTANTES:
# Colores que seran usados en el juego
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)

# Valores necesarios para la pantalla
ALTO = 720               # Alto de la ventana
ANCHO = 1280             # Ancho de la ventana


# Inicialización de variables.
filas = 6
columnas = 7
maxPartidas = 10
ultimaJugada = [0,0]
tablero = [[0]*(columnas) for x in range(filas)]
numPartidas = 0
partidasGanadasPC = 0
partidasGanadasPersona = 0
ultimoGanador = 0
numEmpates = 0
quiereSeguirJugando = True
validacion = True
ganador = 0
estrategia = -1
nombre = ''

# Precondición:
assert(filas>=4 and columnas >= 4 and maxPartidas >= 0)

# Inicializar la pantalla del juego
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("4 en Linea")
reloj = pygame.time.Clock()

# Loop del Juego

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			pygame.quit()
		else:
			# Cota: 
			# assert(maxPartidas - numPartidas)
			while quiereSeguirJugando == True and numPartidas != maxPartidas:

				# Inicializa los valores
				continuar = True
				if numPartidas == 0:
					if cargarPartida():
						nombre, filas, columnas, tablero, dificultad, ultimoGanador, jugador, numPartidas, ultimaJugada, numJugadas, numJugadasPC, numEmpates, partidasGanadasPersona, partidasGanadasPC, estrategia = leeArchivo()
					else:
						dificultad, jugador, numJugadas, numJugadasPC, nombre = inicializarPartida(numPartidas, ultimoGanador, filas, columnas, tablero, NEGRO, BLANCO, nombre, partidasGanadasPersona, partidasGanadasPC)
				else:
					dificultad, jugador, numJugadas, numJugadasPC, nombre = inicializarPartida(numPartidas, ultimoGanador, filas, columnas, tablero, NEGRO, BLANCO, nombre, partidasGanadasPersona, partidasGanadasPC)
				
				# Cota: 
				# assert(filas * columnas - numJugadas)
				while continuar == True and numJugadas != filas * columnas:
					
					ingresaJugada = True
					# Cota: No tiene, la iteracion se hará hasta que la jugada sea correcta
					while ingresaJugada == True:
						
						# Obtiene los valores de la jugada y verifica que sea correcto
						jugada, estrategia, tranca = obtenerJugada(filas, columnas, numJugadasPC, tablero, ultimaJugada, jugador, dificultad, estrategia, nombre)
						validacion = validarJugada(jugada, filas, columnas, tablero)

						if validacion == True:

							# Si la jugada se puede realizar, se almacena en el tablero.
							ultimaJugada, numJugadasPC = reflejarJugada(jugada, jugador, filas, columnas, tablero, ultimaJugada, numJugadasPC, tranca)
							jugador = cambiarTurno(jugador)
							numJugadas = numJugadas + 1

							# Verifica si existe un ganador
							continuar, ganador = verificar4enLinea(filas, columnas, tablero)
							
							if continuar == True:

								# Si no hay ganador,verifica que el tablero no esté lleno
								continuar = verificarTablero(numJugadas, filas, columnas)

								if continuar == False:
									# Si el tablero está lleno, finaliza la partida y aumenta el conteo de empates
									numEmpates = numEmpates + 1
									numPartidas = numPartidas + 1

								# Verifica que quiere continuar con la partida actual
								elif jugador == 1:
									# Pregunta al usuario si desea seguir jugando
									continuar = seguirPartida(nombre)
									if continuar == False:
										if guardarPartida(nombre, filas, columnas, tablero, dificultad, ultimoGanador, jugador,
											numPartidas, ultimaJugada, numJugadas, numJugadasPC, numEmpates, partidasGanadasPersona,
											partidasGanadasPC, estrategia) == False:
											partidasGanadasPC = partidasGanadasPC + 1
											numPartidas = numPartidas + 1
											ganador = 2
											ultimoGanador = ganador
										else:
											quiereSeguirJugando = False
							else:
								# Establece el ganador, le aumenta una victoria y lo registra para determinar el primer
								# jugador de la pŕoxima partida
								if ganador == 1:
									ultimoGanador = ganador
									partidasGanadasPersona = partidasGanadasPersona + 1
								else:
									ultimoGanador = ganador
									partidasGanadasPC = partidasGanadasPC + 1
								numPartidas = numPartidas + 1

							ingresaJugada = False

						else:
							# Si la jugada no se puede realizar, se solicita una nueva jugada
							ingresaJugada = True

				if quiereSeguirJugando:
					# Muestra el ganador de la partida
					entregaGanadorPartida(ganador, nombre)
					# Pregunta si se desea jugar otra partida
					quiereSeguirJugando = quiereSeguir(nombre)

			# Entrega los resultados finales de la partida
			entregaResultados(partidasGanadasPersona, partidasGanadasPC, numEmpates, nombre)
			sys.exit()
			pygame.quit()

# Postcondición:
assert(numPartidas >= 0 and partidasGanadasPersona >=0 and partidasGanadasPC >= 0 and quiereSeguirJugando == False)