#6. Escribe un programa que recorra una lista
#de números y muestre si cada número es par o impar.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista_numeros:
    if numero % 2 == 0:
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")