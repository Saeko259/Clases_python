class Robot():
    x = 0
    y = 0
    def __init__(self,nombre) -> None:
        self.nombre = nombre

        
    def arriba(self):
        l = int(input('Cuantos puntos quiere subir, en numero entero: '))
        self.y = self.y + l
        
    def abajo(self):
        l = int(input('Cuantos puntos quiere bajar, en numero entero: '))
        self.y = self.y - l
        
    def derecha(self):
        l = int(input('Cuantos puntos quiere ir a la derecha, en numero entero: '))
        self.x = self.x + l
        
    def izquierda(self):
        l = int(input('Cuantos puntos quiere ir a la izquierda, en numero entero: '))
        self.x = self.x - l
        
    def posicion(self) -> str:
        print(f'Estas en la cordenada({self.x},{self.y})')
        
cola = Robot('eladio carreon')
cola.arriba()
cola.abajo()
cola.derecha()
cola.izquierda()
cola.posicion()