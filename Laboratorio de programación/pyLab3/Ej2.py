"""2. Definir función, parámetros, retorno,
capturar un valor o varios"""

def sumar(a, b):  # 1. función + 2. parámetros
    return a + b  # 3. retorno

# 4. capturar valores
x = int(input("Ingrese un número: "))
y = int(input("Ingrese otro número: "))

resultado = sumar(x, y)  # 5. llamar a la función con los valores capturados

print(f"Resultado: {resultado}")