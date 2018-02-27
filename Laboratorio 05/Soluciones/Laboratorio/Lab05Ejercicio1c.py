#
# Lab05Ejercicio1c.py
# 
# DESCRIPCION: programa que verifica si una secuencia de enteros no negativos provista por el
# teclado está ordenada en forma creciente. La secuencia de entrada termina cuando se
# recibe el número 0.
#
# Autor: Rosseline Rodriguez
# 
# Ultima modificacion: 24/02/2018

import sys 

# CONSTANTES
MAX = 1000        # int // Maximo numero de intentos 

# VARIABLES
#   e : int      // Entrada: elemento actual leido
#   ant : int    // Entrada: elemento leido en la iteracion anterior
#   crece : bool // Salida: dice si el arreglo es creciente
#   k : int      // Variable de iteracion
#   cota : int   // Cota de la iteracion

# VALORES INICIALES
print("Este programa verifica si una secuencia es creciente")
k, crece = 0, True
cota = MAX-k

# Inv: 0<=k<=MAX /\ crece == (%forall i: 0<=i<k-1 : Sec(i) <= Sec(i+1)) 
#      siendo Sec la secuencia introducida y k el tamano actual de la secuencia

#Verificacion de la cota al inicio del ciclo
try:
   assert(cota >= 0)
except:
   print("Error: cota negativa. El programa terminara ")
   print("cota="+str(cota))
   sys.exit()

while k < MAX:
   e = int(input("Introduzca un entero positivo (para finalizar introduzca 0): "))

   try: 
      # Precondicion: valor leido positivo o cero
      assert(e >= 0) 
   except:
      print("El valor debe ser positivo. El programa terminara...")
      sys.exit() 

   try: 
      # Precondicion: secuencia no vacia
      assert(not(e == 0 and k == 0)) 
   except:
      print("La secuencia no puede ser vacia. El programa terminara...")
      sys.exit()

   try: 
      # Precondicion: secuencia no unitaria
      assert(not(e == 0 and k == 1)) 
   except:
      print("La secuencia no puede ser unitaria. El programa terminara...")
      sys.exit()

   # Calculos 
   k = k+1

   if e == 0: # termino la secuencia
      break
   if k == 1: # se ha leido un numero positivo
      ant = e
   else:      # se ha leido mas de un numero positivo
      if (ant <= e): # es creciente
         ant = e
      else:         # no es creciente
         crece = False

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

# Postcondicion: crece == (%forall i: 0<=i<k-1 : Sec(i) <= Sec(i+1)) 
#                siendo Sec la secuencia introducida y k el tamano de la secuencia

# Salida 
print("La secuencia es creciente?",crece)
