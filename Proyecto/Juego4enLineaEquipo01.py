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
# 		filas:int;										# Numero de filas del tablero
# 		columnas: int;									# Numero de columnas del table
# 		maxPartidas: int;								# Numero maximo de partidas a jugar
#		NEGRO: list;									# Color utilizado en la parte grafica del programa	
#		BLANCO: list;									# Color utilizado en la parte grafica del programa
#		ROJO: list;										# Color utilizado en la parte grafica del programa
#		AZUL: list;										# Color utilizado en la parte grafica del programa
#		AMARILLO: list;									# Color utilizado en la parte grafica del programa
#		ALTO: int          							    # Alto de la ventana
#		ANCHO: int    							        # Ancho de la ventana
#		FPS: int   							            # Cuadros por segundo
#
# 	VAR
# 		tablero: list [0,filas) x [0,columnas) of int;	# Tablero de juego
# 		dificultad: int;								# Variable que almacena la dificultad seleccionada por el jugador (0 basico, 1 medio)
# 		ultimoGanador: int;								# Variable que almacena el ganador de la partida anterior
# 		jugador: int;									# Variable que almacena el jugador del turno actual
# 		numPartidas: int;								# Variable que almacena la cantidad de partidas jugadas
# 		jugada: int;									# Variable que almacena la columna donde se desea jugar
# 		ultimaJugada: list;								# Variable que almacena la fila y columna de la ultima jugada de la computadora
# 		continuar: bool;								# Variable que determina si una partida ha finalizado o no
# 		numJugadas: int;								# Variable que almacena el numero de jugadas de la partida actual
# 		numJugadasPC: int;								# Variable que almacena el numero de jugadas de la computadora en la partida actual
# 		numEmpates: int;								# Variable que almacena el numero de empates de todos los juegos
# 		partidasGanadasPersona: int;					# Variable que almacena la cantidad de veces que gana el jugador
# 		partidasGanadasPC: int;							# Variable que almacena la cantidad de veces que gana la computadora
# 		ganador: int;									# Variable que almacena el ganador de la partida actual
# 		validacion: bool;								# Variable que determina si una jugada es valida o no
# 		quiereSeguirJugando: bool;						# Variable que determina si el usuario desea jugar otra partia o no
# 		ingresaJugada: bool;							# Variable utilizada en el ciclo de cada jugada para en caso de no ser valida, poder ingresar otra jugada
#		nombre: str;									# Variable que almacena el nombre del jugador
#		estrategia: int:								# Variable que almacena la estrategia a utilizar por la computadora en la dificultad media

# Se importa la librería random para generar las jugadas aleatorias.
import random
# Se importa la libreria pygame para generar la grafica del juego.
import pygame
# Se importa la libreria sys para realizar una programacion robusta, y poder finalizar el programa
import sys

def seguirPartida() -> bool:

	# Precondición: 
	assert(True)

	# Le pregunta al usuario si quiere seguir con la partida.
	print("Le pregunta al usuario si quiere seguir con la partida.")

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

def entregaResultados(partidasGanadasPersona: int, partidasGanadasPC: int, numEmpates: int) -> 'void':
	# Precondición: 
	assert(partidasGanadasPersona >= 0 and partidasGanadasPC >= 0 and numEmpates >= 0)

	print("Se imprime la cantidad de partidas ganadas por el Jugador, PC y numero de empates")

	print("Número de partidas ganadas por la persona: " + str(partidasGanadasPersona))
	print("Número de partidas ganadas por la computadora: " + str(partidasGanadasPC))
	print("Número de empates: " + str(numEmpates))

	# Postcondición: 
	# Se imprime la cantidad de partidas ganadas por el Jugador, PC y numero de empates
	assert(True)

def entregaGanadorPartida(ganador: int) -> 'void':
	# Precondición: 
	assert(0 <= ganador <= 2)
	
	print("Entrega los resultados de la partida que acaba de finalizar")

	if ganador == 1:
		print(nombre+ " ha ganado la partida.")
	elif ganador == 2:
		print("La computadora ha ganado la partida.")
	else:
		print("Empate")
	
	# Postcondición: 
	assert(True)

def quiereSeguir() -> bool:
	# Precondición: 
	assert(True)

	# Le pregunta al jugador si desea jugar otra partida cuando ha finalizado una.
	print("El jugador ingresa si desea jugar otra partida")

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

