#objeto es una identidad que tiene caracteristicas inerentes, le podemos agregar funciones o variables pre construidas a traves de las clases
#Podemos crear metodos para las clases que creamos
# Los objetos tendran diferentes propiedades segun su tipo, es decir, dependiendo del tipo que creemos,  tendra diferentes propiedaes
#Podemos usar __init__, para inicializar un objeto, usamos self como parametro, para referirnos al objeto en si, esto se puede usar en funciones.
#Para usar caracteristicas o funciones de una clase, usamos un '.', donde seria, nombreobjeto.funcion, como se ve en el codigo de abajo.
#Init es un metodo magico.
#__str__ es otro m.etodo magico, sirve para crear funciones que indique que pasara cuando se imprima un objeto de ese tipo
#Las funciones dentro de una clase, solo funcionan para objetos de aquella clase, no pueden ser llamadas de otra forma, es decir, la cuestion se ve tal que asi, objeto.funcion(parametros)
# Init, es para darle los atributos al objeto, por lo tanto, todo lo que esta en self puede ser usado en el resto del codigo,
class Personas():
    sentidos = ["bista", "lolfato",'takto','gusto','hoido']
    
    def __init__(self,nombre,edad,apellido) -> None:
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
    def __str__(self) -> str:
        return f'{self.nombre} tiene {self.edad} años'    
    def area_rectangulo(self, 
                altura:float,
                base:float,
                nombre:str
                 ) -> str:
                area = base * altura
                prl = f'{nombre} es un rectangulo de area {area}'
                print(prl)
    def saludo(self):
        print(f'hola {self.nombre} {self.apellido}, HOLA COMO ESTAS')    
    pass
    #En la funcion anterior, se usa self.nombre por que estas accediendo a una variable de otra funcion, que es init.

felipe = Personas('felipe','12')
print(felipe.edad)