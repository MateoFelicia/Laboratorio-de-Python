"""7- Calculadora de descuento de compra:
Solicita al usuario que ingrese el precio original del artículo y el porcentaje de descuento.
Calcula el precio final después del descuento.
Muestra el precio final al usuario.
"""

precioOriginal = float(input("Ingrese el precio original: "))
descuento = float(input("ingrese el descuento(ejemplo: 20): "))

d = descuento * 0.01
precioFinal = precioOriginal - precioOriginal * d

print(f"El precio final es {precioFinal}")