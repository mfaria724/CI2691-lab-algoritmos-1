#
# Quiz31510463.py
#
# DESCRIPCION: 
# 
# Autor: Manuel Faria 15-10463
#	
# Ultima modificacion: 20/03/2018

import sys

# Mueatra el menu de opciones

def menu() -> int:
   print("Menu:")
   print("1) Son coprimos?")
   print("2) Phi de Euler")
   print("3) Salir")
   op = int(input("Tu opcion? "))
   return op

# Retorna 1 si x y y son coprimos y 0 en caso contrario
# escriba la traduccion de la funcion sonCoprimos de GCL


# ... complete el codigo
def sonCoprimos(x: int, y: int) -> int:
   
   # PRE:   ... complete la precondicion ...
   assert( x >= 0 and y >= 0 )

   coprimos = 1

   if x >= y:
      i = y
      menor = y
   else:
      i = x
      menor = x

   while i != 1:
      if x % i == 0 and y % i == 0:
         coprimos = 0

      i = i - 1

   # POST:
   assert(not (any (x % i == 0 and y % i == 0 for i in range(2,menor + 1)) and coprimos == 1) or (any (x % i == 0 and y % i == 0 for i in range(2,menor + 1)) and coprimos == 0))
   
   return coprimos


# Cuenta cuantos enteros positivos menores que n son coprimos con n
#... phiEuler(...)

def phiEuler(n: int) -> int:

   # PRE:  
   assert(n > 0)

   i = n
   contador = 0
   
   while i != 1:
      
      j = i - 1
      coprimos = True

      while j != 1:
         if n % j == 0 and i % j == 0:
            print(j)
            coprimos = False

         j = j - 1

      if coprimos == True:
         contador = contador + 1

      i = i - 1

   # POST:  ... complete la postcondicion ...
   # assert(contador == sum (1 for i in range(2,n) if not any (n % j == 0 and i % j == 0 for j in range(2,i))))

   return contador

# Recibe un entero que representa la opcion seleccionada y llama a la funcion 
# adecuada segun lo que indica esa opcion
def ejecutar(op) -> 'void':
   # VAR 
   #    a: int
   #    b: int
   
   if (op == 1):
      print("Son a y b coprimos?")
      a = int(input("a: "))
      b = int(input("b: "))

      if ( sonCoprimos(a,b) == 1 ): # borrar el True y completar con la llamada a la funcion
         print("SI son coprimos")
      else:
         print("NO son coprimos")
   elif (op == 2):
      print("Cuántos coprimos tiene n?")

      n = int(input("n: "))

      print(str(n) + " tiene " + str(phiEuler(n)) + " coprimos.")

op = 0
while (op != 3):
   op = menu()
   ejecutar(op)

