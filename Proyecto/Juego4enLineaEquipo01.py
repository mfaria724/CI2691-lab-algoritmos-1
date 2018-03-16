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
# 		filas:int;													# Numero de filas del tablero
# 		columnas: int;												# Numero de columnas del table
# 		maxPartidas: int;											# Numero maximo de partidas a jugar
# 	VAR
# 		tablero: list [0,filas) x [0,columnas) of int;				# Tablero de juego
# 		dificultad: int;											# Variable que almacena la dificultad seleccionada por el jugador (0 basico, 1 medio)
# 		ultimoGanador: int;											# Variable que almacena el ganador de la partida anterior
# 		jugador: int;												# Variable que almacena el jugador del turno actual
# 		numPartidas: int;											# Variable que almacena la cantidad de partidas jugadas
# 		jugada: int;												# Variable que almacena la columna donde se desea jugar
# 		ultimaJugada: list;										# Variable que almacena la fila y columna de la ultima jugada de la computadora
# 		continuar: bool;											# Variable que determina si una partida ha finalizado o no
# 		numJugadas: int;											# Variable que almacena el numero de jugadas de la partida actual
# 		numJugadasPC: int;											# Variable que almacena el numero de jugadas de la computadora en la partida actual
# 		numEmpates: int;											# Variable que almacena el numero de empates de todos los juegos
# 		partidasGanadasPersona: int;								# Variable que almacena la cantidad de veces que gana el jugador
# 		partidasGanadasPC: int;										# Variable que almacena la cantidad de veces que gana la computadora
# 		ganador: int;												# Variable que almacena el ganador de la partida actual
# 		validacion: bool;										# Variable que determina si una jugada es valida o no
# 		quiereSeguirJugando: bool;								# Variable que determina si el usuario desea jugar otra partia o no
# 		ingresaJugada: bool;										# Variable utilizada en el ciclo de cada jugada para en caso de no ser valida, poder ingresar otra jugada


def seguirPartida() -> bool:
	# Precondición: 
	# assert(True)
	print("Le pregunta al usuario si quiere seguir con la partida")
	# Postcondición:
	# El jugador ingresa si desea continuar la partida actual o no

def entregaResultados(partidasGanadasPersona: int, partidasGanadasPC: int, numEmpates: int) -> 'void':
	# Precondición: 
	# assert(partidasGanadasPersona >= 0 and partidasGanadasPC >= 0 and numEmpates >= 0)
	print("Se imprime la cantidad de partidas ganadas por el Jugador, PC y numero de empates")
	# Postcondición: 
	# Se imprime la cantidad de partidas ganadas por el Jugador, PC y numero de empates

def entregaGanadorPartida(ganador: int) -> 'void':
	# Precondición: 
	# assert(1 <= ganador <= 2)
	print("Entrega los resultados de la partida que acaba de finalizar")
	# Postcondición: 
	# Se imprime el ganador de la partida en pantalla

def quiereSeguir() -> bool:
	# Precondición: 
	# assert(True)
	print("El jugador ingresa si desea jugar otra partida")
	# Postcondición: 
	# assert(True)

def inicializarPartida(numPartidas: int, ultimoGanador: int, filas: int, columnas: int,tablero: list, numJugadas: int, 
						jugador: int, numJugadasPC: int, ultimaJugada: int) -> 'void':
	# Precondición: 
	# assert(numPartidas >= 0 and 0 <= ultimoGanador <= 2 and filas >= 0 and columnas >= 0)
	print("Inicializa el tablero y los valores necesarios para poder jugar")
	# Postcondición: 
	# assert(all ( all (tablero[i][j] == 0 for i in range(filas)) for j in range(columnas)) and 0 <= dificultad <= 1 and 
	#		(numPartidas != 0 or primerJugador == 1) and (numPartidas == 0 or primerJugador == ultimoGanador))

