#3.Escribe un programa que muestra la primer,
#última u otra letra de una cadena de carcateres,
#inclusive una rebanada.

palabra = input("Ingrese una palabra: ")
print(f"La primera letra es: {palabra[0]}")
print(f"La última letra es: {palabra[-1]}")
print(f"Una letra en el medio es: {palabra[len(palabra)//2]}") #Asi da entero
print(f"Una rebanada de la palabra es: {palabra[0:3]}") 
