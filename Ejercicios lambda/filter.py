numeros = [4, 8, 10, 12, 15, 18, 22, 3, 7, 14]

# --------------------------------------------------
# Versión 1: usando una función definida (condicion)
def condicion(n):
    return n % 2 == 0 and n > 10

resultado_funcion = list(filter(condicion, numeros))
print("Resultado usando función condicion:")
print(resultado_funcion)

# --------------------------------------------------
# Versión 2: usando una función lambda
resultado_lambda = list(filter(lambda n: n % 2 == 0 and n > 10, numeros))
print("Resultado usando función lambda:")
print(resultado_lambda)

# --------------------------------------------------
# Versión 3: usando comprensión de listas
resultado_comprension = [n for n in numeros if n % 2 == 0 and n > 10]
print("Resultado usando comprensión de listas:")
print(resultado_comprension)
