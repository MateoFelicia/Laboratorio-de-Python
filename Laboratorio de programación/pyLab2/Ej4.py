#4. Crear una lista de frutas y mostrar en consola
#algunas frutas de la lista, también por rebanadas.

lista = ["manzana", "banana", "naranja", "pera", "uva"]

for fruta in lista:
    print(fruta)
    mitad = len(fruta) // 2
    print(fruta[:mitad], "|", fruta[mitad:]) #Le tuve que preguntar al chat, lit el profe recien lo habia explicado
    