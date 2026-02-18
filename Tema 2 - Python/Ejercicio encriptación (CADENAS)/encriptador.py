import string

# Primero pedimos al usuario que introduzca la clave:
key = input("Introduce la clave, esta debe de contener más de 15 caractéres, mayúsculas, minúsculas, dígitos y especiales: ")

# -----------------------------
# VALIDADOR DE LA CLAVE. (Utilizo los guiones para distinguir que es una función)
# -----------------------------
def validator(key):
    # Verificamos la longitud con len.
    if len(key) < 15:
        return False
    # Comprobamos todas las restricciones aparte de la longitud.
    # Utilizamos "any" para buscar cualquier mayúscula, minúscula...
    # c es un valor temporal en donde se almacenará cada letra para comprobarla.
    has_upper = any(c.isupper() for c in key)
    has_lower = any(c.islower() for c in key)
    has_digit = any(c.isdigit() for c in key)
    has_special = any(c in string.punctuation for c in key)
    return has_upper and has_lower and has_digit and has_special

# Antes de pedir el mensaje, validamos que la clave sea correcta.
# Para ello hacemos que mientras la funcion validator no devuelva True, repetimos el bucle. "Todas deben ser true"
while not validator(key):
    print("Clave inválida. Debe cumplir todos los requisitos.")
    key = input("Introduce la clave nuevamente: ")

message = input("Introduce el mensaje a cifrar: ")

# -----------------------------
# Definimos las funciones de encriptamiento
# -----------------------------
def encriptar(message, key):
    # Primero debo de convertir el mensaje y la key a un array para poder manipularlos:
    # Quedarían así: ['H', 'o', 'l', 'a', 'M', 'u', 'n', 'd', 'o']
    message_list = list(message)
    key_list = list(key)

# Ahora empezamos con las permutaciones:
    # Convertir minúsculas a mayúsculas, hacemos un SWAP por cada palabra en el list de mensaje. "hOLA", por ejemplo.
    message_list = [letter.swapcase() for letter in message_list]
    # -----------------------------
    # Rotar las posiciones
    # -----------------------------
        
    
    # Invertir las posiciones
    message_list = message_list[::-1]

    # 

# Mutaciones
    # -----------------------------
    # Intercambiar una letra por su numero de aparición.
    # -----------------------------
    def switch(message_list):
        # Unimos el mensaje de nuevo.
        new_message.join(message_list)
    # Para cada letra en la lista
        for letter in message_list:
            # Contamos y guardamos las veces que aparece esa letra en el new message
            veces = new_message.count(letter)
            # Remplazamos la letra, por veces
            message_list.replace(letter, veces)
        return message_list

# Devolver como una cadena normal de nuevo
    