def inicializarPartida(numPartidas: int, ultimoGanador: int, filas: int, columnas: int,tablero: list, BLANCO: list, NEGRO: list) -> int:
	# Precondición: 
	assert(numPartidas >= 0 and 0 <= ultimoGanador <= 2 and filas >= 0 and columnas >= 0)

	# Inicializa el tablero y los valores necesarios para poder jugar
	print("Inicializa el tablero y los valores necesarios para poder jugar")

	inicializarTablero(filas, columnas, tablero)
	dibujarTablero(BLANCO, NEGRO)
	dificultad = escogerDificultad()
	jugador = definirPrimero(numPartidas, ultimoGanador)

	# Inicializa las variables para la partida
	numJugadas = 0
	numJugadasPC = 0
	ultimaJugada = [-1,-1]

	# Postcondición: 
	assert(all ( all (tablero[i][j] == 0 for i in range(filas)) for j in range(columnas)) and 0 <= dificultad <= 1 and 
		(numPartidas != 0 or jugador == 1) and (numPartidas == 0 or jugador == ultimoGanador))

	return dificultad, jugador, numJugadas, numJugadasPC

def inicializarTablero(filas: int,columnas: int,tablero: list) -> 'void':

	# Precondición: 
	assert(filas >= 4 and columnas >= 4)

	print("Inicializa el tablero de manera que esté vacío")

	# Inicializa el tablero de manera que esté vacío

	# VAR
	# 	i: int;							# Variable auxiliar para iterar
	# 	j: int;							# Variable auxiliar para iterar

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

def escogerDificultad() -> (int):
	# Se le solicita al usuario que ingrese la dificultad de la partida que va a jugar. Siendo 0 para básico y 1 para medio.

	# Precondición: 
	assert(True)
	
	print("Se solicita al usuario que ingrese una dificultad hasta que ingrese una correctamente.")

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

	return dificultad

def definirPrimero(numPartidas: int, ultimoGanador: int) -> (int):
	# Precondición: 
	assert(numPartidas >= 0 and 0 <= ultimoGanador <= 2)

	# Función que devuelve el primer jugador dependiendo de la partida en que se encuentren.
	print("Función que devuelve el primer jugador dependiendo de la partida en que se encuentren.")

	# VAR 
	# 	primerJugador: int;					# Variable que almacena quien sera el primer jugador de cada partida

	if numPartidas == 0:
		primerJugador = 1
	else:
		primerJugador = ultimoGanador

	# Postcondición: 
	assert((numPartidas != 0 or primerJugador == 1) and (numPartidas == 0 or primerJugador == ultimoGanador))

	return primerJugador

def obtenerJugada(filas: int, columnas: int, numJugadasPC: int, tablero: int, ultimaJugada: list, jugador: int, dificultad: int, estrategia: int) -> (int, int):
	
	# Precondición: 
	assert(columnas >= 4 and 1 <= jugador <= 2 and 0 <= dificultad <= 1)
	print("Verifica quien debe ingresar la jugada y la obtiene")

	if jugador == 2:
			# Verifica la dificultad
		if dificultad == 0:
			# Jugada aleatoria
			jugada = randomJugadaPC(columnas)
		
		elif dificultad == 1:
			# Busca una jugada con una estrategia
			jugada, estrategia = jugadaPC(filas, columnas, numJugadasPC, tablero, ultimaJugada, estrategia)
	
	elif jugador == 1: # Turno del jugador
		jugada = jugadaPersona(columnas)

	return jugada, estrategia

	# Postcondición: 0 <= jugada <= columnas }
	# Devuelve la columna donde se desea jugar

def jugadaPersona(columnas: int) -> int:
	# VAR:
	# Columnas: int 	# Número de columnas del tablero, la jugada no puede estar fuera del rango [0,columnas).

	print("Solicita entrada de una jugada válida a la persona hasta que se introduzca una correctamente.")

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
	print("Valida que la jugada sea válida")

	# VAR		
	# 	i: int;								# Variable auxiliar para iterar

	i = filas - 1

	validacion = False
	
	# Cota:
	cota = i + 1
	assert(cota >= 0)

	while i != -1:
		if tablero[i][jugada] == 0:
			validacion = True

		i = i - 1

		# Verificacion de cota estrictamente decreciente.
		assert(cota > i)

		cota = i + 1

		# Verificacion de cota acotada por 0.
		assert(cota >= 0)

	# Postcondición: 
	assert(any (tablero[i][jugada] == 0 for i in range(filas)) == validacion)

	return validacion

