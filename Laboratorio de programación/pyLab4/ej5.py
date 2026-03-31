"""5- Juego de adivinanza de números:
Genera un número aleatorio entre 1 y 100.
Pide al usuario que adivine el número.
Proporciona pistas al usuario si el número es demasiado alto o demasiado bajo.
Continúa solicitando al usuario que adivine hasta que lo haga correctamente.
Muestra el número de intentos necesarios para adivinar.
"""

from random import randint, random

aleatorio = randint(1, 100)
intentos = 0

while True:
    intentos += 1
    intentoUsuario = float(input("Ingrese su intento: "))

    if intentoUsuario == aleatorio:
        print(f"Correcto, el numero era {aleatorio}")
        print(f"Numero de intentos: {intentos}")
        break
    else:
        if intentoUsuario < aleatorio:
            print("El numero aleatorio es mayor")
        elif intentoUsuario > aleatorio:
            print("El numero aleatorio es menor")