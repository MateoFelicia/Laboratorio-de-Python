#5.2 Escribe un programa verifique si una fruta 
#específica está en una lista de frutas y muestra
#un mensaje correspondiente.

lista = ["manzana", "banana", "naranja", "pera", "uva"]
frutaUsuario = input("Ingrese el nombre de una fruta: ").lower()
if frutaUsuario in lista:
    print(f"{frutaUsuario} está en la lista.")
else:
    print(f"{frutaUsuario} no está en la lista.")