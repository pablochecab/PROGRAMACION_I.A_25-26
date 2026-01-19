class Timer:
    # CONSTRUCTOR. Creamos el objeto self con sus variables.
    def __init__(self, hora, minutos, segundos):
        print("Objeto creado")
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos

    # FUNCIÓN para poner los ceros a la izquierda.
    def formatear_tiempo(hora, minutos, segundos):
        # Convertimos a string y añadimos ceros si hace falta
        h = str(hora).zfill(2)
        m = str(minutos).zfill(2)
        s = str(segundos).zfill(2)
    
        return f"{h}:{m}:{s}"

# Crear objeto (LLama automáticamente al constructor __init__)
t = Timer(9, 5, 3)

print(t)          # Llama automáticamente a __str__
print(t.hora)     # Acceso correcto al atributo
