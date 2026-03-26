#4. Verificación de Palíndromos

palabra = input("Ingrese una palabra: ").lower()
palabraF = palabra.replace(" ", "") 

if palabraF == palabraF[::-1]: # Se compara con el reverso
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")
