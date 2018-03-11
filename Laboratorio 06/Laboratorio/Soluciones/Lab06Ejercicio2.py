#
# Lab6Ejercicio2.py
#
# DESCRIPCION: programa que dado un arreglo A de N numeros naturales 
# produce otro arreglo F lleno con los numeros de Fibonacci de los valores de A
#
# Autor: 
#	Rosseline Rodriguez
#
# Ultima modificacion: 10/03/2018

def leerArreglo(N) -> [int]:
# PARAMETROS N: int // tamanio del arreglo
   
   while True:
      # Precondicion
      S = [ int(input("S[" + str(i) + "]=" )) for i in range(0,N) ] 
      try:
         assert( all (S[i] >= 0 for i in range(0,N)) ) 
         break
      except:
         print("Todos los valores deben ser positivos o 0 ")
         print("Vuelva a intentar")

   return S

def imprimirArreglos(N,A,F) -> 'void':
# PARAMETROS N: int                 // tamanio del arreglo
#            A: array [0..N) of int // arreglo a imprimir
#            F: array [0..N) of int // arreglo a imprimir
   print("Los numero de fibonacci son:")
   for i in range(0,N):
      print("Fib("+str(A[i])+")="+str(F[i]))
   

def fib(n) -> int:
# PARAMETROS n: int                 // tamanio del arreglo

   # Precondicion: 
   assert(n >= 0)

   # VARIABLES
   #  fk: int   // fib(k)
   #  fk_1: int // fib(k-1)
   #  k: int    // variable de control del ciclo

   if n == 0 :
      fk = 0
   elif n == 1 : 
      fk = 1
   else: 
      fk,fk_1 = 1,0

      #inv: 1<=k<=N and fk contiene el fibonacci de k
      #cota = n-i
      for k in range(1,n):
        fk,fk_1 = fk + fk_1,fk 
        k = k+1	
   
   # Post:  fib devuelve el numero de fibonacci de n 

   return fk
   

def llenarconFib(N,A) -> [int]:
# PARAMETROS N: int                 // tamanio del arreglo
#            A: array [0..N) of int // arreglo con valores 

   # Precondicion: 
   assert(N >= 0)

   # VARIABLE
   #  k: int                 // variable de control del ciclo
   #  F: array [0..N) of int // arreglo para el resultado 

   F = [ 0 for i in range(0,N)]

   # cota: N-k
   for k in range (0,N): 
     # invariante:
     assert(0<=k<=N and all((F[i] == fib(A[i])) for i in range(0,k)))

     F[k] = fib(A[k])

   # Postcondicion: 
   assert (all((F[i] == fib(A[i])) for i in range(0,N)) )
   return F
   

# PROGRAMA PRINCIPAL
   
# Variables: 
#    N : int                 // ENTRADA: tamanio de la secuencia
#	 A: array [0..N) of int  // ENTRADA: valores a calcular el fibonacci
#	 F: array [0..N) of int  // SALIDA: fibonacci de todos los valores de A
	 
	 
# Valores iniciales:
print("Diga el tamanio del arreglo:")

while True:
  try:
    N = int(input('N = '))
	
	# Precondicion:
    assert( N > 0 )
    break
  except:
    print("N debe ser positivo ")
    print("Vuelva a intentar")

A = leerArreglo(N)

# Calculos
F = llenarconFib(N,A)

# Postcondicion:	  
assert(all( (F[i] == fib(A[i])) for i in range(0,N) ) )

# Salida:
imprimirArreglos(N,A,F)

