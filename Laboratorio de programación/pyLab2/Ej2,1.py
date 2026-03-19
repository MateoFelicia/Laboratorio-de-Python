# 2.1. Escribe un programa que solicita al usuario
#que ingrese números enteros positivos y muestre
#la suma de esos números. La entrada de números
#continuará hasta que el usuario ingrese un 
#número negativo, momento en el que el programa 
#mostrará la suma total.

suma = 0
while True:
    nro = int(input("Dame un número: "))
    if nro < 0:
        break
    suma += nro
print(f"La suma total es: {suma}")