palabra = input("Ingrese una palabra: ").lower()
palabraF = palabra.replace(" ", "")

for i in range(len(palabraF) // 2): # Solo se necesita revisar hasta la mitad
    if palabraF[i] != palabraF[-i - 1]: # Compara el carácter actual con su contraparte desde el final
        print(f"{palabra} no es un palíndromo.")
        break
else:
    print(f"{palabra} es un palíndromo.")