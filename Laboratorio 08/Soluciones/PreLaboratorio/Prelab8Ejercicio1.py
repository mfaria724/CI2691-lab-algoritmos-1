#
# Prelab8ejercicio.py
#
# Descripcion: Programa que lee de un archivo con nombre “input.txt” una cadena ADN factorizada y
#              escribe en otro archivo “output.txt”, el resultado del ADN no-factorizado.
#
# Autores:  Prof. Rosseline Rodriguez y Prof. Saul Hidalgo
#
# Ultima modificacion: 26/03/2018

import sys

# CONSTANTES
ERROR = "Linea erronea\n" # MENSAJE DE ERROR.

def defactorizar( linea : str ) -> str:
  # PRECONDICION: la linea cumple con el formato establecido
  
  try:
    assert( len(linea.split()) == 2 )      # cada linea debe contener 2 palabras
    
    palabras = linea.split()
    numero = int( palabras[0] )            # la primera palabra es un numero
    assert( numero >= 0 and numero <= 50 ) # el numero debe ser no negativo y no mayor a 50
    
    # las letras de la palabra deben estar en el conjunto {A,T,C,G}
    adn = palabras[1]
    assert( all( (c == 'A' or c == 'T' or c == 'C' or c == 'G') for c in adn ) )
    
  except:
    return ERROR

  # CUERPO DE LA FUNCION.

  # La palabra del adn se multiplica por el numero de veces para crear la linea
  respuesta = adn * numero + "\n"
  
  # POSTCONDICION
  assert( respuesta == int(linea.split()[0]) * linea.split()[1] + "\n" )
  
  return respuesta


# PROGRAMA PRINCIPAL.

# PRECONDICION: el archivo existe y tiene el formato adecuado
try:
  # Se verifica que el archivo existe
  with open("input.txt") as entrada:
    lineas = entrada.readlines()
    
except:
  print("NO SE HA PODIDO LEER EL ARCHIVO input.txt")
  sys.exit()

try:
  # Se abre el archivo para escritura.
  with open("output.txt", "w") as salida:
    # se escriben las lineas defactorizadas
    for l in lineas:
      salida.write( defactorizar(l) )
      
except:
  print("NO SE HA PODIDO ESCRIBIR EL ARCHIVO output.txt")
  sys.exit()


# POSTCONDICION: Se creó el archivo output.txt con el resultado de la defactorizacion del ADN
