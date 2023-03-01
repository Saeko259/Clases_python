class Triangulos():
    def __init__(self) -> None:
        self.lado1 = float(input('Ingrese la medida del primer lado: '))
        self.lado2 = float(input('Ingrese la medida del segundo lado: '))
        self.lado3 = float(input('Ingrese la medida del tercer lado: '))
        self.lados = [self.lado1,self.lado2,self.lado3]
        
    def lado_mayor(self):
        mayor = max(self.lados)
        print(f'El lado mayorxx es {mayor}')
    def tipo_triangulo(self): 
        conjunto_lados = set(self.lados)
        if len(conjunto_lados) == 3:
            print(f'El triangulo es escaleno')
        elif len(conjunto_lados) == 2:
            print(f'El triangulo es isoceles')
        else:
            print('El triangulo es equilatero')
            
lol = Triangulos()
lol.tipo_triangulo()
            
        

    