def inicializarTablero(filas: int,columnas: int,tablero: list) -> 'void':

	# Precondición: 
	# assert(filas >= 4 and columnas >= 4)
	print("Inicializa el tablero de manera que esté vacío")
	# Postcondición: 
	# assert(all ( all (tablero[i][j] == 0 for i in range(filas)) for j in range(columnas)))

def dificultad() -> (int):
	# Precondición: 
	# assert(True)
	print("El usuario ingresa la dificultad")
	# Postcondición: 0 <= dificultad <= 1 }
	# Dificultad ingresada por el usuario

def definirPrimero(numPartidas:int, ultimoGanador: int) -> (int):
	# Precondición: 
	# assert(numPartidas >= 0 and 0 <= ultimoGanador <= 2)
	print("Función que devuelve el primer jugador dependiendo de la partida en que se encuentren")
	# Postcondición: 
	# assert(numPartidas != 0 or primerJugador == 1) and (numPartidas == 0 or primerJugador == ultimoGanador)

def obtenerJugada(filas: int, columnas: int, tablero: int, ultimaJugada: list, jugador: int, dificultad: int) -> int:
	# Precondición: 
	# assert(columnas >= 4 and 1 <= jugador <= 2 and 0 <= dificultad <= 1)
	print("Verifica quien debe ingresar la jugada y la obtiene")
	# Postcondición: 0 <= jugada <= columnas }
	# Devuelve la columna donde se desa jugar

def validarJugada(jugada: int, filas: int, columnas: int, tablero: list,validacion: bool,
				   ultimaJugada: list) -> 'void':
	# Precondición: 
	# assert(0 <= jugada < columnas and filas >= 4 and columnas >= 4)
	# Postcondición: 
	print("Valida que la jugada sea válida")
	# assert(any (tablero[i][jugada] == 0 for i in range(filas) == validacion))
	# Verifica si una jugada es posible o no

def reflejarJugada(jugada: int, jugador: int, filas: int, columnas:int,tablero: list) -> 'void':
	# Precondición: 
	# assert(1 <= jugador <= 2 and 0 <= jugada < columnas and filas >= 4 and columnas >= 4)
	print("Guarda la jugada en el tablero")
	# Postcondición: 
	# assert(any (tablero[i][jugada] == jugador for i in range(filas)))

def cambiarTurno(jugador) -> int:
	# Precondición:
	# assert(1 <= jugador <= 2)
	print("Pasa el turno al siguiente jugador")
	# Postcondición: 
	# assert((jugador != 1 or jugador ==2) and (jugador != 2 or jugador == 1))

def verificar4enLinea(filas: int, columnas: int, tablero: list, continuar:bool, ganador:int) -> 'void':
	# Precondicion: 
	# assert(filas >= 4 and columnas >= 4 and 
	#	     all ( all (0 <= tablero[i][j] <= 2 for j in range(columnas)) for i in range(filas)))
	print("Verifica si alguno de los jugadores realizó un 4 en línea")
	# Postcondición: 
	# assert(any (ganadores[i] != 0 and ganador == ganadores[i] for i in range(4) == (continuar == False)))

def verificarHorizontal(filas: int, columnas:int, tablero: list) -> int:
	# Precondición: 
	# assert(filas >= 4 and columnas >= 4 and 
	# 		 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))
	print("Verifica si existe una linea horizontal")
	# Postcondición: 
	# assert(any ( any (tablero[i][j] == tablero[i][j+1] == tablero[i][j+2] == tablero[i][j+3] for i in range(filas)) 
	# 	     for j in range(columnas - 3)) == hay4enLinea)

def verificarVertical(filas: int, columnas:int, tablero: list) -> int:
	# Precondición: 
	# assert(filas >= 4 and columnas >= 4 and 
	# 	     all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(filas - 3)))
	print("Verifica si  existe una linea vertical")
	# Postcondición: 
	# assert(any (any (tablero[j][i] == tablero[j+1][i] == tablero[j+2][i] == tablero[j+3][i] for i in range(columnas)) 
	#		 for j in range(filas - 3)) == hay4enLinea)

