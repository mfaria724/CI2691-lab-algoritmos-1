#
# Prelab5ejercicio3.py
#
# DESCRIPCION: Ejercicio del Prelaboratorio 3 modificado con acciones que verifican las aserciones.
#              Programa que cuenta los divisores de un numero entero N. Version por contrato
# Autor: 
#	Rosseline Rodriguez
#
# Ultima modificacion: 24/02/2018

# Variables:
#    N: int;             // ENTRADA: entero para calcular su numero de divisores
#	 cuenta: bool;       // SALIDA: numero de divisores de N
#	 k: int;             // Variable de control del ciclo
#    cota: int;          // Limite de iteraciones del ciclo

import sys

# Valores iniciales:
N = int(input("Introduzca un entero positivo: "))

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

# Salida:
print("El numero de divisores de ",N,"es:", cuenta)

