
#1- Calculadora de índice de masa corporal (IMC):

#- Solicita al usuario que ingrese su peso en kg y su altura en metros.
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

#- Calcula el IMC utilizando la fórmula: IMC = peso / (altura * altura).
imc = peso / (altura * altura)

#- Muestra el IMC calculado y una categoría de peso según el IMC (talla s, talla m, talla l, talla xl).
print(f"Tu IMC es: {imc:.2f}") #Mostramos hasta centecimas

if imc < 18.5:
    print("Tienes bajo peso.")
elif 18.5 <= imc < 25:
    print("Tienes un peso normal.")
elif 25 <= imc < 30:
    print("Tienes sobrepeso.")
else:
    print("Tienes obesidad.")