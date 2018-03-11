#
# Prelab6Ejercicio2.py
#
# DESCRIPCION: Ejercicio del Prelaboratorio 5 modificado con un subprograma para los calculos.
#              El programa calcula la suma de los factoriales de 0 a N. 
#
# Autor:
#        Rosseline Rodriguez
#
# Ultima modificacion: 24/02/2018

import sys

# SUBPROGRAMAS

# Definicion del cuantificador productoria
def prod( iterable ):
	p = 1
	for n in iterable:
		p *= n
	return p

def sumaFactoriales(N: int) -> int:
# ENTRADAS: N     // limite de la suma de factoriales
# SALIDAS:  suma  // valor de la suma de factoriales
# PRE: N >= 0
# POST: suma == sum ( prod( j for j in range(1,i+1) ) for i in range(0,N+1) )

# Variables locales: 
#     fact : int // auxiliar para el calculo del factorial 
#     cota : int // valor de la cota del ciclo
#     k : int    // variable de control del ciclo

   try: 
      # Precondicion: valor de N positivo
      assert(N >= 0)
   except:
      print("La precondicion no se cumple: valor negativo ")
      print("El programa terminara")
      sys.exit()
	  
   suma,fact,k = 0,1,0
   cota = N + 1 - k

   # Verificacion de invariante al inicio del ciclo
   try:
      assert(0<=k<=N+1 and (fact == prod( j for j in range(1,k) ) ) and suma == sum( prod( j for j in range(1,i+1) ) for i in range(0,k) ) )
   except:
      print("Hubo un error en el invariante para los siguientes valores")
      print("k="+str(k)+" fact="+str(fact)+" suma="+str(suma))
      print("El programa terminara")
      sys.exit()

	  
   #Verificacion de la cota al inicio
   try:
      assert(cota >= 0)
   except:
      print("Error: cota negativa. El programa terminara ")
      print("cota="+str(cota))
      sys.exit()

   while(k<=N):
      if( k>0 ):
         fact = fact*k
      else:
         pass
      suma = suma+fact
      k = k + 1
	
      #Verificacion de invariante en cada iteracion
      try:
         assert( 
            0<=k<=N+1 and fact == prod ( j for j in range(1,k) ) and suma == sum ( prod ( j for j in range(1,i+1) ) for i in range(0,k) ) 
         )
      except:
         print("Hubo un error en el invariante para los siguientes valores")
         print("k="+str(k)+" fact="+str(fact)+" suma="+str(suma))
         print("El programa terminara")
         sys.exit()
   
      #Verificacion de cota decreciente en cada iteracion	    
      try:
         assert(cota > N+1-k) 
      except:
         print("Error: cota no decreciente. El programa terminara ")
         print("cota anterior ="+str(cota)+" nueva cota ="+str(N-k+1))
         sys.exit()

      cota = N+1 - k
      #Verificacion de la cota no negativa en cada iteracion
      try:
         assert(cota >= 0)
      except:
         print("Error: cota negativa. El programa terminara ")
         print("cota="+str(cota))
         sys.exit()

   # Postcondicion:
   assert( suma == sum ( prod( j for j in range(1,i+1) ) for i in range(0,N+1) ) )

   return (suma)
# FIN de sumaFactoriales

# PROGRAMA PRINCIPAL
   
# Variables: 
#     N : int    // ENTRADA: natural que limita la suma
#     suma : int // SALIDA: suma de los factoriales

# Valores iniciales:
while (True):
   N = int(input("Introduzca un entero positivo: "))

   # Precondicion: se verifica la pre porque se hace programacion robusta
   try:
      assert(N >= 0)
      break
   except:
      print("La precondicion no se cumple: valor negativo ")
      print("Vuelva a intentar")

# Calculos
suma = sumaFactoriales(N)

# Aquí no se verifica la post. Ya se verifico en el subprograma.
# Es muy sencillo el codigo del programa principal seria redundante

# Salida:
print("la suma de los factoriales de cero a", N ,"es:")
print(suma)

# FIN DEL PROGRAMA PRINCIPAL