def verificarDiagonalDerecha(filas: int, columnas:int, tablero: list) -> int:
	# Precondicion: 
	# assert(filas >= 4 and columnas >= 4 and 
	# 	     all( all(0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))
	print("Verifica si existe una linea diagonal derecha")
	# Postcondición: 
	# assert(any (any (tablero[i][j] == tablero[i+1][j+1] == tablero[i+2][j+2] == tablero[i+3][j+3] for j in range(columnas - 3))
	#  		 for i in range(filas - 3)) == hay4enLinea)

def verificarDiagonalIzquierda(filas: int, columnas:int, tablero: list) -> int:
	# Precondición: 
	# assert(filas >= 4 and columnas >= 4 and 
	#		 all( all(0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))
	print("Verifica si existe una linea diagonal izquierda")
	# Postcondición:
	# assert(any( any(tablero[j][i] == tablero[j+1][i-1] == tablero[j+2][i-2] == tablero[j+3][i-3] for i in range(columnas))
	#		 for j in range(filas - 3)) == hay4enLinea) 

def verificarTablero(numJugadas: int, filas: int, columnas:int) -> bool:
	# Precondición: 
	# assert(filas >= 4 and columnas >= 4 and numJugadas <= filas * columnas)
	print("Verifica si el tablero está lleno")
	# Postcondición: 
	# assert((numJugadas != filas * columnas or continuar == False) and (numJugadas == filas * columnas or continuar == True))

def jugadaPC(filas: int, columnas: int, numJugadasPC: int, tablero: int, ultimaJugada: list) -> int:
	# Precondición: 
	# assert(filas >= 4 and columnas >= 4 and numJugadas >= 0 and 
	#    	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))
	print("Inteligencia Artificial del computador")
	# Postcondición: 
	# assert(0 <= jugada < columnas)


def compruebaJugadaVertical(ultimaJugada: list, tablero: list, jugada:int, puedeJugar:bool, estrategia:int) -> 'void':
	# Precondición: 
	# assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	#	     (all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas))))
	print("Verifica si puede jugar en la casilla de arriba")
	# Postcondición: 
	# assert((ultimaJugada[0] == 0 or (( tablero[ultimaJugada[0] - 1][ultimaJugada[1]] != 0 or (puedeJugar == True and jugada == ultimaJugada[1])) and
	# 	 	 (tablero[ultimaJugada[0] - 1][ultimaJugada[1]] == 0 or (puedeJugar == False and jugada == -1)))) and (ultimaJugada[0] != 0 or (jugada == -1 and puedeJugar == False)))

def compruebaJugadaHorizontalDerecha(ultimaJugada: list, tablero: list, columnas:int, jugada:int, puedeJugar:bool, estrategia:int) -> 'void':
	# Precondición: 
	# assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	#		 all (all (0 <= tablero[i][j] <= 2 for j in range(columnas)) for i in range(filas)))
	print("Verifica si puede jugar en la casilla de la derecha")
	# Postcondición: 
	# assert((ultimaJugada[1] == columnas - 1 or (( tablero[ultimaJugada[0]][ultimaJugada[1] + 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] + 1)) and
	# 		(tablero[ultimaJugada[0]][ultimaJugada[1] + 1] == 0 or (puedeJugar == False and jugada == -1)))) and (ultimaJugada[1] != columnas - 1 or (jugada == -1 and puedeJugar == False)))


def compruebaJugadaHorizontalIzquierda(ultimaJugada: list, tablero: list, jugada:int, puedeJugar:bool, estrategia:int) -> 'void':
	# Precondición: 
	# assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	# 		 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))
	print("Verifica si puede jugar en la casilla de la izquierda")
	# Postcondición: 
	# assert((ultimaJugada[1] == 0 or (( tablero[ultimaJugada[0]][ultimaJugada[1] - 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] - 1)) and
	#  		(tablero[ultimaJugada[0]][ultimaJugada[1] - 1] == 0 or (puedeJugar == False and jugada == -1)))) and (ultimaJugada[1] != 0 or (jugada == -1 and puedeJugar == False)))

