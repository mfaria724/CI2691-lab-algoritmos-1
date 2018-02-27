#
# Lab04Ejercicio2.py
#
# DESCRIPCION: Programa que calcula la suma de todos los elementos
# de una matriz NxM.
#
# Autores: 
#	Saul Hidalgo y Rosseline Rodriguez
#
# Ultima modificacion: 16/02/2018

# Variables:
#   N: int                             // ENTRADA: primera dimension de la matriz
#   M: int                             // ENTRADA: segunda dimension de la matriz
#   matriz: array [0..N)x[0..M) of int // ENTRADA: coeficientes de la matriz
#   suma: int                          // SALIDA: Suma de los elementos
#   f: int                             // Variable de control del ciclo externo
#   c: int                             // Variable de control del ciclo interno0

# Valores iniciales:

print("Programa que suma los elementos de una matriz NxM.")
N = int(input("Indique el N : "))
M = int(input("Indique el M : "))
matriz = [ [ int(input("Posicion (" + str(i) + "," + str(j) + "): ")) for j in range(0,M) ] for i in range(0,N) ]

# Precondicion:
assert( M > 0 and N > 0 )

# Calculos:
suma = 0

# Cota: N-f

for f in range(0,N):
  # Verificacion de invariante en cada iteracion
  assert ( suma == sum( sum( matriz[i][j] for i in range(0,f) ) for j in range (0,M) ) and 0 <= f <= N )

  # Cota: M-c
  for c in range(0,M):
    # Verificacion de invariante en cada iteracion
    assert ( suma == sum( sum( matriz[i][j] for j in range(0,M) ) for i in range (0,f) ) + sum( matriz[f][j] for j in range(0,c) ) 
			 and 0 <= f <= N and 0 <= c <= M )
    
    suma = suma + matriz[f][c]
    

# Postcondicion:
assert ( suma == sum( sum( matriz[i][j] for i in range(0,N) ) for j in range (0,M) ) )

print("La suma de los elementos es: " + str(suma)) 

