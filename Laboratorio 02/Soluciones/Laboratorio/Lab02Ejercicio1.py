#
# Lab02Ejercicio1.py
#
# DESCRIPCION: Programa para calcular si un año es bisiesto
#
# Autor: 
#	Kevin Mena

# Variables:
# anyo: entero         // ENTRADA: año a ser verificado
# esBisiesto: booleano // SALIDA: saber si es bisiesto o no

# Valores iniciales:
anyo = int(input("Introduzca el año a verificar: "))
esBisiesto = True

# Precondicion:
assert(anyo > 0)

# Calculos:
if (anyo % 4 == 0 and anyo % 100 != 0): 
    pass
elif (anyo % 400 == 0):
    pass
else:
    esBisiesto = False

# Postcondicion:

assert(
    esBisiesto == (anyo % 4 == 0 and anyo % 100 != 0 or anyo % 400 == 0)
)

# Salida:

if esBisiesto == True:
    print("El año", anyo, "es bisiesto")
else:
    print("El año", anyo, "no es bisiesto")