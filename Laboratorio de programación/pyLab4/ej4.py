"""4- Validador de contraseña:
Solicita al usuario que cree una contraseña.
Verifica si la contraseña cumple con los siguientes criterios:
Tiene al menos 8 caracteres de longitud.
Contiene al menos una letra mayúscula y una letra minúscula.
Tiene al menos un número.
Tiene al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.).
Informa al usuario si la contraseña es válida o no.
"""

contraseña = input("Ingrese una contraseña: ")

if len(contraseña) >= 8:
    longitud_valida = True
else:    
    longitud_valida = False

tiene_mayuscula = False
tiene_minuscula = False
tiene_numero = False
tiene_especial = False

especiales = "!@#$%&*"

# 3. Recorrer la contraseña
for c in contraseña:
    if c.isupper():
        tiene_mayuscula = True
    elif c.islower():
        tiene_minuscula = True
    elif c.isdigit():
        tiene_numero = True
    elif c in especiales:
        tiene_especial = True

# 4. Resultado final
if (longitud_valida and 
    tiene_mayuscula and 
    tiene_minuscula and 
    tiene_numero and 
    tiene_especial):
    
    print("Contraseña válida")
else:
    print("Contraseña inválida")