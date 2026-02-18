class Timer:
    # CONSTRUCTOR. Creamos el objeto self con sus variables.
    def __init__(self, hora, minutos, segundos):
        print("Objeto creado")
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos
        

    # FUNCIÓN para poner los ceros a la izquierda.
    def formatear_tiempo(hora, minutos, segundos):
        # Convertimos a string y añadimos ceros si hace falta. zFill 2 digits.
        h = str(hora).zfill(2)
        m = str(minutos).zfill(2)
        s = str(segundos).zfill(2)
    
        return f"{h}:{m}:{s}"
    
    # LEGIBILIDAD
    def __str__(self):
        return Timer.formatear_tiempo(
            self.hora,
            self.minutos,
            self.segundos
        )
    
    def next_second(self):
        self.segundos += 1
        if self.segundos == 60:
            self.segundos = 0
            self.minutos += 1
            if self.minutos == 60:
                self.minutos = 0

    def prev_second(self):
        self.segundos -= 1
        if self.segundos == -1:
            self.segundos = 59
            self.minutos -= 1
            if self.minutos == -1:
                self.minutos = 59
    
# Crear objeto (LLama automáticamente al constructor __init__ para crearse)
t = Timer(9, 5, 3)

print(t)        
# Self se refiere a t.
t.next_second()
print(t)        
t.prev_second()
print(t)        