def reflejarJugada(jugada: int, jugador: int, filas: int, columnas:int, tablero: list, ultimaJugada: list, numJugadasPC: int) -> 'void':
	# Precondición: 
	assert(1 <= jugador <= 2 and 0 <= jugada < columnas and filas >= 4 and columnas >= 4)

	# Guarda una jugada en el tablero
	print("Guarda la jugada en el tablero")

	# VAR
	# 	i: int;								# Variable auxiliar para iterar
	#	continua: boolean;					# Variable auxiliar para finalizar el ciclo y evitar seguir modificando el tablero

	i = filas - 1
	continua = True

	# Cota:
	cota = i + 1
	assert(cota >= 0)

	while i != -1 and continua == True:
		if tablero[i][jugada] == 0:
			tablero[i][jugada] = jugador
			if jugador == 2:
				ultimaJugada = [i,jugada]
				numJugadasPC = numJugadasPC + 1
				dibujarJugada(i, jugada, AZUL)
			else:
				dibujarJugada(i, jugada, ROJO)
			continua = False
			pygame.display.flip()
				
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
	print("Pasa el turno al siguiente jugador")

	if jugador == 1:
		jugador = 2
	elif jugador == 2:
		jugador = 1

	# Postcondición: 
	assert(jugador == 1 or jugador == 2)

	return jugador

def verificar4enLinea(filas: int, columnas: int, tablero: list) -> 'void':
	# Precondicion: 
	assert(filas >= 4 and columnas >= 4 and 
			all ( all (0 <= tablero[i][j] <= 2 for j in range(columnas)) for i in range(filas)))

	# Verifica si alguno de los jugadores realizó un 4 en línea
	print("Verifica si alguno de los jugadores realizó un 4 en línea")
	
	# VAR
	# 	ganadores: array[0,4) of int;							# Arreglo utilizado para verificar si se cumple alguna de las verificaciones de 4 en linea
	# 	i: int;													# Variable auxiliar para iterar

	continuar = True
	ganador = 0
	ganadores = [verificarHorizontal(filas, columnas, tablero), verificarVertical(filas, columnas, tablero), verificarDiagonalDerecha(filas, columnas, tablero), verificarDiagonalIzquierda(filas, columnas, tablero)]

	i = 0

	# Cota 
	cota = 4 - i
	# Verificacion de cota acotada por 0.
	assert(cota >= 0)

	while i != 4:
		if ganadores[i] != 0:
			ganador = ganadores[i]
			continuar = False
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
	print("Verifica si existe una linea horizontal")

	# VAR
	# 	i: int;													# Variable auxiliar para iterar
	# 	j: int;													# Variable auxiliar para iterar
	# 	hay4enLinea: boolean;									# Variable que determina si hay 4 en linea
	# 	ganador: int;											# Variable que al almacena el ganador de la partida actual, (en caso de ser distinto de 0)

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

		while j != columnas - 3 and ganador == 0:

			if (tablero[i][j] == tablero[i][j+1] == tablero[i][j+2] == tablero[i][j+3]) and tablero[i][j] != 0:
				ganador = tablero[i][j];
				resaltarGanador(i, j, AMARILLO)
				resaltarGanador(i, j+1, AMARILLO)
				resaltarGanador(i, j+2, AMARILLO)
				resaltarGanador(i, j+3, AMARILLO)
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
	# 	i: int;													# Variable auxiliar para iterar
	# 	j: int;													# Variable auxiliar para iterar
	# 	hay4enLinea: boolean;									# Variable que determina si hay 4 en linea
	# 	ganador: int;											# Variable que al almacena el ganador de la partida actual, (en caso de ser distinto de 0)

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

		while j != filas - 3 and ganador == 0:

			if (tablero[j][i] == tablero[j+1][i] == tablero[j+2][i] == tablero[j+3][i]) and tablero[j][i] != 0:
				ganador = tablero[j][i]
				resaltarGanador(j, i, AMARILLO)
				resaltarGanador(j+1, i, AMARILLO)
				resaltarGanador(j+2, i, AMARILLO)
				resaltarGanador(j+3, i, AMARILLO)
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
	# 	i: int;													# Variable auxiliar para iterar
	# 	j: int;													# Variable auxiliar para iterar
	# 	hay4enLinea: boolean;									# Variable que determina si hay 4 en linea
	# 	ganador: int;											# Variable que al almacena el ganador de la partida actual, (en caso de ser distinto de 0)

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

		while j != columnas - 3 and ganador == 0:
			if (tablero[i][j] == tablero[i+1][j+1] == tablero[i+2][j+2] == tablero[i+3][j+3]) and tablero[i][j] != 0:
				ganador = tablero[i][j]
				resaltarGanador(i, j, AMARILLO)
				resaltarGanador(i+1, j+1, AMARILLO)
				resaltarGanador(i+2, j+2, AMARILLO)
				resaltarGanador(i+3, j+3, AMARILLO)
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
	# 	i: int;													# Variable auxiliar para iterar
	# 	j: int;													# Variable auxiliar para iterar
	# 	hay4enLinea: boolean;									# Variable que determina si hay 4 en linea
	# 	ganador: int;											# Variable que al almacena el ganador de la partida actual, (en caso de ser distinto de 0)

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

		while j != filas - 3 and ganador == 0:
			if (tablero[j][i] == tablero[j+1][i-1] == tablero[j+2][i-2] == tablero[j+3][i-3]) and tablero[j][i] != 0:
				ganador = tablero[j][i]
				resaltarGanador(j, i, AMARILLO)
				resaltarGanador(j+1, i-1, AMARILLO)
				resaltarGanador(j+2, i-2, AMARILLO)
				resaltarGanador(j+3, i-3, AMARILLO)
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
	# 	continuar: boolean;								# Variable que determina si la partida ha finalizado o no

	if numJugadas == filas * columnas:
		continuar = False
	else:
		continuar = True

	# Postcondición: 
	assert((numJugadas != filas * columnas or continuar == False) and (numJugadas == filas * columnas or continuar == True))
	
	return continuar

