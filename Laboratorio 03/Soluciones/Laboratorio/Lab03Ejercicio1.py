#
# Lab02Ejercicio1.py
#
# DESCRIPCION: Programa que presenta un menú de tres opciones 
# (1: Superficie de una habitación; 2: Área de una circunferencia; 
# 3: Suma de cuadrados). Si se selecciona la opción 1, se solicita 
# el largo y ancho de una habitación y muestra la superficie de esta 
# con cuatro digitos decimales. Si se selecciona la opcion 2, se 
# solicita el radio de la circunferencia, y muestra el area de la misma. 
# Si se selecciona la opcion 3, se solicita un numero natural n, y 
# produce como resultado el valor de la suma de los cuadrados de 1 a n.
#
# Autor: 
#	Rosseline Rodriguez
#
# Ultima modificacion: 03/02/2018

# Variables:
#	 opc: int;          // ENTRADA: opcion seleccionada
#    largo: float;      // ENTRADA: largo de la habitacion
#    ancho: float;      // ENTRADA: ancho de la habitacion
#    radio: float;      // ENTRADA: radio de la circunferencia
#    n: int;            // ENTRADA: natural para la suma de cuadrados
#	 superficie: float; // SALIDA: superficie de la habitacion
#	 area: float;       // SALIDA: area de la circunferencia
#	 suma: int;         // SALIDA: suma de cuadrados
#	 k: int;            // Variable de control del ciclo

# Menu de opciones:
print("(1) Superficie de una habitacion")
print("(2) Area de una circunferencia")
print("(3) Suma de cuadrados")

# Valores iniciales:
opc = int(input("Introduzca una opcion (1-3): "))
largo = 0.0
ancho = 0.0
radio = 0.0
n = 0
superficie = 0.0
area = 0.0
suma = 0

# Precondicion:
assert(opc == 1 or opc == 2 or opc == 3)

# Calculos:
if (opc == 1): 
    # Entrada:
    largo = float(input("Largo: "))
    ancho = float(input("Ancho: "))
	
    # Precondicion:
    assert(largo >= 0 and ancho >= 0)
	
    superficie = largo*ancho
    # Salida:
    print("La superficie es ", superficie)

elif (opc == 2):
    # Entrada:
    radio = float(input("Radio: "))
    area = 3.1416*radio**2

    # Precondicion:
    assert(radio >= 0)

    # Salida:
    print("El area es ", area)

else:
    # Entrada:
    n = int(input("n: "))

    # Precondicion:
    assert(n > 0)

    suma,k = 0,0
    cota = n+1-k
	
    #Verificacion de invariante al inicio del ciclo
    assert(0<=k<=n+1 and suma == sum( i**2 for i in range(0,k)))
    assert(cota >= 0)
	  
    while (k<=n):
	    suma,k = suma + k*k, k+1
		
	    #Verificacion de invariante y cota en cada iteracion	    
	    assert(0<=k<=n+1 and suma == sum( i**2 for i in range(0,k)))
	    assert(cota > n+1-k)
	    cota = n+1 - k
	    assert(cota >= 0)
	 
    # Salida:
    print("La suma de cuadrados es ", suma)

# Postcondicion:
assert(
    (opc == 1 and superficie == largo*ancho) or 
	(opc == 2 and area == 3.1416*radio*radio) or 
	(opc == 3 and suma == sum( i**2 for i in range(0,n+1)))
)
