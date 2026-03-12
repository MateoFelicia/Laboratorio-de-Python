"""8.  crearemos un programa que verifica si
un número ingresado por el usuario es positivo,
negativo o cero, y también si es un número par o impar."""


nro = int(input("Ingrese un número: "))

if nro > 0:
    print("El número es positivo.")
elif nro < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

if nro % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