def jugadaPC(filas: int, columnas: int, numJugadasPC: int, tablero: int, ultimaJugada: list, estrategia: int) -> int:

	# Inteligencia Artificial del computador
	# Toma una estrategia y la sigue mientras sea posible, en caso de no serlo
	# En caso de que el jugador tenga una fila vertical de 3 fichas, la tranca
	# toma una nueva estrategia aleatoriamente.

	print("Genera una jugada que tenga cierto nivel de dificultad.")

	# CONST
	# 	intentosMaximos: int;									# Numero maximo de intentos que puede hacer la computadora de intentar con varias estrategias antes de jugar random 

	# VAR
	# 	puedeJugar: boolean;									# Variable que determina si las estrategias comprobadas pueden llevarse a cabo
	# 	estrategia: int;										# Variable que almacena la estrategia a llevar a cabo por la computadora
	# 	jugada: int;											# Variable que almacena la columna en la que se desea jugar	
	# 	i: int;													# Variable auxiliar para realizar la iteracion
		
	# Precondición: 
	assert(filas >= 4 and columnas >= 4 and numJugadas >= 0 and 
		all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))
	
	intentosMaximos = 50
	puedeJugar = False
	i = 0

	if numJugadasPC == 0:
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

			if jugada == -1:
				jugada = randomJugadaPC(columnas)
	return jugada, estrategia

	# Postcondición: 
	assert(0 <= jugada < columnas)


