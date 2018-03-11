#
# Prelab6ejercicio1.py
#
# Descripcion: Programa que dado un polinomio de grado 2 calcula sus raices
# Utilizando condicionales y funciones.
#
# Autores:  Prof. Rosseline Rodriguez y Prof. Saul Hidalgo
#
# Ultima modificacion: 06/03/2018

from math import sqrt # Importamos sqrt para calcular raices cuadradas
import sys

# SUBPROGRAMAS

def calcularRaices(a: float, b: float, c: float) -> (float,float):
# ENTRADAS: a,b,c coeficientes de la ecuacion cuadratica
# SALIDAS:  x1,x2 raices de la ecuacion cuadratica
# PRE: b * b - 4 * a * c >= 0
# POST: a * x1 * x1 + b * x1 + c == 0 and a * x2 * x2 + b * x2 + c == 0

  try:
     # Precondicion: se verica que el sistema tiene solucion.
     assert( b * b - 4 * a * c >= 0)
  except:
    print("funcion calcularRaices: la precondicion no se cumple")
    print("El programa terminara")
    sys.exit()
	
  # Calculos  
  x1 = (-b + sqrt( b * b - 4 * a * c )) / ( 2 * a )
  x2 = (-b - sqrt( b * b - 4 * a * c )) / ( 2 * a )

  try:
    # Postcondicion: 
    assert( (a * x1 * x1 + b * x1 + c == 0 and a * x2 * x2 + b * x2 + c == 0) )
  except:
    print("Hubo un error al calcularRaices x1=",x1,"y x2=",x2)
    print("El programa terminara..." )
    sys.exit()

  return (x1,x2)
# FIN calcularRaices


# PROGRAMA PRINCIPAL

# VARIABLES:
#       a: float     // Entrada: termino cuadratico
#       b: float     // Entrada: termino lineal
#       c: float     // Entrada: termino constante
#       x1,x2: float // Salidas: raices del polinomio

# Valores iniciales:
print("Introduzca los coeficiente de la ecuacion AX^2 + BX + C:")

while True:
  try:
    a = float(input('A: '))
    b = float(input('B: '))
    c = float(input('C: '))

    # Aquí no se verifica la pre se deja para el subprograma
	# pues es muy sencillo el codigo del programa principal
    break
  except:
    print("Hubo un error en los datos de entrada")
    print("Vuelva a intentar")

# Calculos
x1,x2 = calcularRaices(a,b,c)

# Aquí no se verifica la post. Ya se verifico en el subprograma.
# Es muy sencillo el codigo del programa principal seria redundante

# Salida
print("El resultado es: x1 = " + str(x1) + " y x2 = " + str(x2))
  
# FIN DEL PROGRAMA PRINCIPAL