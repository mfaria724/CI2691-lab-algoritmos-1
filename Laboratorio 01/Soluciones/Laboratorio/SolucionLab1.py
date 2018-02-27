#
# SolucionLab1.py
#
# DESCRIPCION: Este archivo contiene la solucion modelo de los ejercicios adicionales 
#              del laboratorio 1 (Partes 1-3)
#
# Autor: 
#	Prof. Rosseline Rodriguez
#
# Ultima modificacion: 13/01/2018
#

## PARTE 1: Traducción de variables y expresiones de GCL a Python.

# VARIABLES:

# 1. var x := 10:int // Valor inicial de x
x = 10

# 2. var edad := 32:int        // Valor inicial de la edad
edad = 32

# 3. var pi:= 3.14159: float   // Valor de la constante pi
pi = 3.114159

# 4. var altura:= 2.1: float   // Valor inicial de la altura
altura = 2.1

# 5. var peso:= 76.8: float    // Valor inicial del peso
peso = 76.8

# 6. var y:= 20 + 3i: complejo // Valor inicial de y
y = 20.0+3.0j

# 7. var z:= 1+i: complejo     // Valor inicial de z
z = 1+1j

# EXPRESIONES:
# 1. x mod 3
x%3

# 2. 525 div edad
525 // edad

# 3. el valor absoluto de -pi
abs(-pi)

# 4. la norma de y dividido entre el peso
abs(y)/peso

# 5. altura por pi
altura*pi

## PARTE 2: Cuantificadores y funciones de agregacion

# 1. ( sum x : 1 <= x < 100 /\ x mod 7 == 0 : x )
sum (x for x in range(1,100) if x % 7 == 0)

# 2. ( max x : 5 <= x < 40 /\ x*x mod 7== 0 : x )
max (x for x in range(5,40) if x*x % 7 == 0)

# 3. ( min x : 5 <= x < 40 /\ x*x == 128 : x )
min (x for x in range(5,40) if x*x % 7 == 0)

# 4. ( exists x: 0 <= x <= b : b=2*x )
any (b==2*x for x in range(0,b+1))

# 5. Esperfecto(n) == (exists x: 0 <= x <= n : n=x*x )
def Esperfecto(n): return any (n==x*x for x in range(0,n+1))


## PARTE 3: Secuencia de instrucciones con aserciones

# 1.
a,b = 32,43
# Precondicion
assert( a == 32 and b == 43)
b , a = a , b
# Postcondicion
assert( b == 32 and a == 43)

# 2.
a,b = 100,5
# Precondicion
assert( a == 100 and b == 5 )
c = a//b
# Postcondicion
assert( c == a//b )

# 3.
a,b = 43, 35
# Precondicion: (a == A and b = B)
assert( a == 43 and b == 35 )
# Calculos
c = a % b
c = c*10
a = c
# Postcondicion: (a == c and c == A%B*10)
assert( a == c and c == 43%35*10)

# 4.
a,b,c = 80,180,0
# Precondicion
assert( a == 80 and b == 180 )
# Calculos
c = (b % a)*100
# Postcondicion
assert( a == 80 and b == 180 and c == 2000 )
