#
# Lab03Ejercicio3.py
#
# DESCRIPCION: Dado un entero positivo n, el programa dice si el entero es perfecto
#
# Autor: 
#	Rosseline Rodriguez
#
# Ultima modificacion: 03/02/2018

# Variables:
#    n: int;             // ENTRADA: natural para la suma de cuadrados
#	 esPerfecto: bool;   // SALIDA: suma de cuadrados
#	 k: int;             // Variable de control del ciclo
#    suma:int;           // Auxiliar para el calculo de la suma de divisores

# Valores iniciales:
n = int(input("Introduzca un entero positivo: "))

# Precondicion:
assert(n > 0)

# Calculos:
suma,k = 0,1
cota = n-k
	
#Verificacion de invariante al inicio del ciclo
assert(1<=k<=n and suma == sum( i for i in range(1,k) if (n % i == 0)) )
assert(cota >= 0)
	  
while (k<n):
   if (n % k == 0):
      suma = suma + k
   k = k+1
		
   #Verificacion de invariante y cota en cada iteracion	    
   assert(1<=k<=n and suma == sum( i for i in range(1,k) if (n % i == 0)) )
   assert(cota > n-k) 
   cota = n - k
   assert(cota >= 0)
   
if (n == suma):
   esPerfecto = True
else:
   esPerfecto = False

# Postcondicion:
assert(
	esPerfecto == (n == sum( i for i in range(1,n) if (n % i == 0)))
)

# Salida:
print(n,"es perfecto?", esPerfecto)

