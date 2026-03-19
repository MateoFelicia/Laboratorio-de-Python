#5.1 Agregar otras frutas a la lista.
import os
os.system("cls")

lista = ["manzana", "banana", "naranja", "pera", "uva"]

for fruta in lista:
    print(fruta)
    
while True:
    fruta_nueva = input("Ingrese una nueva fruta: ")
    if fruta_nueva == "0":
        break
    else:
        
        lista.append(fruta_nueva)
        print(f"Lista actualizada: {lista}")