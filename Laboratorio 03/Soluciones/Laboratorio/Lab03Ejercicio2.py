#
# Lab03Ejercicio2.py
#
# DESCRIPCION: Dado un entero positivo n, el programa dice si el entero es primo
#
# Autor: 
#	Rosseline Rodriguez
#
# Ultima modificacion: 03/02/2018

# Variables:
#    n: int;            // ENTRADA: natural para la suma de cuadrados
#	 esPrimo: bool;     // SALIDA: suma de cuadrados
#	 k: int;            // Variable de control del ciclo

# Valores iniciales:
n = int(input("Introduzca un entero positivo: "))

# Precondicion:
assert(n > 0)

# Calculos:
esPrimo,k = True,2
cota = n-k
	
#Verificacion de invariante al inicio del ciclo
assert(2<=k<=n and esPrimo == all( (n % i != 0) for i in range(2,k)))
assert(cota >= 0)
	  
while (esPrimo and k<n): # la guardia también puede ser k<(n//2) que es más eficiente
   if (n % k == 0):
      esPrimo = False
   k = k+1
		
   #Verificacion de invariante y cota en cada iteracion	    
   assert(2<=k<=n and esPrimo == all( (n%i != 0) for i in range(2,k)))
   assert(cota > n-k) 
   cota = n - k
   assert(cota >= 0)
	 
# Postcondicion:
assert(
	esPrimo == all( (n%i != 0) for i in range(2,n))
)

# Salida:
print(n,"es primo?", esPrimo)

