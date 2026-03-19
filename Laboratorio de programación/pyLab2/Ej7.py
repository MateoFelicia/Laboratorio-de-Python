#7. Escribe un programa que recorra una cadena de 
#texto y cuente cuántas veces aparece la letra 'a' en la cadena.

palabra = input("Ingrese una palabra o frase: ")
contador_a = 0
for letra in palabra:
    if letra.lower() == 'a':
        contador_a += 1
print(f"La letra 'a' aparece {contador_a} veces en la cadena.")