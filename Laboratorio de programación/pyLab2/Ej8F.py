# 8. Integrador:
#Escribe un programa que permita a un usuario crear
#una lista de nombres.
#El programa continuará pidiendo
#nombres hasta que el usuario ingrese "fin".
#Luego, el programa mostrará la lista de nombres en orden alfabético,
#indicará cuántos nombres empiezan con la letra 'A' o 'E', 
#y mostrará si un nombre específico está en la lista.
import os
os.system('cls')

nombres = []


#Escribe un programa que permita a un usuario crear
#una lista de nombres.
#El programa continuará pidiendo
#nombres hasta que el usuario ingrese "fin".
while True:
    entradaUsuario = input("Ingrese un nombre: ").lower()
    if entradaUsuario == "fin": #Me habia olvidado las comillas ja
        break
    else:
        nombres.append(entradaUsuario)

#Luego, el programa mostrará la lista de nombres en orden alfabético,
nombres.sort()
print(f"La lista de nombres es: {nombres}")

#indicará cuántos nombres empiezan con la letra 'A' o 'E', 
contadorAE = 0
for nombre in nombres:
    if nombre[0] == "a" or nombre[0] == "e":
        contadorAE += 1

print(f"La cantidad de nombres que empiezan con e y/o a es {contadorAE}")


#y mostrará si un nombre específico está en la lista.


nombreEspecifico = input("Ingrese un nombre para verificar si está en la lista: ").lower()
if nombreEspecifico in nombres:
    print(f"{nombreEspecifico} está en la lista.")
else:
    print(f"{nombreEspecifico} no está en la lista.")
