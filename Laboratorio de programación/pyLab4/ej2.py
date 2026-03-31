"""2- Conversor de temperaturas:
Pide al usuario que ingrese una temperatura en grados Celsius.
Convierte la temperatura a grados Fahrenheit utilizando la fórmula: Fahrenheit = (Celsius * 9/5) + 32.
Imprime la temperatura en grados Fahrenheit."""

Celsius = float(input("Ingrese los grados en C: "))
Fahrenheit = (Celsius * 9/5) + 32

print(f"En farenheit, tus {Celsius} Celsius son {Fahrenheit} Fahrenheit")