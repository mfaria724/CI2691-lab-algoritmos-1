#
# Lab6Ejercicio1.py
#
# DESCRIPCION: programa que determina si una secuencia S de N enteros 
# esta ordenada en forma creciente, decreciente, o está en desorden
#
# Autor: 
#	Rosseline Rodriguez
#
# Ultima modificacion: 10/03/2018

def leerSecuencia(N) -> [int]:
# PARAMETROS N: int // tamanio del arreglo

   S = [ int(input("S[" + str(i) + "]=" )) for i in range(0,N) ] 
   return S

def imprimirOrden(orden) -> 'void':
# PARAMETROS orden: int  // el orden de la secuencia

   if orden == 1:
      print("LA SECUENCIA ES CRECIENTE")
   elif orden == -1:
      print("LA SECUENCIA ES DECRECIENTE")
   else:
      print("LA SECUENCIA ESTA EN DESORDEN")
   

def esCreciente(N,S)-> bool:
# PARAMETROS N: int                 // tamanio del arreglo
#            S: array [0..N) of int // secuencia a verificar

   # Precondicion: 
   assert(N > 1) 

   # VARIABLES
   #   crece: bool
   #   k: int
   #   cota: int     // funcion de cota

   crece,k = True,1
   cota = N-k

   # Verificacion de Invariante y cota antes del ciclo
   assert(1<=k<=N and crece == all(S[i-1]<=S[i] for i in range(1,k) ))
   assert(cota >= 0)
   while crece and k < N :
      if S[k-1] > S[k]: 
         crece = False
      k = k+1
      # Verificacion de Invariante y cota en cada ciclo
      assert(1<=k<=N and crece == all(S[i-1]<=S[i] for i in range(1,k) ))
      assert(cota >= N-k)
      cota = N-k
      assert(cota >= 0)

   # Postcondicion:  
   assert(crece == all(S[i-1]<=S[i] for i in range(1,N) ) )
    
   return crece

def esDecreciente(N,S)-> bool:
# PARAMETROS N: int                 // tamanio del arreglo
#            S: array [0..N) of int // secuencia a verificar

   # Precondicion: 
   assert(N > 1) 

   # VARIABLES
   #   decrece: bool
   #   k: int
   #   cota: int     // funcion de cota

   decrece,k = True,1
   cota = N-k

   # Verificacion de Invariante y cota antes del ciclo
   assert(1<=k<=N and decrece == all(S[i-1]>=S[i] for i in range(1,k) ))
   assert(cota >= 0)
   while decrece and k < N :
      if S[k-1] < S[k]: 
         decrece = False
      k = k+1
      # Verificacion de Invariante y cota en cada ciclo
      assert(1<=k<=N and decrece == all(S[i-1]>=S[i] for i in range(1,k) ))
      assert(cota >= N-k)
      cota = N-k
      assert(cota >= 0)

   # Postcondicion:  
   assert(decrece == all(S[i-1]>=S[i] for i in range(1,N) ) )
    
   return decrece

def verOrden(N, S) -> int:
# PARAMETROS N: int                 // tamanio del arreglo
#            S: array [0..N) of int // secuencia a verificar

   # Precondicion: 
   assert(N > 1) 

   # VARIABLES
   #   orden: int
	  
   if esCreciente(N,S):
     orden = 1
   elif esDecreciente(N,S):
     orden = -1
   else:
     orden = 0
   
   # Postcondicion:  
   assert((orden == 1 and esCreciente(N,S)) or (orden == -1 and esDecreciente(N,S)) or 
          (orden == 0 and (not esCreciente(N,S)) and (not esDecreciente(N,S))) )
   
   return orden


# PROGRAMA PRINCIPAL
   
# Variables: 
#    N : int                 // ENTRADA: tamanio de la secuencia
#	 S: array [0..N) of int  // ENTRADA: secuencia a verificar
#    orden: int              // SALIDA: dice en que orden viene la secuencia
	 
# Valores iniciales:
print("Diga el tamanio de la secuencia:")

while True:
  try:
    N = int(input('N = '))
	
	# Precondicion:
    assert( N > 1 )
    break
  except:
    print("N debe ser positivo y mayor que 1")
    print("Vuelva a intentar")

S = leerSecuencia(N)

# Calculos
orden = verOrden(N,S)

# Postcondicion	
assert(	
     (orden == 1 and all(S[i-1]<=S[i] for i in range(1,N))) or 
     (orden == -1 and all(S[i-1]>=S[i] for i in range(1,N))) or 
	 (orden == 0 and (not all(S[i-1]<=S[i] for i in range(1,N)) or not all(S[i-1]>=S[i] for i in range(1,N))))
)

# Salida: 
imprimirOrden(orden)
