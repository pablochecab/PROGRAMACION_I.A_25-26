
def gestion_inventario(accion, inventario, producto=None, cantidad=0):

    if accion == "agregar":

        # Si el producto existe, aumentamos su cantidad
        if producto in inventario:
            inventario[producto] += cantidad
            print("Cantidad actualizada")

        # Si el producto no existe, lo añadimos nuevo.
        else:
            inventario[producto] = cantidad
            print( f"Producto {producto} agregado. Cantidad total: {inventario[producto]}")

    elif accion == "eliminar":

        # Si el producto existe en el inventario.
        if producto in inventario:
            # Si la cantidad a quitar se puede quitar "que haya stock suficiente para quitar."
            if inventario[producto] >= cantidad:          
                inventario[producto] -= cantidad
                # Si llega a 0, borramos el producto directamente.
                if inventario[producto] == 0:
                    del inventario[producto]      
                print( f"Producto {producto} eliminado. Cantidad restante: {inventario.get(producto, 0)}")

            else:
                print( "Cantidad a eliminar excede la cantidad en inventario.")
        else:
            print( "Producto no encontrado en inventario.")

    elif accion == "buscar":
        # Si el producto existe
        if producto in inventario:
            print( f"Producto {producto} encontrado. Cantidad: {inventario[producto]}")
            
        else:
            print( "Producto no encontrado en inventario.")
            
    else:
        print("Acción no válida. Use 'agregar', 'eliminar' o 'buscar'.")

# Este es la variable inventario que necesitamos.
productos = {
    "Zumo": 50,
    "Manzana": 34,
    "Frutos secos": 7,
    "Carne": 1,
    "Pollo": 90
}

### Añadir:
# Añadimos un nuevo producto
gestion_inventario("agregar", productos, "Pera", 5)
print("NUEVO PRODUCTO AÑADIDO:", productos)

# Si el producto ya existe, aumentamos su cantidad:
gestion_inventario("agregar", productos, "Pera", 5)
print("CANTIDAD ACTUALIZADA", productos)

### Eliminar:
# Si el producto NO existe
gestion_inventario("eliminar", productos, "Albondigas", 5)
print("EL PRODUCTO NO EXISTE PARA ELIMINARLO", productos)

# Si el producto existe PERO la cantidad excede la posible:
gestion_inventario("eliminar", productos, "Pera", 11)
print("NO SE PUEDE QUITAR MÁS DE LO QUE REALMENTE HAY", productos)

# Si el producto existe y la cantidad es correcta:
gestion_inventario("eliminar", productos, "Pera", 9)
print("PRODUCTO ACTUALIZADO", productos)

# Si el producto existe y además se queda a 0:
gestion_inventario("eliminar", productos, "Zumo", 50)
print("PRODUCTO ELIMINADO", productos)

### Buscar
# Buscar el producto si existe:
gestion_inventario("buscar", productos, "Pera", 90)
print("PRODUCTO ENCONTRADO", productos)

# Si no existe:
gestion_inventario("buscar", productos, "Naranja", 5)
print("PRODUCTO NO ENCONTRADO", productos)

# Si el usuario utiliza otra acción:
gestion_inventario("reciclar", productos, "Pera", 5)
print("ACCION NO RECONOCIDA")

