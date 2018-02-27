#
# Lab04Ejercicio3.py
#
# Descripcion: Dados los datos (nombre, edad, indice) de un grupo de estudiantes 
#              calcula el promedio de edad del grupo
#
# Autor:
#        Rosseline Rodriguez
#
# Ultima modificacion: 19/02/2018

# Libreria donde se localiza las funciones de numeros aleatorios
import random

# Definicion de la clase Estudiante
class Estudiante:
  nombre = ""
  edad = 0
  indice = 0
  notasDeParciales = []
  notaTotal = 0

# CONSTANTES:
#     P: int                             // cantidad de parciales
P = 4
  
# VARIABLES: 
#     N : int                            // ENTRADA: tamano de la lista
#     grupo: array [0..N) of Estudiante  // ENTRADA: lista de estudiantes
#     promEdad : int                     // SALIDA: promedio de edades
#     promxParcial: array [0..P) of int  // SALIDA: promedio por parcial
#     suma: int                          // suma de edades
#     sumaParciales: int                 // suma de las notas de los parciales de un estudiante
#     sumNotas: array [0..P) of int      // suma de las notas de todos los estudiantes en un parcial
#     k: int                             // variable de control para los ciclos 0..N 
#     l: int                             // variable de control para los ciclos 0..P
  
# VALORES INICIALES DE LAS VARIABLES DE ENTRADA:
N = int(input("Indique la cantidad de estudiantes: ")) 

grupo = [ Estudiante() for i in range(0,N) ] # Crea la lista de estudiantes con valores nulos

print("Introduzca los datos del grupo de estudiantes:")

# Cota: N-k

for k in range(0,N): # Lectura de los datos del grupo de estudiantes
  grupo[k].nombre = input( "Nombre del estudiante " + str(k) + ": " )
  grupo[k].edad = int(input( "Edad del estudiante " + str(k) + ": " ))
  grupo[k].indice = float(input( "Indice del estudiante " + str(k) + ": " ))
  
  # Valores aleatorios para las notas de los parciales
  grupo[k].notasDeParciales = [ random.randint(0,25) for j in range(0,P) ]

# PRECONDICION DEL PROGRAMA:
assert( 
   N > 0 and 
   all ( 
      len(grupo[i].nombre) > 0 and grupo[i].edad > 0 and 
	  1 <= grupo[i].indice <= 5 and
	  all (0 <= grupo[i].notasDeParciales[j] <= 25 for j in range (0,P))
   for i in range(0,N))
)

# CALCULOS
suma = 0
sumNotas = [0 for j in range(0,P)]
   
# Cota: N-k

for k in range(0,N):
  # Verificacion del invariante en cada iteracion
  assert( suma == sum( grupo[i].edad for i in range(0,k) )  and
   all ( 
	  (grupo[i].notaTotal==1 and ( 0 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) < 30)) or
	  (grupo[i].notaTotal==2 and (30 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) < 50)) or
	  (grupo[i].notaTotal==3 and (50 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) < 70)) or
	  (grupo[i].notaTotal==4 and (70 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) < 85)) or
	  (grupo[i].notaTotal==5 and (85 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) < 100)) 
	  for i in range(0,k)
   ) and
   all ( sumNotas[j] == sum( grupo[i].notasDeParciales[j] for i in range(0,k) ) for j in range (0,P))
  )

  suma = suma + grupo[k].edad
 
  sumaParciales = 0 

  # Cota: P-l
  for l in range(0,P):
    # Verificacion del invariante en cada iteracion
    assert( 
	    sumaParciales == sum( grupo[k].notasDeParciales[j] for j in range(0,l) ) and
        all ( sumNotas[j] == sum( grupo[i].notasDeParciales[j] for i in range(0,k+1) ) for j in range (0,l))
    )

    sumaParciales = sumaParciales + grupo[k].notasDeParciales[l] 
	
    sumNotas[l] = sumNotas[l] + grupo[k].notasDeParciales[l] 

  # Postcondicion del ciclo interno
  assert( 
     sumaParciales == sum( grupo[k].notasDeParciales[j] for j in range(0,P) ) and
     all ( sumNotas[j] == sum( grupo[i].notasDeParciales[j] for i in range(0,k+1) ) for j in range (0,P))
  )

  if sumaParciales < 30:
    grupo[k].notaTotal = 1
  elif sumaParciales < 50:
    grupo[k].notaTotal = 2
  elif sumaParciales < 70: 
    grupo[k].notaTotal = 3
  elif sumaParciales < 85: 
    grupo[k].notaTotal = 4
  else:  
    grupo[k].notaTotal = 5
	

# Postcondicion del ciclo externo
assert(
   suma == sum( grupo[i].edad for i in range(0,N) ) and
   all ( 
	  (grupo[i].notaTotal==1 and ( 0 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) <30)) or
	  (grupo[i].notaTotal==2 and (30 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) <50)) or
	  (grupo[i].notaTotal==3 and (50 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) <70)) or
	  (grupo[i].notaTotal==4 and (70 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) <85)) or
	  (grupo[i].notaTotal==5 and (85 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) < 100)) 
	  for i in range(0,N)
   ) and
   all ( sumNotas[j] == sum( grupo[i].notasDeParciales[j] for i in range(0,N) ) for j in range (0,P))
)

promEdad = suma/N

promXParcial = [0 for j in range(0,P)]

# Cota: P-l
for l in range(0,P):
   # Verificacion del invariante en cada iteracion
   assert( all (promXParcial[j] == sumNotas[j]/N for j in range (0,l)) )
   
   promXParcial[l] = sumNotas[l]/N

# Postcondicion del ciclo
assert( all (promXParcial[j] == sumNotas[j]/N for j in range (0,P)) )
   
# POSTCONDICION DEL PROGRAMA:
assert(
   promEdad == sum( grupo[i].edad for i in range(0,N) ) / N and
   all ( 
	  (grupo[i].notaTotal==1 and ( 0 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) < 30)) or
	  (grupo[i].notaTotal==2 and (30 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) < 50)) or
	  (grupo[i].notaTotal==3 and (50 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) < 70)) or
	  (grupo[i].notaTotal==4 and (70 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) < 85)) or
	  (grupo[i].notaTotal==5 and (85 <= sum( grupo[i].notasDeParciales[j] for j in range(0,P)) < 100)) 
	  for i in range(0,N)
   ) and
   all (promXParcial[j] == sum( grupo[i].notasDeParciales[j] for i in range(0,N) )/N for j in range (0,P))
)

# SALIDAS:
print( "El promedio de las edades del grupo es: " + str(promEdad) )

for k in range(0,N):
   print("Nota Total del estudiante " + str(k) + ": " + str(grupo[k].notaTotal) ) 

for l in range(0,P):
   print("El promedio para el parcial " + str(l+1) + ": " + str(promXParcial[l]) ) 



