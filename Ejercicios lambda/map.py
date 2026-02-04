lista = [1,2,3,4,5,6,7]

def triplicar(valores):
    listaDevolver = []
    for numero in valores:
        nuevoNumero = numero * 3
        listaDevolver.append(nuevoNumero)
    print("Lista multiplicada por 3: ", listaDevolver)
    return listaDevolver

triplicar(lista)