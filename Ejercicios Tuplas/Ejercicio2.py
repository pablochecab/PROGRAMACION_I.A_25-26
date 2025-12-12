# Vamos a recorrer cada valor del diccionario, y de ese valor, el cual es una tupla,
# trataremos de calcular la media sumando sus componentes y dividiendo entre su longitud.

def calculadorMedia(notas):
    for asignatura, nota in notas.items():
        media = sum(nota) / len(nota)
        print(f"La media de {asignatura} es: {media:.2f}")


# Creamos un diccionario que dentro contiene las tuplas con todas las notas.
notas = {
    "Lengua": (5, 9, 9),
    "Matemáticas": (6, 9, 6),
    "Física": (3, 5, 4),
    "Inglés": (5, 5, 5)
}

print("Las notas de Pedro son:\n", notas)

calculadorMedia(notas)
