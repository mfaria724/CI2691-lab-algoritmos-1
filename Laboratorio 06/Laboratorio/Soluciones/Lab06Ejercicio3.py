#
# Lab6Ejercicio3.py
#
# DESCRIPCION: programa que dados dos numeros naturales N y M, produce la secuencia de
# los factores primos de M que son menores o iguales a N, junto con su
# exponente en la factorizacion de M.
#
# Autor: 
#	Rosseline Rodriguez
#
# Ultima modificacion: 10/03/2018

# Definicion del cuantificador productoria
def prod( iterable ):
	p = 1
	for n in iterable:
		p *= n
	return p
	

def esprimo( n ) -> bool:
# PARAMETROS n: int  // el entero a verificar

   # Precondicion: 
   assert(n > 1) 

   # VARIABLES
   #   primo: bool // dice si n es primo
   #   k: int      // variable de control del ciclo
   #   cota: int   // funcion de cota
   
   primo,k = True,2
   cota = n-k
   
   # Verificacion de Invariante y cota antes del ciclo
   assert(1<k<=n and primo == all((n % i != 0) for i in range(2,k) ))
   assert(cota >= 0)
   while primo and k < n :
     if n % k == 0 :
        primo = False
     k = k+1
     # Verificacion de Invariante y cota en cada ciclo
     assert(1<=k<=n and primo == all((n % i != 0) for i in range(2,k) ))
     assert(cota >= n-k)
     cota = n-k
     assert(cota >= 0)
   
   # Postcondicion:  
   assert(primo == all((n % i != 0) for i in range(2,n) ) )
    
   return primo
   

# Cuantas veces divide a n a x
def cuantoDivide(n, x)->int:
# PARAMETROS n: int  // el divisor
#            x: int  // el dividendo

   # Precondicion: 
   assert(n > 1 and x > 1) 

   # VARIABLES
   #   cuenta: int   // numero de veces que n divide a x
   #   cociente: int // el cociente de de dividir entre n
	  
   cociente,cuenta = x,0
   cota = x//n-cuenta

   # Verificacion de Invariante y cota antes del ciclo
   assert(0<=cuenta<x/n and x == cociente*prod(n for i in range(0,cuenta) ))
   assert(cota >= 0)
   while ( cociente % n == 0):
     cuenta = cuenta+1
     cociente = cociente // n
	 
     # Verificacion de Invariante y cota en cada ciclo
     assert(0<=cuenta<x/n and x == cociente*prod(n for i in range(0,cuenta) ))
     assert(cota >= x//n-cuenta)
     cota = x//n-cuenta
     assert(cota >= 0)
    
   # Postcondicion: 
   assert ((x % prod(n for i in range(0,cuenta) ) == 0) and (x % prod(n for i in range(0,cuenta+1) ) != 0) )
   
   return cuenta
   

def producirSecuenciaFP(N,M)->'void':
# PARAMETROS N: int  // entero a quien se le buscan los divisores
#            M: int  // entero como cota superior

   # Precondicion: 
   assert(N > 0 and M > 0) 

   # VARIABLES
   #  k: int        // variable control del ciclo
   #  termine: bool // dice si se llego al limite
   #  cota: int     // funcion de cota
   
   k,termine = 2,False
   cota= N-k
   
   # Verificacion de Invariante y cota antes del ciclo
   assert(1<k<=N+1 and termine == (not (k < M)) )
   assert(cota >= 0)
   while not termine and k <= N :
      if k < M :
         if esprimo(k) and (N % k == 0) :
           print(str(k) + " divide a " + str(N) + " con exponente " + str(cuantoDivide(k,N)))
      else:
        termine = True
      k = k+1

   # Postcondicion: 
   #   (%forall i: 0<=i<|S| /\ (i mod 2 = 0): 
   #      (S[i] < M) /\ esprimo(S[i]) /\ (N mod (S[i]^S[i+1]) == 0) /\ S[i+1] = cuantoDivide(S[i],N)) 


# PROGRAMA PRINCIPAL
   
# Variables: 
#    N: int  // ENTRADA: entero a quien se le buscan los divisores
#	 M: int  // ENTRADA: cota superior de busqueda
	 
# Valores iniciales:
print("Este programa calcula los divisores de un entero N menores que M") 

while True:
  try:
    N = int(input('N = '))
	
	# Precondicion:
    assert( N > 0 )
    break
  except:
    print("N debe ser positivo ")
    print("Vuelva a intentar")
	 
while True:
  try:
    M = int(input('M = '))
	
	# Precondicion:
    assert( M > 0 )
    break
  except:
    print("M debe ser positivo ")
    print("Vuelva a intentar")

# Calculos y Salida	
producirSecuenciaFP(N,M)