def compruebaJugadaDiagonalDerechaAbajo(ultimaJugada: list, tablero: list, columnas:int, filas:int, jugada:int, puedeJugar:bool, estrategia:int) -> 'void':
	# Precondición: 
	# assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	#    	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))
	print("Verifica si puede jugar en la casilla inferior derecha")
	# Postcondición: 
	# assert(((ultimaJugada[0] == filas - 1 or ultimaJugada[1] == columnas - 1 ) or (( tablero[ultimaJugada[0] + 1][ultimaJugada[1] + 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] + 1)) and
	# 		 (tablero[ultimaJugada[0] + 1][ultimaJugada[1] + 1] == 0 or (puedeJugar == False and jugada == -1)))) and ((ultimaJugada[0] != filas - 1 and ultimaJugada[1] != columnas -1) or (jugada == -1 and puedeJugar == False)))

def compruebaJugadaDiagonalDerechaArriba(ultimaJugada: list, tablero: list, jugada:int, puedeJugar:bool, estrategia:int) -> 'void':
	# Precondición: 
	# assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	#    	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))
	print("Verifica si puede jugar en la casilla superior derecha")
	# Postcondición: 
	# assert(((ultimaJugada[0] == 0 or ultimaJugada[1] == 0 ) or (( tablero[ultimaJugada[0] - 1][ultimaJugada[1] - 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] - 1)) and
	# 		 (tablero[ultimaJugada[0] - 1][ultimaJugada[1] - 1] == 0 or (puedeJugar == False and jugada == -1)))) and ((ultimaJugada[0] != 0 and ultimaJugada[1] != 0) or (jugada == -1 and puedeJugar == False)))

def compruebaJugadaDiagonalIzquierdaAbajo(ultimaJugada: list, tablero: list, filas:int, jugada:int, puedeJugar:bool, estrategia:int) -> 'void':
	# Precondición: 
	# assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	#    	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))
	print("Verifica si puede jugar en la casilla inferior izquierda")
	# Postcondición: 
	# assert(((ultimaJugada[0] == filas - 1 or ultimaJugada[1] == 0 ) or (( tablero[ultimaJugada[0] + 1][ultimaJugada[1] - 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] - 1)) and
	# 		 (tablero[ultimaJugada[0] + 1][ultimaJugada[1] - 1] == 0 or (puedeJugar == False and jugada == -1)))) and ((ultimaJugada[0] != filas - 1 and ultimaJugada[1] != 0) or (jugada == -1 and puedeJugar == False)))

def compruebaJugadaDiagonalIzquierdaArriba(ultimaJugada: list, tablero: list, columnas: int, jugada:int, puedeJugar:bool, estrategia:int) -> 'void':
	# Precondición: 
	# assert(0 <= ultimaJugada[0] < filas and 0 <= ultimaJugada[1] < columnas and 
	#    	 all (all (0 <= tablero[i][j] <= 2 for i in range(filas)) for j in range(columnas)))
	print("Verifica si puede jugar en la casilla superior izquierda")
	# Postcondición: 
	# assert(((ultimaJugada[0] == 0 or ultimaJugada[1] == columnas - 1 ) or (( tablero[ultimaJugada[0] - 1][ultimaJugada[1] + 1 ] != 0 or (puedeJugar == True and jugada == ultimaJugada[1] + 1)) and
	#		 (tablero[ultimaJugada[0] - 1][ultimaJugada[1] + 1] == 0 or (puedeJugar == False and jugada == -1)))) and ((ultimaJugada[0] != 0 and ultimaJugada[1] != columnas -1) or (jugada == -1 and puedeJugar == False)))

def randomEstrategia() -> int:
	# Precondición: 
	# assert(True)
	print("Devuelve una estrategia aleatoria")
	# Postcondición: 
	# assert(0 <= estrategia < 4)

