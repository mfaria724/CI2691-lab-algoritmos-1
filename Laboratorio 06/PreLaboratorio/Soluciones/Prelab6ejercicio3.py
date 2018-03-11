#
# Prelab6ejercicio3.py
#
# DESCRIPCION: Ejercicio del Prelaboratorio 6 modificado con subprogramas para los calculos.
#              Programa que cuenta los divisores de un numero entero N. 
# Autor: 
#	Rosseline Rodriguez
#
# Ultima modificacion: 06/03/2018

import sys

# SUBPROGRAMAS

def cuentaDivisores(N: int) -> int:
# ENTRADAS: N       // numero a quien se le buscan los divisores
# SALIDAS:  cuenta  // numero de divisores de N
# PRE: N > 0
# POST: cuenta == sum( 1 for i in range(1,N+1) if (N % i == 0))

# Variables locales: 
#	 cuenta: int       // Auxiliar para el numero de divisores de N
#	 k: int            // Variable de control del ciclo
#    cota: int         // Limite de iteraciones del ciclo

   # Precondicion:
   try:
      assert(N > 0)
   except:
      print("La precondicion no se cumple: valor negativo ")
      print("El programa terminara")
      sys.exit()

   # Calculos:
   cuenta,k = 0,1
   cota = N+1-k
	
   #Verificacion de invariante al inicio del ciclo
   try:
      assert(1<=k<=N+1 and cuenta == sum( 1 for i in range(1,k) if (N % i == 0)) )
   except:
      print("Hubo un error en el invariante para los siguientes valores")
      print("k="+str(k)+" cuenta="+str(cuenta))
      print("El programa terminara")
      sys.exit()

   #Verificacion de la cota al inicio
   try:
      assert(cota >= 0)
   except:
      print("Error: cota negativa. El programa terminara ")
      print("cota="+str(cota))
      sys.exit()

   while (k<=N):
      if (N % k == 0):
         cuenta = cuenta + 1
      k = k+1
		
      #Verificacion de invariante en cada iteracion
      try:
         assert(1<=k<=N+1 and cuenta == sum( 1 for i in range(1,k) if (N % i == 0)) )
      except:
         print("Hubo un error en el invariante para los siguientes valores")
         print("k="+str(k)+" cuenta="+str(cuenta))
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
   assert( cuenta == sum( 1 for i in range(1,N+1) if (N % i == 0)))

   return (cuenta)
# END de cuentaDivisores

# PROGRAMA PRINCIPAL

# Variables:
#    N: int;             // ENTRADA: entero para calcular su numero de divisores
#	 cuenta: bool;       // SALIDA: numero de divisores de N

# Valores iniciales:
try: 
   N = int(input("Introduzca un entero positivo: "))

   # Aquí no se verifica la pre se deja para el subprograma
   # pues es muy sencillo el codigo del programa principal
except:
   print("Datos incorrectos ")
   print("El programa terminara")
   sys.exit()

cuenta = cuentaDivisores(N)

# Aquí no se verifica la post. Ya se verifico en el subprograma.
# Es muy sencillo el codigo del programa principal seria redundante

# Salida:
print("El numero de divisores de",N,"es:", cuenta)

