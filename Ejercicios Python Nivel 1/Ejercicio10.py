n = int(input("Escribe un número: "))

# Inicializar la suma
suma = 0

# Calcular la serie
for i in range(1, N + 1):
    suma += 1 / i

# Redondear a 2 decimales
resultado = round(suma, 2)

# Mostrar el resultado
print("La suma de la serie es:", resultado)