def randomjugadaPC() -> int:
	# Precondición:
	# assert(True)
	print("Devuelva una columna aleatoriamente, deben verificar el número de columnas.")	
	# Postcondición
	# assert(0 <= jugada < filas)

def​ dibujarTablero ​ (filas: int, columnas: int, color: color) -> 'void':
	# Precondición: 
	# assert(filas > 0 and columnas > 0)
	print("Se dibuja el tablero en la interfaz gráfica")
	# Postcondición: 
	# se dibuja en una ventana gráfica un tablero con "filas" filas y "columnas" columnas de color "color"

def dibujarJugada(fila: int, columna: int, color: color)
	# Precondición: 
	# assert(filas >= 0 and columnas >= 0)
	print("Dibuja en el tablero la jugada luego de haberla reflejado en la matriz")
	# Postcondición: 
	# Se dibuja un circulo de color "color" en la casilla posicionada en la fila "fila" y columna "columna" del tablero

def resaltarGanador(fila, columna, color)
	# Precondición: 
	# assert(fila >= 0 and columna >= 0)
	print("Resalta las fichas que se encuentran en 4 en linea")
	# Postcondición: 
	# Se resalta el circulo de la casilla posicionada en la fila "fila" y columna "columna" del tablero de color "color" }


# Precondición:
# assert(filas>=4 and columnas >= 4 and maxPartidas >= 0)
	
# Inicialización de variables.
filas = 6
columnas = 7
maxPartidas = 10
numJugadas = 0
numJugadasPC = 0
ultimaJugada = [0,0]
jugador = 0
tablero = [[0]*filas]*columnas
numPartidas = 0
partidasGanadasPC = 0
partidasGanadasPersona = 0
ultimoGanador = 0
numEmpates = 0
quiereSeguirJugando = True
validacion = True
ganador = 0

# Cota: 
# assert(maxPartidas - numPartidas)
while quiereSeguirJugando == True and numPartidas != maxPartidas:

	# Inicializa los valores
	continuar = True
	inicializarPartida(numPartidas, ultimoGanador, filas, columnas, tablero, numJugadas, jugador, numJugadasPC, ultimaJugada)
	
	# Cota: 
	# assert(filas * columnas - numJugadas)
	while continuar == True and numJugadas != filas * columnas:
		
		ingresaJugada = True
		# Cota: No tiene, la se hará hasta que la jugada sea correcta
		while ingresaJugada == True:
			
			# Obtiene los valores de la jugada y verifica que sea correcto
			jugada = obtenerJugada(filas, columnas, tablero, ultimaJugada, jugador, dificultad)
			validarJugada(jugada, filas, columnas, tablero, validacion, ultimaJugada)

			if validacion == True:

				# Si la jugada se puede realizar, se almacena en el tablero.
				reflejarJugada(jugada, jugador, filas, columnas, tablero)
				jugador = cambiarTurno(jugador)
				numJugadas = numJugadas + 1

				# Verifica si existe un ganador
				verificar4enLinea(filas, columnas, tablero, continuar, ganador)
				
				if continuar == True:

					# Si no hay ganador,verifica que el tablero no esté lleno
					continuar = verificarTablero(numJugadas, filas, columnas)

					if continuar == False:
						# Si el tablero está lleno, finaliza la partida y aumenta el conteo de empates
						numEmpates = numEmpates + 1
						numPartidas = numPartidas + 1

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

		# Verifica que quiere continuar con la partida actual
		if jugador == 1:
			# Pregunta al usuario si desea seguir jugando
			continuar = seguirPartida()

	# Muestra el ganador de la partida
	entregaGanadorPartida(ganador)

	# Pregunta si se desea jugar otra partida
	quiereSeguirJugando = quiereSeguir()

# Entrega los resultados finales de la partida
entregaResultados(partidasGanadasPersona, partidasGanadasPC, numEmpates)

# assert(Postcondición: numPartidas >= 0 and partidasGanadasPersona >=0 and partidasGanadasPC >= 0 and quiereSeguirJugando == False)