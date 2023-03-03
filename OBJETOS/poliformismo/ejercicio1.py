class SerVivo():
    sentidos_lista= ['olfato','vista','tacto','gusto','oido']
    x = 0
    y = 0    
    def __init__(self) -> None:
        nombre = input('cual es tu nombre: ')
        self.nombre = nombre
        self.x = 0
        self.y = 0
    
    def sentidos(self):
        print(self.sentidos_lista)
        
    def movimiento(self):
        print(f'{self.nombre} se esta moviendo')
    def sonido(self):
        print(f'{self.nombre} esta haciendo un sonido')
    def arribajo(self):
        l = int(input('Cuantos pasos quiere moverse adelante(+) o atras(-), en numero entero: '))
        self.y = self.y + l
    def izqder(self):
        l = int(input('Cuantos pasos quiere ir a la derecha(+) o a la izquierda(-), en numero entero: '))
        self.x = self.x + l
    def posicion(self) -> str:
        if self.x < 0 and self.y<0:
            print(f'Has dado {-self.x} pasos hacia la izquierda , {-self.y} pasos hacia atras{-self.y})') 
        elif self.x < 0 and self.y >0:
            print(f'Has dado {-self.x} pasos hacia la izquierda, {self.y} pasos hacia adelante')
        elif self.x > 0 and self.y <0:
            print(f'Has dado {self.x} pasos hacia la derecha, {-self.y} pasos hacia atras')
        elif self.x > 0 and self.y >0:
            print(f'Has dado {self.x} pasos hacia la derecha, {self.y} pasos hacia adelante')
class Persona(SerVivo):
    def movimiento(self):
        print(f'{self.nombre} esta caminando')
    def sonido(self):
        print(f'{self.nombre} esta hablando')
    
class Gato(SerVivo):
    def movimiento(self):
        print(f'{self.nombre} esta gateando')
    def sonido(self):
        print(f'{self.nombre} esta maullando')

class Perro(SerVivo):
    def movimiento(self):
        print(f'{self.nombre} esta andando')
    def sonido(self):
        print(f'{self.nombre} esta ladrando')
        
pp = Gato()
pp.izqder()
pp.arribajo()
pp.posicion()