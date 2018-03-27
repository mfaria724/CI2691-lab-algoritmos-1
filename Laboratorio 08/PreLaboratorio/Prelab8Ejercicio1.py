# Prelab8Ejercicio1.py
#
# DESCRIPCION: Programa que decripta una archivo de entrada con especificaciones
# de ADN.
#
# Autor: 
#	Manuel Faria 15-10463
# 
# Ultima modificacion: 26/02/2018
#
# Contenido del archivo input.txt
	# 1 A
	# 5 ATCA
	# 0 CCC
	# -1 A
	# 10 SA
	# 51 ATCG
	# 2 T

#LECTURA LINEA POR LINEA EN EL ARCHIVO "workfile.txt"
print("\nLECTURA LINEA POR LINEA USANDO FOR:")
f = open('input.txt', 'r+')
for line in f:
	linea = line.split()
	print('')

	letras = linea[1].split()
	print(letras)

	if int(linea[0]) < 1 or int(linea[0]) >= 50:
		print('Línea Erronea')
	else:		
		for i in range(int(linea[0])):
			print(linea[1],end='')

print('')
f.closed		
