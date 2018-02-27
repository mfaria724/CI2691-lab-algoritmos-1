#
# Lab05Ejercicio3c.py
# 
# DESCRIPCION: programa que dada una secuencia de enteros terminada en 0 provista por el teclado,
# donde solo aparecen los valores del conjunto {1,2,3,4}, cuenta para cada valor del conjunto,
# cuantas veces aparece dentro de la secuencia. Version por contrato
#
# Autor: Rosseline Rodriguez
# 
# Ultima modificacion: 24/02/2018

import sys 

# CONSTANTES
MAX = 1000        # int // Maximo numero de intentos 

# VARIABLES
#   e : int      // Entrada: elemento actual leido
#   n1 : int     // Salida: dice cuantas veces aparece el 1
#   n2 : int     // Salida: dice cuantas veces aparece el 2
#   n3 : int     // Salida: dice cuantas veces aparece el 3
#   n4 : int     // Salida: dice cuantas veces aparece el 4
#   k : int      // Variable de iteracion
#   cota : int   // Cota de la iteracion

# VALORES INICIALES
print("Introduzca una secuencia de valores en el conjunto {1,2,3,4} ")
k,n1,n2,n3,n4 = 0,0,0,0,0
cota = MAX-k

# Inv: 0<=k<=MAX /\ 
#      n1 == (%sigma i: 0<=i<k : Sec(i) == 1) /\ 
#      n2 == (%sigma i: 0<=i<k : Sec(i) == 2) /\ 
#      n3 == (%sigma i: 0<=i<k : Sec(i) == 3) /\ 
#      n4 == (%sigma i: 0<=i<k : Sec(i) == 4)
#      siendo Sec la secuencia introducida y k el tamano actual de la secuencia

#Verificacion de la cota al inicio del ciclo
try:
   assert(cota >= 0)
except:
   print("Error: cota negativa. El programa terminara ")
   print("cota="+str(cota))
   sys.exit()

while k < MAX:
   e = int(input("Introduzca un valor del conjunto (para finalizar introduzca 0): "))

   try: 
      # Precondicion: valor leido en el rango 0..4
      assert(e >= 0 and e <= 4) 
   except:
      print("El valor no esta en el conjunto. El programa terminara...")
      sys.exit() 

   # Calculos 

   if e == 0: # termino la secuencia
      break
   if e == 1: 
      n1 = n1+1
   elif e == 2: 
      n2 = n2+1
   elif e == 3: 
      n3 = n3+1
   else: 
      n4 = n4+1
   k = k+1

   #Verificacion de cota decreciente en cada iteracion	    
   try:
      assert(cota > MAX-k) 
   except:
      print("Error: cota no decreciente. El programa terminara ")
      print("cota anterior ="+str(cota)+" nueva cota ="+str(MAX-k))
      sys.exit()

   cota = MAX - k
   #Verificacion de la cota no negativa en cada iteracion
   try:
      assert(cota >= 0)
   except:
      print("Error: cota negativa. El programa terminara ")
      print("cota="+str(cota))
      sys.exit()
		 
# Postcondicion: 
#      n1 == (%sigma i: 0<=i<k : Sec(i) == 1) /\ 
#      n2 == (%sigma i: 0<=i<k : Sec(i) == 2) /\ 
#      n3 == (%sigma i: 0<=i<k : Sec(i) == 3) /\ 
#      n4 == (%sigma i: 0<=i<k : Sec(i) == 4)
#      siendo Sec la secuencia introducida y k el tamano actual de la secuencia

# Salida 
print("Numero de veces que aparece el 1 : ",n1)
print("Numero de veces que aparece el 2 : ",n2)
print("Numero de veces que aparece el 3 : ",n3)
print("Numero de veces que aparece el 4 : ",n4)
