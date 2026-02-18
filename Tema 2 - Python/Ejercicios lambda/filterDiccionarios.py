# Diccionario de productos y precios
productos = {
    "Teclado": 30,
    "Ratón": 20,
    "Monitor": 150,
    "Impresora": 80,
    "USB": 10,
    "Auriculares": 60
}

# --------------------------------------------------
# Usando filter y list
# items() devuelve pares (producto, precio)

resultado = list(filter(lambda item: item[1] > 50, productos.items()))

print("Productos con precio mayor de 50:")
print(resultado)
