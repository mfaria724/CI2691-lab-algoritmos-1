# Prelab7Ejemplo1.py
# DESCRIPCION: Ilustración de los comandos de entrada y salida en python
# Autor: 
#	Prof. Josué Ramírez
# Ultima modificacion: 22/05/2015
# Contenido de los archivos de entrada y salida workfile.txt y workfile2.txt:
	# Leyendo linea 1
	# Leyendo linea 2
	# Leyendo linea 3

#LECTURA DE 10 CARACTERES EN EL ARCHIVO "workfile.txt". EL ARCHIVO SE ABRE PARA LECTURA Y ESCRITURA ( r+ )
print("LECTURA DE 10 CARACTERES:")
f = open('workfile.txt', 'r+')
string = f.read(10)
print("El string leido es:",string)

                                                            ##########

#LECTURA LINEA POR LINEA EN EL ARCHIVO "workfile.txt"
print("\nLECTURA LINEA POR LINEA USANDO FOR:")
#La primera línea se lee a partir del caracter 11
for line in f:
	print(line, end="")
f.closed		

print("\nLECTURA LINEA POR LINEA USANDO f.readlines():")
f = open('workfile.txt','r+')
print(f.readlines())
#lineas = f.readlines()
#print("Las lineas del archivo son:", lineas)


															##########

#ESCRITURA Y LECTURA EN EL ARCHIVO "workfile.txt". SE AGREGA AL FINAL LO ESCRITO (se abrió con opción r+)
print("\nESCRITURA USANDO f.write Y LECTURA USANDO f.readlines():")
f.write("Escritura linea 4\n")
f.closed		

f = open('workfile.txt','r+')
lineas = f.readlines()
print("Las lineas del archivo luego de escribir son:", lineas)

#Convertir un valor a string y escribirlo al archivo
valor = [2, 3, 4]
s = str(valor)
f.write("La lista leida es:" + s +"\n")
f.closed		

f = open('workfile.txt','r+')
lineas = f.readlines()
print("\nLas lineas del archivo luego de escribir son:", lineas)
f.closed

															##########
															
#LECTURA EN EL ARCHIVO "workfile2.txt". Se abre con opción w lo cual sobreescribe el archivo anterior
print("\nESCRITURA USANDO with y f.write:")
with open('workfile2.txt', 'w') as f:
	f.write("\nLa lista leida es:" + s + "\n")
f.closed		

f = open('workfile2.txt','r+')
lineas = f.readlines()
print("Las lineas del archivo luego de escribir son:\n", lineas)

