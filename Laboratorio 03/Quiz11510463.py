#
# Quiz11510463.py
#
# DESCRIPCION: Programa que dados los valores del centro y radio de una 
# circunferencia y un punto (x1,y1) de coordenadas enteras, se desea 
# saber si el punto se encuentra dentro o fuera de dicha circunferencia. 
# El resultado se almacenara en la variable "resultado".
#
# Autor: 
#	Manuel Faria

# Variables:
# a: entero         // ENTRADA: Coordenada en el eje x del centro de la 
#								circunferencia.
# b: entero         // ENTRADA: Coordenada en el eje y del centro de la 
#								circunferencia.
# r: entero         // ENTRADA: Radio de la circunferencia.
# x1: entero        // ENTRADA: Coordenada en el eje x del punto a evaluar.
# y1: entero        // ENTRADA: Coordenada en el eje y del punto a evaluar.
# resultado: booleano // SALIDA: Variable donde se almacenará el resultado.

# Valores iniciales:
a = int(input("Coordenada en el eje x del centro de la circunferencia: "))
b = int(input("Coordenada en el eje y del centro de la circunferencia: "))
r = int(input("Radio de la circunferencia: "))
x1 = int(input("Coordenada en el eje x del punto a evaluar: "))
y1 = int(input("Coordenada en el eje x del punto a evaluar: "))
resultado = True

# Precondicion:
assert( a>=r and b>=r and r>=0 )

# Calculos:
if ((x1-a)**2 + (y1-b)**2) <= r**2: 
    pass
elif ((x1-a)**2 + (y1-b)**2) > r**2:
    resultado = False

# Postcondicion:
assert(
    (((x1-a)**2 + (y1-b)**2) > r**2 or resultado==True) and
    (((x1-a)**2 + (y1-b)**2) <= r**2 or resultado==False)
)

# Salida:
if resultado == True:
    print("El punto (",x1,",",y1,") pertenece a la circunferencia.")
else:
    print("El punto (",x1,",",y1,") NO pertenece a la circunferencia.")