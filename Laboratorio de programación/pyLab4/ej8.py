"""8- Generador de contraseñas aleatorias:
Solicita al usuario que ingrese la longitud deseada para la contraseña.
Genera una contraseña aleatoria con la longitud especificada.
Utiliza caracteres alfanuméricos y caracteres especiales para mayor seguridad.
Muestra la contraseña generada al usuario.
"""

import random
import string

longitud = int(input("ingrese la longitud deseada: "))

caracteres = string.ascii_letters + string.digits + string.punctuation
contraseña = ''.join(random.sample(caracteres, longitud)) #Entre los caracteres, elegimos caracteres randoms
print(f"Contraseña generada: {contraseña}")