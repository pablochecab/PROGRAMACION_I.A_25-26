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
    #C    #VALOR -> CLAVE      #VALOR
    1: {'disponible': False,
        'usuario': 'Pepe' },
    2: {'disponible': True,
        'usuario': None },
    3: {'disponible': False,
        'usuario': 'Ana' }
}


print(prestamos[1].values())
