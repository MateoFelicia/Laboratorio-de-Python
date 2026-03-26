palabra = input("Ingrese una palabra: ").lower()
palabraF = palabra.replace(" ", "") 

for letra in palabraF:
    if letra != palabraF[-1 - palabraF.index(letra)]: 
        print(f"{palabra} no es un palíndromo.")
        break
else:
    print(f"{palabra} es un palíndromo.")