from datetime import date 
class persona():
    def __init__(self,nombre,id):
        self.id = id
        self.nombre = nombre
        self.info ={
            "id":self.id,
            "nombre":self.nombre,
            "libros":[]
        }
    def __str__(self) -> str:
        return f'{self.id}:{self.nombre} = tiene {self.info} prestados'
    def agregar_libro(self,libro):
        fecha = date.today()
        libro_prestado = {
            'nombre':libro,
            'fecha':fecha,
            'estado':'prestado'
        }
        self.info['libros'].append(libro_prestado)   
    def visualizar_libros(self):
        print(self.info['libros'])
    def devolver_libro(self,libro):
        for i in self.info['libros']:
            if i['nombre'] == libro:
                
                i['estado'] = 'devuelto'
    def eliminar_libro(self,libro):  
        for i in self.info['libros']:
            if i == libro:
                self.info.pop(libro)
p1 = persona('sam','1146534002')
print(p1)
p1.agregar_libro('listico')
print(p1)
p1.eliminar_libro('listico')
print(p1)