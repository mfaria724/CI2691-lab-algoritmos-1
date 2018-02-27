#
# Prelab3Ejercicio2.py
#
# DESCRIPCION: Programa que cuenta los divisores de un numero entero N
#
# Autor: 
#	Rosseline Rodriguez
#
# Ultima modificacion: 03/02/2018

# Variables:
#    N: int;             // ENTRADA: entero para calcular su numero de divisores
#	 cuenta: bool;       // SALIDA: numero de divisores de N
#	 k: int;             // Variable de control del ciclo
#    cota: int;          // Limite de iteraciones del ciclo

# Valores iniciales:
N = int(input("Introduzca un entero positivo: "))

# Precondicion:
assert(N > 0)

# Calculos:
cuenta,k = 0,1
cota = N+1-k
	
#Verificacion de invariante al inicio del ciclo
assert(1<=k<=N+1 and cuenta == sum( 1 for i in range(1,k) if (N % i == 0)) )
assert(cota >= 0)
	  
while (k<=N):
   if (N % k == 0):
      cuenta = cuenta + 1
   k = k+1
		
   #Verificacion de invariante y cota en cada iteracion	    
   assert(1<=k<=N+1 and cuenta == sum( 1 for i in range(1,k) if (N % i == 0)) )
   assert(cota > N+1-k) 
   cota = N+1 - k
   assert(cota >= 0)
   
# Postcondicion:
assert( cuenta == sum( 1 for i in range(1,N+1) if (N % i == 0)))

# Salida:
print("El numero de divisores de ",N,"es:", cuenta)

