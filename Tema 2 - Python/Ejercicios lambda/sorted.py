# Lista de tuplas (nombre, edad)
listaPersonas = [
    ("Ana", 25),
    ("Luis", 32),
    ("María", 19),
    ("Carlos", 40),
    ("Elena", 28)
]

# --------------------------------------------------
# Versión 1: usando una función definida (obtener_edad)
def obtener_edad(persona):
    return persona[1]

personas_ordenadas_funcion = sorted(listaPersonas, key=obtener_edad, reverse=True)
print("Ordenadas de mayor a menor edad usando función obtener_edad:")
print(personas_ordenadas_funcion)

# --------------------------------------------------
# Versión 2: usando una función lambda
personas_ordenadas_lambda = sorted(listaPersonas, key=lambda persona: persona[1], reverse=True)
print("Ordenadas de mayor a menor edad usando función lambda:")
print(personas_ordenadas_lambda)
