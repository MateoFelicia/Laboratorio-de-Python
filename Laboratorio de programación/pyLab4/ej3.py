"""3- Generador de secuencia Fibonacci:
Pide al usuario que ingrese un número entero positivo.
Genera los primeros n números de la secuencia Fibonacci, donde n es el número ingresado por el usuario.
Muestra la secuencia Fibonacci resultante.
"""

n = int(input("Ingrese un numero: "))
# n(x) = n(x-1) + n(x-2)
sequence = []

if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    sequence.append(0)  # n(0)
    if n > 1:
        sequence.append(1)  # n(1)
for i in range(2, n):
    next_number = sequence[i-1] + sequence[i-2]
    sequence.append(next_number)
    
print(f"Los primeros {n} números de la secuencia Fibonacci son: {sequence}")