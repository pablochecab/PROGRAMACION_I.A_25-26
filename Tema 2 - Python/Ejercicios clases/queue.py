class QueueError(IndexError):        
    pass
    
    def lanzarMensaje():
        return "Mensaje de error lanzado desde QueueError"

class Queue:
    
    # CONSTRUCTOR
    def __init__(self, lista):
        self.lista = lista
    
    # LEGIBILIDAD
    def __str__(self):
        return str(self.lista)
    
    def put(self, numero):
        self.lista.insert(0, numero)
        return self
    
    def get(self):
        try:
            if len(self.lista) != 0:
                self.lista.pop()
        except QueueError as qE:
            qE.lanzarMensaje()
        return self
        
# self se refiere al objeto que está llamando a la función.

lista = Queue([1, 2, 3, 4, 5])
listaVacia = Queue([])

lista.put(9)
print(lista)
lista.get()
print(lista)

listaVacia.get()
