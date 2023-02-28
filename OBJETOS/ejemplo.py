#Podemos hacer organizaciones de datos dependientes o independientes, usando el self, por ejemplo, si creamos un diccionario con .self, sera guardado como una base de datos para el objeto en especifico, pero si la establecemos como un diccionario general, sera usado como base de datos de todos los objetos y se guardaran ahi los datos

class Personas ():
    libros = {}
    def __init__(self,nom) -> None:
        self.nom = nom
        
    def agregar(self,nom_libro,fecha):
        self.libros.update({nom_libro:fecha})
        
p1 = Personas('lola')
p2 = Personas('gab')

p1.agregar('python','lol')
print(p1.libros)