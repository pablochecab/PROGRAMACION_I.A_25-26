import math  # Importamos el módulo math para usar la función hypot

class Point:

    """ CONSTRUCTOR """
    def __init__(self, x, y):

        # Guardamos las coordenadas como atributos privados
        # El doble guion bajo evita el acceso directo desde fuera de la clase
        self.__x = float(x)
        self.__y = float(y)

    """ GETTER DEL PUNTO X """
    def getx(self):     
        return self.__x

    """ GETTER DEL PUNTO Y """
    def gety(self):
        return self.__y

    """ FUNCIÓN PASANDO LOS ATRIBUTOS """
    def distance_from_xy(self, x, y):

        # Restamos las coordenadas para obtener los lados
        px = self.__x - x  # Diferencia en el eje X
        py = self.__y - y  # Diferencia en el eje Y
        
        return math.hypot(px, py)

    """ FUNCIÓN PASANDO EL OBJETO ENTERO """
    def distance_from_point(self, point):
 
        # Obtenemos las coordenadas del otro punto usando sus métodos
        x = self.__x - point.getx()
        y = self.__y - point.gety()
        
        return math.hypot(x, y)


# PRUEBAS 

# Creamos dos puntos
p1 = Point(0, 0)  
p2 = Point(1, 1) 

# Calculamos y mostramos las distancias
print(p2.distance_from_xy(2, 0))   # Distancia entre p2 y (2, 0)

print(p1.distance_from_point(p2))  # Distancia entre p1 y p2