def compruebaJugadaVertical(ultimaJugada: list, tablero: list, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
		     (all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas))))
	
	# Verifica si puede jugar en la casilla de arriba
	print("Verifica si puede jugar en la casilla de arriba")

	if ultimaJugada[0] != 0:
		if tablero[ultimaJugada[0] - 1][ultimaJugada[1]] == 0:
			jugada = ultimaJugada[1]
			puedeJugar = True
		else:
			jugada = -1
			estrategia = randomEstrategia()
			puedeJugar = False
	else:
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
	print("Verifica si puede jugar en la casilla de la derecha")
	if ultimaJugada[1] != columnas - 1:
		if tablero[ultimaJugada[0]][ultimaJugada[1] + 1] == 0:
			if ultimaJugada[0] != filas - 1:
				if tablero[ultimaJugada[0] + 1][ultimaJugada[1] + 1] != 0:			
					jugada = ultimaJugada[1] + 1
					puedeJugar = True
				else:
					jugada = -1
					estrategia = randomEstrategia()
					puedeJugar = False
			else:
				jugada = ultimaJugada[1] + 1
				puedeJugar = True
		else:
			jugada = -1
			estrategia = randomEstrategia()
			puedeJugar = False
	else:
		jugada = -1
		estrategia = randomEstrategia()
		puedeJugar = False

	# Postcondición: 
	# assert((ultimaJugada[1] == columnas - 1 or (( tablero[ultimaJugada[0]][ultimaJugada[1] + 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] + 1)) and
	#  		(tablero[ultimaJugada[0]][ultimaJugada[1] + 1] == 0 or (puedeJugar == False and jugada == -1)))) and (ultimaJugada[1] != columnas - 1 or (jugada == -1 and puedeJugar == False)))

	return jugada, puedeJugar, estrategia

