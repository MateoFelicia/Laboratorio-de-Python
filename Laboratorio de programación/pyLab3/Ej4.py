#4. Verificación de Palíndromos

palabra = input("Ingrese una palabra: ").lower()

"""if palabra == palabra[::-1]:
    print(f"{palabra} es un palíndromo."""
    
for letra in palabra:
    if letra != palabra[-1 - palabra.index(letra)]:
        
        print(f"{palabra} no es un palíndromo.")
        break
else:
    print(f"{palabra} es un palíndromo.")