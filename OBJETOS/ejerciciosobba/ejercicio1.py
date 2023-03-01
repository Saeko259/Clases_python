class coche():
    def __init__(self,matricula,marca,kilometros,gasolina) -> None:
        self.matricula = matricula
        self.marca = marca
        self.kilometros = kilometros
        self.gasolina = gasolina
    def avanzar(self,km):
        if km > self.gasolina:
            x = -(self.gasolina - km)
            
            km2 = km - x
            self.kilometros = self.kilometros + km2
            self.gasolina = self.gasolina - km2
            print(f'te quedaste sin gasolina en el km {x}')
        else:
            self.gasolina = self.gasolina -km
            self.kilometros = self.kilometros + km
        
        
carrito = coche('QHY451','chevrolet',45,20)

carrito.avanzar(25)

print(carrito.gasolina)
print(carrito.kilometros)