#
# Lab04Ejercicio1.py
#
# DESCRIPCION: Programa que lee los coeficientes de un P
# hasta que se introduzca el valor cero, y los almacena en un arreglo. 
# El programa muestra en pantalla el grado del P y luego escribe 
# el P en notacion polinomial, es decir, 
# P(X) = C0+C1X+C2X^2+...+CnX^n, donde Ci es el coeficiente i leido. 
#
# Autores: 
#	Saul Hidalgo y Rosseline Rodriguez
#
# Ultima modificacion: 16/02/2018

# Variables:
#   M: int                 // ENTRADA: tamanio maximo del P
#   P: array [0..M) of int // ENTRADA: coeficientes del P
#   grado: int             // SALIDA: Grado del P
#   continuar: bool        // Dice si se debe continuar leyendo coeficientes
#   i: int                 // Variable de control del ciclo
#   xi: int                // Auxiliar para la lectura de coeficientes
#   cota: int              // Función de cota

# Valores iniciales:
M = int(input("Indique el tamanyo maximo posible del P: "))
P = [0 for x in range(0,M+1)]
continuar = True
xi = -1  # se inicializa xi con un valor que satisfaga el invariante

# Precondición
assert( M >= 0 )

# Calculos
i = 0
cota = M+1-i
	
#Verificacion de invariante al inicio del ciclo
assert( 0<=i<=M+1 and all( P[x] != 0 for x in range(0,i)) and continuar == (xi != 0) )
assert(cota >= 0)

while (continuar and i < M+1):

  xi = int(input("Indique el siguiente coeficiente (terminar con 0): "))
    
  if ( xi == 0 ):
      continuar = False
  else:
      P[i] = xi
      i = i+1
      #Verificacion de invariante y cota en cada iteracion	    
      assert(0<=i<=M+1 and  all( P[x] != 0 for x in range(0,i)) and continuar ==(xi != 0) )
      assert(cota > M+1-i)
      cota = M+1 - i
      assert(cota >= 0)

if (i > 0):  # al menos tiene un coeficiente diferente de cero
   grado = i-1
else:
   grado = 0
   
# Postcondicion

assert ( (all( P[x] != 0 for x in range(0,grado+1) ) ) or (grado == 0 and P[0] == 0 ) ) 
		 
# Salida
print("El grado del P es: " + str(grado))

print('P(x) = ', end="") # colocamos el end="", para evitar el fin de linea.

if ( P[0] == 0 ):
  print(0,end="")
elif ( P[0] != 0 ):
   for x in range(0,grado+1):
      if ( P[x] > 0 and x > 0 ):
         print( "+", end="")
         if (P[x] > 1):
            print( P[x] , end="")

      elif ( P[x] == -1 and x > 0 ):
         print( "-" , end="")
      else:
         print( P[x] , end="" )
      
      if ( x > 0 ):
         print( "X", end="" )
         if ( x > 1 ):
            print( "^" + str(x) , end="" )          
  
print()


