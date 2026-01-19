def gestion_prestamos(accion, prestamos, libro_id=None, usuario=None):

    if accion == "prestar":
        if libro_id in prestamos:
            if prestamos[libro_id]["disponible"]:
                prestamos[libro_id]["disponible"] = False
                prestamos[libro_id]["usuario"] = usuario
                print( f"Libro {libro_id} prestado a {usuario}.")
            else:
                print( f"Libro {libro_id} no disponible.")
        else:
            prestamos[libro_id] = {"disponible": False, "usuario": usuario}
            print( f"Libro {libro_id} agregado y prestado a {usuario}.")

    elif accion == "devolver":
        if libro_id in prestamos:
            if not prestamos[libro_id]["disponible"]:
                prestamos[libro_id]["disponible"] = True
                usuario_devuelto = prestamos[libro_id]["usuario"]
                prestamos[libro_id]["usuario"] = None
                print( f"Libro {libro_id} devuelto por {usuario_devuelto}.")

            else:
                print( f"Libro {libro_id} ya estaba disponible.")

        else:
            print( "Libro no encontrado en el sistema.")


    elif accion == "consultar":
        if libro_id in prestamos:
            estado = "disponible" if prestamos[libro_id]["disponible"] else f"prestado a {prestamos[libro_id]['usuario']}"
            print( f"Libro {libro_id} está {estado}.")
        else:
            print( "Libro no encontrado en el sistema.")

    else:
        print( "Acción no válida. Use 'prestar', 'devolver' o 'consultar'.")


prestamos = {
    1: {'disponible': False, 'usuario': 'Pepe'},
    2: {'disponible': True, 'usuario': None},
    3: {'disponible': False, 'usuario': 'Ana'}
}

# CASOS DE PRUEBA

print("\n--- PRESTAR ---")

# 1. Prestar un libro disponible (ID = 2)
gestion_prestamos("prestar", prestamos, 2, "Juan")
print("Estado actual:", prestamos[2])

# 2. Intentar prestar un libro ya prestado (ID = 1)
gestion_prestamos("prestar", prestamos, 1, "Luis")
print("Estado actual:", prestamos[1])

# 3. Prestar un libro nuevo que no existe en el sistema (ID = 4)
gestion_prestamos("prestar", prestamos, 4, "Maria")
print("Estado actual:", prestamos[4])

print("\n--- DEVOLVER ---")

# 4. Devolver un libro que está prestado (ID = 1)
gestion_prestamos("devolver", prestamos, 1)
print("Estado actual:", prestamos[1])

# 5. Devolver un libro que ya está disponible (ID = 2)
gestion_prestamos("devolver", prestamos, 2)
print("Estado actual:", prestamos[2])

# 6. Devolver un libro que no existe en el sistema (ID = 5)
gestion_prestamos("devolver", prestamos, 5)

print("\n--- CONSULTAR ---")

# 7. Consultar estado de un libro disponible (ID = 2)
gestion_prestamos("consultar", prestamos, 2)

# 8. Consultar estado de un libro prestado (ID = 3)
gestion_prestamos("consultar", prestamos, 3)

# 9. Consultar libro no existente (ID = 6)
gestion_prestamos("consultar", prestamos, 6)

print("\n--- ACCIÓN INVÁLIDA ---")

# 10. Acción inválida
gestion_prestamos("perder", prestamos, 1)
