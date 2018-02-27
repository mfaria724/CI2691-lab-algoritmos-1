#
# Prelab4Ejercicio2.py
#
# Descripcion: programa que lee los elementos de un arreglo 
#              y calcula la suma de ellos
#
# Autor:
#        Rosseline Rodriguez
#
# Ultima modificacion: 06/02/2018

# Variables: 
#     N : int                 // ENTRADA: tamanio del arreglo
#     A: array [0..N) of int  // ENTRADA: elementos del arreglo
#     suma : int              // SALIDA: suma de los elementos del arreglo
#     k : int                 // variable de control del ciclo

# Valores iniciales:
N = int(input("Introduzca un entero positivo: "))

# Precondicion:
assert( N > 0 )

# Inicialización del arreglo A
A = [ int(input("A[" + str(i) + "]= ")) for i in range(0,N) ]

# Calculos:
suma,k = 0,0

# Cota: N-k

for k in range(0,N):
  # Verificacion de invariante en cada iteracion
  assert ( suma == sum( A[i] for i in range(0,k) ) )

  suma = suma + A[k]

# Postcondicion:
assert ( suma == sum( A[i] for i in range(0,N) ) )

# Salida:
print( "La suma de los elementos de A es: ",suma )

