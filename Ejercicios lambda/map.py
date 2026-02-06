# Lista de números enteros
numeros = [1, 2, 3, 4, 5]

# Versión 1: usando una función definida
def incrementa(n):
    return n * 3

resultado_funcion = list(map(incrementa, numeros))
print("Resultado usando función incrementa:")
print(resultado_funcion)

# Versión 2: usando una función lambda
resultado_lambda = list(map(lambda n: n * 3, numeros))
print("Resultado usando función lambda:")
print(resultado_lambda)
