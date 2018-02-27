#
# Prelab4Ejercicio5.py
#
# Descripcion: Dados los datos (nombre, edad, indice) de un grupo de estudiantes 
#              calcula el promedio de edad del grupo
#
# Autor:
#        Rosseline Rodriguez
#
# Ultima modificacion: 06/02/2018

# Definicion de la clase Estudiante
class Estudiante:
  nombre = ""
  edad = 0
  indice = 0

# Variables: 
#     N : int                            // ENTRADA: tamano de la lista
#     grupo: array [0..N) of Estudiante  // ENTRADA: lista de estudiantes
#     promedio : int                     // SALIDA: promedio de edades
#     suma : int                         // suma de edades
#     k : int                            // variable de control del ciclo 

  
# Valores iniciales
N = int(input("Indique la cantidad de estudiantes: ")) 
grupo = [ Estudiante() for x in range(N) ] #crea el arreglo de estudiantes

print("Introduzca los datos del grupo de estudiantes:")

for k in range(0,N): # Lectura de los datos del grupo de estudiantes
  grupo[k].nombre = input( "Nombre del estudiante " + str(k) + ": " )
  grupo[k].edad = int(input( "Edad del estudiante " + str(k) + ": " ))
  grupo[k].indice = float(input( "Indice del estudiante " + str(k) + ": " ))


# Precondicion 
assert( N > 0 and all ( len(grupo[i].nombre) > 0 and grupo[i].edad > 0 and 1 <= grupo[i].indice <= 5 for i in range(0,N)))

# Calculos
suma = 0

# Cota: C = N - k

for k in range(0,N):
  # Verificacion del invariante en cada iteracion
  assert( suma == sum( grupo[i].edad for i in range(0,k) ) )
  suma = suma + grupo[k].edad

# Postcondicion del ciclo
assert(suma == sum( grupo[i].edad for i in range(0,N) ) )

promedio = suma/N

# Postcondicion del programa
assert(promedio == sum( grupo[x].edad for x in range(0,N) ) / N )

print( "El promedio de las edades del grupo es: " + str(promedio) )


