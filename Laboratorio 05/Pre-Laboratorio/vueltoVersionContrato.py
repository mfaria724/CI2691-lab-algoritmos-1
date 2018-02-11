#
# vueltoVersionContrato.py
#
# Descripcion:
# Al realizar una compra en efectivo, es necesario dar el vuelto al comprador.
# Para dar el vuelto se dispone de billetes de 10, 5 y 2, asi como monedas de 1.
# Dado el monto de una compra y del pago, se debe calcular el vuelto y entregarlo
# con el numero minimo posible de billetes y monedas. Los montos de compra y de
# pago son redondos (sin centimos). Se desea solicitar al usuario los montos de
# una compra y del pago, y calcular el vuelto, en su desglose optimo.
#
# Autor: Saul Hidalgo
#
# Ultima modificacion: 07/02/2018
#

import sys    # Se importa la libreria sys para poder utilizar sys.exit()

# CONSTANTES:
BLL_ALTO = 100 # Valor del billete de denominacion alta
BLL_MEDIO = 50 # Valor del billete de denominacion media
BLL_BAJO = 2  # Valor del billete de denominacion baja

# VARIABLES
#   compra: int        // Entrada: monto de la compra
#   pago: int          // Entrada: monto del pago realizado
#   cnt_bll_alto: int  // Salida: Cantidad de billetes de denominacion alta
#   cnt_bll_medio: int // Salida: Cantidad de billetes de denominacion media
#   cnt_bll_bajo: int  // Salida: Cantidad de billetes de denominacion baja
#   cnt_monedas: int   // Salida: Cantidad de monedas

# Valores iniciales
compra = 0    
pago = 0      

# Verificacion de la Precondicion (version por contrato)

try: 
   compra = int(input("Indique el monto de la compra: "))
   pago = int(input("Indique el monto del pago: "))
   assert( compra > 0 and pago >= compra )
except:
   print("Error en los datos de entrada")
   print("Los valores deben ser positivos, y pago mayor o igual que compra")
   sys.exit() # Se aborta el programa pues no cumple la precondicion (el contrato)

# El algoritmo basicamente consiste en 
# tomar la mayor cantidad de billetes de alta demonimacion
# luego los de media denominacion, y finalmente los de 
# baja denominacion. El resto se devolvera en monedas.

# Calculos
vuelto = pago - compra
cnt_monedas = vuelto

cnt_bll_alto = cnt_monedas // BLL_ALTO
cnt_monedas = cnt_monedas % BLL_ALTO

cnt_bll_medio = cnt_monedas // BLL_MEDIO
cnt_monedas = cnt_monedas % BLL_MEDIO

cnt_bll_bajo = cnt_monedas // BLL_BAJO
cnt_monedas = cnt_monedas % BLL_BAJO

# Postcondicion
try:
  assert( vuelto == pago - compra and
          vuelto == cnt_bll_alto * BLL_ALTO 
                +   cnt_bll_medio * BLL_MEDIO 
                +   cnt_bll_bajo * BLL_BAJO
                +   cnt_monedas 
          and (0 <= cnt_bll_alto)
          and (0 <= cnt_bll_medio) and (cnt_bll_medio*BLL_MEDIO < BLL_ALTO)
          and (0 <= cnt_bll_bajo) and (cnt_bll_bajo*BLL_BAJO < BLL_MEDIO)
          and (0 <= cnt_monedas) and (cnt_monedas < BLL_BAJO) )
except:
  print("Error en los calculos") 
  print("No se cumple la postcondicion con los valores ")
  print("  vuelto = " + str(vuelto))
  print("  pago = " + str(pago))
  print("  compra = " + str(compra))
  print("  cnt_bll_alto = " + str(cnt_bll_alto))
  print("  cnt_bll_medio = " + str(cnt_bll_medio))
  print("  cnt_bll_bajo = " + str(cnt_bll_bajo))
  print("  cnt_monedas = " + str(cnt_monedas))
  sys.exit() # Se aborta el programa, pues no cumple la postcondicion (el contrato)

# Salida 

print("El vuelto es: " + str(vuelto))
print("\nRepartido en:\n")
print(str(cnt_bll_alto) + " billetes de " + str(BLL_ALTO))
print(str(cnt_bll_medio) + " billetes de " + str(BLL_MEDIO))
print(str(cnt_bll_bajo) + " billetes de " + str(BLL_BAJO))
print(str(cnt_monedas) + " monedas ")

