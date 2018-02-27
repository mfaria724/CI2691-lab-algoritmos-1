#
# Lab02Ejercicio1.py
#
# DESCRIPCION: Programa para determinar si una persona puede votar
#
# Autor: 
#	Kevin Mena

# Variables:
# esDescendienteExtranjero: booleano // ENTRADA: Para saber si la persona es descendiente o no
# edad: entero                       // ENTRADA: La edad de la persona
# puedeVotar: booleano               // SALIDA: Indica si puede o no votar la persona

# Valores iniciales:
esDescendienteExtranjero = int(input("Si la persona es descendiente extranjero coloque '1', \
sino coloque '0': "))
edad = int(input("Indique la edad de la persona: "))
puedeVotar = True

# Precondicion:
assert(0 < edad and edad < 120)

# Calculos:

if (esDescendienteExtranjero == 1):
    if (edad >= 25): pass
    else:
        puedeVotar = False
else:
    if (edad >= 18): pass
    else:
        puedeVotar = False

# Postcondicion:
assert(
    puedeVotar == ((esDescendienteExtranjero == 1 and edad>=25) or (esDescendienteExtranjero == 0 and edad >= 18))
)

# Salida:
if puedeVotar == True:
    print("La persona puede votar")
else:
    print("La persona no puede votar")