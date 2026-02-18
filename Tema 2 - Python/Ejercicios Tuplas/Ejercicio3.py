def traducir(textoUsuario):
    # Aquí estoy recibiendo un texto plano, necesito pasarlo a una lista, tupla... algo (split)
    listTexto = textoUsuario.split(" ")
    print("Texto con espacios: ", listTexto)
    # Una vez lo tenga de esa forma, podré comparar los valores, buscando por la key
    # Si coincide, generaremos una nueva lista utilizando append, posteriormente la transformaremos a String y la devolvemos.
    listaDevolver = []

    # Recorremos cada palabra del texto
    for palabra in listTexto:
        # Si la palabra está en el diccionario, usamos su traducción
        if palabra in traductor:
            palabraTraducida = traductor[palabra]
        else:
            palabraTraducida = palabra  # Si no está, dejamos la palabra tal cual
        # La añadimos a la lista a devolver
        listaDevolver.append(palabraTraducida)
        
        resultado = " ".join(listaDevolver)

    return resultado;


traductor = {
    'Hola': "Hello",
    'soy': "im",
    'pablo': "Paul",
    # Como 'y' seria "and" y este está reservado, vamos a no ponerla.
    'tengo': "I Have",
    'años': "years"
}


textoUsuario = input("Escribe una frase: ")

print("Texto traducido: ", traducir(textoUsuario))