def compruebaJugadaHorizontalIzquierda(ultimaJugada: list, tablero: list, columnas: int, filas: int, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	 		 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si puede jugar en la casilla de la izquierda
	print("Verifica si puede jugar en la casilla de la izquierda")

	if ultimaJugada[1] != 0:
		if tablero[ultimaJugada[0]][ultimaJugada[1] - 1] == 0:
			if ultimaJugada[0] != filas - 1:
				if tablero[ultimaJugada[0] + 1][ultimaJugada[1] - 1] != 0:			
					jugada = ultimaJugada[1] - 1
					puedeJugar = True
				else:
					jugada = -1
					estrategia = randomEstrategia()
					puedeJugar = False
			else:
				jugada = ultimaJugada[1] - 1
				puedeJugar = True
		else:
			jugada = -1
			estrategia = randomEstrategia()
			puedeJugar = False
	else:
		jugada = -1
		estrategia = randomEstrategia()
		puedeJugar = False

	# Postcondición: 
	# assert((ultimaJugada[1] == 0 or (( tablero[ultimaJugada[0]][ultimaJugada[1] - 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] - 1)) and
	#   		(tablero[ultimaJugada[0]][ultimaJugada[1] - 1] == 0 or (puedeJugar == False and jugada == -1)))) and (ultimaJugada[1] != 0 or (jugada == -1 and puedeJugar == False)))

	return jugada, puedeJugar, estrategia


def compruebaJugadaDiagonalDerechaAbajo(ultimaJugada: list, tablero: list, columnas:int, filas:int, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	   	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si puede jugar en la casilla inferior derecha
	print("Verifica si puede jugar en la casilla inferior derecha")

	if ultimaJugada[0] == filas - 1 or ultimaJugada[1] == columnas - 1:
		jugada = -1
		estrategia = randomEstrategia()
		puedeJugar = False
	else:
		if tablero[ultimaJugada[0] + 1][ultimaJugada[1] + 1] == 0:
			if ultimaJugada[0] != filas - 2:
				if tablero[ultimaJugada[0] + 2][ultimaJugada[1] + 1] != 0:
					jugada = ultimaJugada[1] + 1
					puedeJugar = True
				else:
					jugada = -1
					estrategia = randomEstrategia()
					puedeJugar = False
			else:
				jugada = ultimaJugada[1] + 1
				puedeJugar = True
		else:
			jugada = -1
			estrategia = randomEstrategia()
			puedeJugar = False

	# Postcondición: 
	# assert(((ultimaJugada[0] == filas - 1 or ultimaJugada[1] == columnas - 1 ) or (( tablero[ultimaJugada[0] + 1][ultimaJugada[1] + 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] + 1)) and
	# 		 (tablero[ultimaJugada[0] + 1][ultimaJugada[1] + 1] == 0 or (puedeJugar == False and jugada == -1)))) and ((ultimaJugada[0] != filas - 1 and ultimaJugada[1] != columnas -1) or (jugada == -1 and puedeJugar == False)))

	return jugada, puedeJugar, estrategia

def compruebaJugadaDiagonalIzquierdaArriba(ultimaJugada: list, tablero: list, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	   	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si puede jugar en la casilla superior izquierda
	print("Verifica si puede jugar en la casilla superior izquierda")
	
	if ultimaJugada[0] == 0 or ultimaJugada[1] == 0:
		jugada = -1
		estrategia = randomEstrategia()
		puedeJugar = False
	else:
		if tablero[ultimaJugada[0] - 1][ultimaJugada[1] - 1] == 0:
			if tablero[ultimaJugada[0]][ultimaJugada[1] - 1] != 0:
				jugada = ultimaJugada[1] - 1
				puedeJugar = True
			else:
				jugada = -1
				estrategia = randomEstrategia()
				puedeJugar = False	
		else:
			jugada = -1
			estrategia = randomEstrategia()
			puedeJugar = False

	# Postcondición: 
	# assert(((ultimaJugada[0] == 0 or ultimaJugada[1] == 0 ) or (( tablero[ultimaJugada[0] - 1][ultimaJugada[1] - 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] - 1)) and
	# 		 (tablero[ultimaJugada[0] - 1][ultimaJugada[1] - 1] == 0 or (puedeJugar == False and jugada == -1)))) and ((ultimaJugada[0] != 0 and ultimaJugada[1] != 0) or (jugada == -1 and puedeJugar == False)))

	return jugada, puedeJugar, estrategia

def compruebaJugadaDiagonalIzquierdaAbajo(ultimaJugada: list, tablero: list, filas:int, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	   	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si puede jugar en la casilla inferior izquierda
	print("Verifica si puede jugar en la casilla inferior izquierda")

	if ultimaJugada[0] == filas - 1 or ultimaJugada[1] == 0:
		jugada = -1
		estrategia = randomEstrategia()
		puedeJugar = False
	else:
		if tablero[ultimaJugada[0] + 1][ultimaJugada[1] - 1] == 0:
			if ultimaJugada[0] != filas - 2:
				if tablero[ultimaJugada[0] + 2][ultimaJugada[1] - 1] != 0:
					jugada = ultimaJugada[1] - 1
					puedeJugar = True
				else:
					jugada = -1
					estrategia = randomEstrategia()
					puedeJugar = False
			else:
				jugada = ultimaJugada[1] - 1
				puedeJugar = True
		else:
			jugada = -1
			estrategia = randomEstrategia()
			puedeJugar = False

	# Postcondición: 
	# assert(((ultimaJugada[0] == filas - 1 or ultimaJugada[1] == 0 ) or (( tablero[ultimaJugada[0] + 1][ultimaJugada[1] - 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] - 1)) and
	# 		 (tablero[ultimaJugada[0] + 1][ultimaJugada[1] - 1] == 0 or (puedeJugar == False and jugada == -1)))) and ((ultimaJugada[0] != filas - 1 and ultimaJugada[1] != 0) or (jugada == -1 and puedeJugar == False)))

	return jugada, puedeJugar, estrategia

def compruebaJugadaDiagonalDerechaArriba(ultimaJugada: list, tablero: list, columnas: int, estrategia: int) -> (int, bool, int):
	# Precondición: 
	assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	   	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))

	# Verifica si puede jugar en la casilla superior derecha
	print("Verifica si puede jugar en la casilla superior derecha ")

	if ultimaJugada[0] == 0 or ultimaJugada[1] == columnas - 1:
		jugada = -1
		estrategia = randomEstrategia()
		puedeJugar = False
	else:
		if tablero[ultimaJugada[0] - 1][ultimaJugada[1] + 1] == 0:
			if tablero[ultimaJugada[0]][ultimaJugada[1] + 1] != 0:
				jugada = ultimaJugada[1] + 1
				puedeJugar = True
			else:
				jugada = -1
				estrategia = randomEstrategia()
				puedeJugar = False
		else:
			jugada = -1
			estrategia = randomEstrategia()
			puedeJugar = False

	# Postcondición: 
	# assert(((ultimaJugada[0] == 0 or ultimaJugada[1] == columnas - 1 ) or (( tablero[ultimaJugada[0] - 1][ultimaJugada[1] + 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] + 1)) and
	# 	 (tablero[ultimaJugada[0] - 1][ultimaJugada[1] + 1] == 0 or (puedeJugar == False and jugada == -1)))) and ((ultimaJugada[0] != 0 and ultimaJugada[1] != columnas -1) or (jugada == -1 and puedeJugar == False)))

	return jugada, puedeJugar, estrategia

def randomEstrategia() -> int:

	print("Devuelve una estrategia aleatoria.")
	
	# Precondición: 
	assert(True)
	
	estrategia = random.randrange(7)
	print("Estrategia seleccionada: " + str(estrategia))
	
	# Postcondición: 
	assert(0 <= estrategia < 7)

	return estrategia 

def randomJugadaPC(columnas: int) -> int:
	# Precondición:
	assert(True)
	print("Devuelve una columna aleatoriamente para generar la jugada de la computadora.")

	jugada = random.randrange(columnas)
	print("Columna seleccionada: " + str(jugada))

	# Postcondición
	assert(0 <= jugada < columnas)

	return jugada

def dibujarTablero(colorlineas: list, colorfondo: list) -> 'void':
	# Precondición: 
	assert(True)
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

	pygame.display.flip()

	print("Se dibuja el tablero en la interfaz gráfica")
	# Postcondición: 
	# se dibuja en una ventana gráfica un tablero con "filas" filas y "columnas" columnas de color "color"

def dibujarJugada(i: int, jugada: int, color: list) -> 'void':
	# Precondición: 
	assert(True)
	print("Dibuja en el tablero la jugada luego de haberla reflejado en la matriz")
	pygame.draw.circle(pantalla, color, (201 + jugada*142, 134 + i*88), 30, 0)
	# Postcondición: 
	# Se dibuja un circulo de color "color" en la casilla posicionada en la fila "i" y columna "jugada" del tablero

def resaltarGanador(i: int, j: int, color: list) -> 'void':
	# Precondición: 
	assert(True)
	print("Resalta las fichas que se encuentran en 4 en linea")
	pygame.draw.circle(pantalla, color, (201 + j*142, 134 + i*88), 25, 0)
	pygame.display.flip()

	# Postcondición: 
	# Se resalta el circulo de la casilla posicionada en la fila "i" y columna "j" del tablero de color "color" }

def pedirNombre() -> str:
	# Solicita el nombre del jugador.
	# Precondicion:
	assert(True)

	nombre = str(input("Por favor, ingrese su nombre: "))
	print("Hola "+ nombre)

	# Postcondicion:
	assert(True)

	return nombre

# Precondición:
# assert(filas>=4 and columnas >= 4 and maxPartidas >= 0)0


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
FPS = 60                 # Cuadros por segundo

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
nombre = pedirNombre()
estrategia = -1

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
				dificultad, jugador, numJugadas, numJugadasPC = inicializarPartida(numPartidas, ultimoGanador, filas, columnas, tablero, BLANCO, NEGRO)
				
				# Cota: 
				# assert(filas * columnas - numJugadas)
				while continuar == True and numJugadas != filas * columnas:
					
					ingresaJugada = True
					# Cota: No tiene, la iteracion se hará hasta que la jugada sea correcta
					while ingresaJugada == True:
						
						# Obtiene los valores de la jugada y verifica que sea correcto
						jugada, estrategia = obtenerJugada(filas, columnas, numJugadasPC, tablero, ultimaJugada, jugador, dificultad, estrategia)
						validacion = validarJugada(jugada, filas, columnas, tablero)

						if validacion == True:

							# Si la jugada se puede realizar, se almacena en el tablero.
							ultimaJugada, numJugadasPC = reflejarJugada(jugada, jugador, filas, columnas, tablero, ultimaJugada, numJugadasPC)
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
									continuar = seguirPartida()
									if continuar == False:
										partidasGanadasPC = partidasGanadasPC + 1
										numPartidas = numPartidas + 1
										ganador = 2
										ultimoGanador = ganador

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


				# Muestra el ganador de la partida
				entregaGanadorPartida(ganador)

				# Pregunta si se desea jugar otra partida
				quiereSeguirJugando = quiereSeguir()

			# Entrega los resultados finales de la partida
			entregaResultados(partidasGanadasPersona, partidasGanadasPC, numEmpates)
			sys.exit()
			pygame.quit()

			# assert(Postcondición: numPartidas >= 0 and partidasGanadasPersona >=0 and partidasGanadasPC >= 0 and quiereSeguirJugando == False)