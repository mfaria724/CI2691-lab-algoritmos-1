#
# Prelab4Ejercicio4.py
#
# Descripcion: programa que dada una matriz cuadrada NxN, 
#              calcula si la matriz es diagonal
#
# Autor:
#        Rosseline Rodriguez
#
# Ultima modificacion: 06/02/2018

# Variables: 
#     N : int                        // ENTRADA: dimension de la matriz
#     M: array [0..N)x[0..N) of int  // ENTRADA: elementos del arreglo
#     esDiagonal : int               // SALIDA: dice si la matriz es diagonal
#     f : int                        // variable de control del ciclo externo
#     c : int                        // variable de control del ciclo interno

# Valores iniciales:
N = int(input("Introduzca la dimension de la matriz: "))

# Precondicion:
assert( N > 0 )

# Inicialización de la matriz M
M = [ [int(input("M["+str(i)+","+str(j)+"]=")) for j in range(0,N)] for i in range(0,N)]

# Calculos:
diagonal,f = True,0

# Cota: N-f
for f in range(0,N):
  # Verificacion de invariante en cada iteracion
  assert ( diagonal == all( all ( M[i][j]==0 for j in range(0,N) if i!=j ) for i in range(0,f))  )

  c = 0
  # Cota: N-c
  for c in range(0,N):
     # Verificacion de invariante en cada iteracion
     assert ( 
	    diagonal == (
		   all( all ( M[i][j]==0 for j in range(0,N) if i!=j ) for i in range(0,f)) and 
		   all ( M[f][j]==0 for j in range(0,c) if j!=f )
		) 
     )
     if (f!=c and M[f][c] != 0):
        diagonal = False

# Postcondicion:
assert ( diagonal == all( all ( M[i][j]==0 for j in range(0,N) if i!=j ) for i in range(0,N)) )

# Salida:
print( "La matriz es diagonal?",diagonal )

