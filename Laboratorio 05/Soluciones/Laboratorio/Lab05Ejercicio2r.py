#
# Lab05Ejercicio2r.py (version robusta)
# 
# DESCRIPCION: Recibe un numero y se calcula la cantidad de pasos para verificar la conjetura
# que dice: “Si se toma cualquier número natural x, el siguiente de la secuencia se genera así:
# si el número x es par, el siguiente número será igual a la mitad x;
# si el número x es impar, el siguiente se obtiene al multiplicar por 3 y sumarle 1.Si el
# proceso se repite, en algún número finito de pasos se llegará a la secuencia 4, 2, 1”. Y 
# en cada paso se debe mostrar el número de intentos y el valor actual de x.
#
# Autor: Rosseline Rodriguez
# 
# Ultima modificacion: 24/02/2018

import sys 

# CONSTANTES
MAX = 1000        # int // Maximo numero de intentos 

# VARIABLES
#    x : int        // Entrada: un numero natural
#    intentos : int // Salida: numero de intentos 

# Valores iniciales 
x = 0

# Verificacion de la Precondicion (version robusta)
while True:
   x = int(input("Introduzca el numero natural : " ))   
   try:
      assert(x > 0)
      break
   except: 
      print("El numero debe ser positivo. Vuelva a intentar ...")
   
# Calculos
intentos = 0
cota = MAX-intentos

#Verificacion de la cota al inicio del ciclo
try:
   assert(cota >= 0)
except:
   print("Error: cota negativa. El programa terminara ")
   print("cota="+str(cota))
   sys.exit()
   
while (x != 4) and (intentos < MAX):
   if (x % 2 == 0):
      x = x//2
   else:
      x = (3*x)+1
   intentos = intentos + 1

   #Verificacion de cota decreciente en cada iteracion	    
   try:
      assert(cota > MAX-intentos) 
   except:
      print("Error: cota no decreciente. El programa terminara ")
      print("cota anterior ="+str(cota)+" nueva cota ="+str(MAX-intentos))
      sys.exit()

   cota = MAX - intentos
   #Verificacion de la cota no negativa en cada iteracion
   try:
      assert(cota >= 0)
   except:
      print("Error: cota negativa. El programa terminara ")
      print("cota="+str(cota))
      sys.exit()

   # Salida interna del ciclo
   print("Intento: " + str(intentos))
   print("El valor actual de x es " + str(x))

	  
# Postcondicion: intentos tiene el numero de veces que se realizo el ciclo para
#                llegar al valor 4 empenzando en el valor inicial de x y siguiendo
#                la conjetura planteada