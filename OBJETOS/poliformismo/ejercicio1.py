class SerVivo():
    sentidos_lista= ['olfato','vista','tacto','gusto','oido']
    
    def __init__(self) -> None:
        nombre = input('cual es tu nombre: ')
        self.nombre = nombre
    
    def sentidos(self):
        print(self.sentidos_lista)
        
    def movimiento(self):
        print(f'{self.nombre} se esta moviendo')
        
    def sonido(self):
        print(f'{self.nombre} esta haciendo un sonido')
        
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
        
lol = Persona()
lol.movimiento()
lol.sonido()
pp = Gato()
pp.movimiento()
pp.sonido()
oo = Perro()
oo.movimiento()
oo.sonido()