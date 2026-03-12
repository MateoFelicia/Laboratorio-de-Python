# Pedir al usuario que ingrese su nombre
# Pedir al usuario que ingrese su edad
# Pedir al usuario que ingrese su ciudad de residencia
# Calcular el año de nacimiento
# Saludar al usuario y mostrar la información
# Comprobar si la edad es mayor de 18 años
# Comprobar si la edad es un múltiplo de 5

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: ")) 
ciudad = input("Ingrese su ciudad de residencia: ")
año_nacimiento = 2026 - edad

print(f"Hola, {nombre}! \n pie de pagina ")
print(f"Tu edad es: {edad}")
print(f"Vives en: {ciudad}")
print(f"Tu año de nacimiento es: {año_nacimiento}")

if edad > 18:
    print("Eres mayor de 18 años.")
else:
    print("No eres mayor de 18 años.")

if edad % 5 == 0:
    print("Tu edad es un múltiplo de 5.")
else:
    print("Tu edad no es un múltiplo de 5.")
