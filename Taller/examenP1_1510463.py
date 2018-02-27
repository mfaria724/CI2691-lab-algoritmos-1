#
# examenP1_1510463.py
#
# DESCRIPCION: Programa que calcula el máximo de las diagonales principales de una matriz.
#
# Autor: Manuel Faria 15-10463
#
# Ultima modificacion: 27/02/2018
#

# VARIABLES:
#	N: int                        // ENTRADA: número de filas y columnas de la matriz.
#	Mat: array [0,N)x[0,N) of int // ENTRADA: Matriz de valores enteros
# k: int                        // Valor para iterar en el ciclo.
# md1: int                      // Valor que almacena el maximo de la diagonal principal.
# md2: int                      // Valor que almacena el maximo de la diagonal secundaria.
# maxdia: int                   // SALIDA: Valor que almacena el maximo de las dos diagonales.


# Se importa la librería sys para terminar el programa en caso de error
import sys

# Valores iniciales:
N = int(input("Ingrese el número de filas y columnas de la matríz (Debe ser cuadrada)"))
Mat = [ [ int(input("Posición (" + str(i) + "," + str(j) + "): ")) for j in range(0,N) ] for i in range(0,N) ]
k,md1,md2,maxdia=1,Mat[0][0],Mat[0][N-1],Mat[0][0]
	
cota=N-k

# Precondicion: 
assert(N>0)

#Verificacion de invariante al inicio del ciclo
try:
    assert(all( Mat[x][x] <= md1 for x in range(0,k)) and all( Mat[x][N-1-x] <= md2 for x in range(0,k)) and 0<=k<=N)
except:
   print("Error: El invariante no se cumple al inicio del ciclo. El programa terminara ")
   sys.exit()

#Verificacion de la cota positiva al inicio del ciclo
try:
   assert(cota >= 0)
except:
   print("Error: cota negativa. El programa terminara ")
   print("cota="+str(cota))
   sys.exit()


# Calculos:
while k!=N:

    # Diagonal principal
    if Mat[k][k]>md1:
    	md1= Mat[k][k]

    # Diagonal secundaria
    if Mat[k][N-1-k]>md2:
    	md2= Mat[k][N-1-k]

    # Compara diagonales
    if md1>=md2:
    	maxdia=md1
    elif md2>md1:
    	maxdia=md2

    k=k+1

    #Verificacion de invariante en cada iteración
    try:
        assert(all( Mat[x][x] <= md1 for x in range(0,k)) and all( Mat[x][N-1-x] <= md2 for x in range(0,k)) and 0<=k<=N)
    except:
       print("Error: El invariante no se cumple al inicio del ciclo. El programa terminara ")
       sys.exit()

    #Verificacion de la cota positiva en cada iteración
    try:
       assert(cota > N-k)
    except:
       print("Error: cota no decreciente. El programa terminara ")
       print("cota="+str(cota))
       sys.exit()

    cota=N-k

    #Verificacion de la cota decreciente en cada iteración
    try:
       assert(cota >= 0)
    except:
       print("Error: cota negativa. El programa terminara ")
       print("cota="+str(cota))
       sys.exit()

# Postcondicion: 
assert(max (Mat[x][x] for x in range(0,N))==md1 and max (Mat[x][N-1-x] for x in range(0,N))==md2)

# Salida:
print("El máximo de las diagonales es: ")
print(maxdia)