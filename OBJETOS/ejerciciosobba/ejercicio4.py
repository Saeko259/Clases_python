class Cuenta():
    cuenta = 0
    def __init__(self) -> None:
        nombre = input('Cual es su nombre: ')
        self.cuenta = 0
        self.nombre = nombre
    def muestra(self):
        print(f'Sr.{self.nombre}, tiene ${self.cuenta} en su cuenta')
    def ingresar(self):
        x = float(input('Cuanto dinero quiere ingresar: '))
        while True:
            if x < 0:
                print('Ingrese una cantidad valida')
            if x > 0:
                self.cuenta = self.cuenta + x
                break
    def retirar(self):
        y = float(input('Cuanto dinero quiere retirar? '))
        self.cuenta = self.cuenta - y
        
lol = Cuenta()
while True:
    lol.ingresar()
    lol.retirar()
    lol.muestra()
                
        
        
