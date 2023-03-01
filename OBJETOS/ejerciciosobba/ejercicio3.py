class Alumno():
    x = 3.0
    
    def __init__(self):
        nombre = input('Como te llamas: ')
        nota = float(input('Que nota sacaste: '))
        self.nombre = nombre
        self.nota = nota
        self.x = 3.0
        
    def aprobaste(self):
        
        if self.nota > self.x:
            print(f'Excelente {self.nombre} aprobaste el examen')
        if self.nota < self.x:
            print(f'Disculpa {self.nombre}, no aprobaste el examen')
            
isaac = Alumno()

isaac.aprobaste()