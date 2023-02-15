lista_estudiantes = ['David','Omar','Isaac']
lista_profesores = ['Felipe']

def agregar(
    lista:list
) -> list:
    estudiante = input('Ingrese estudiante: ')
    lista.append(estudiante)
    print(lista)
    
def agregar_profesores(
    lista:list
) -> list:
    profesor = input('Ingrese estudiante: ')
    lista.append(profesor)
    print(lista)
    
def eliminar_estudiante(
    lista:list
) -> list:
    estudiante = str(input('Ingrese el nombre del estudiante: '))
    lista.remove(estudiante)
    
def eliminar_profesor(
    lista:list
) -> list:
    profesor = str(input('Ingrese el nombre del estudiante: '))
    lista.remove(profesor)
    
def leer(
    lista:list
):
    for i in lista:
        print(i, end= ' - ')
        
def juntar(
    lista1:list,
    lista2:list,
    elemento = ['HOLA']
) -> list:
    lista3 = lista1 + lista2
    lista3 = lista3 + elemento
    print(lista3)
    
        
while True:
    x= int(input("""Ingrese lo que quiere hacer:
          
          1.Agregar un nombre a la lista
          2.Eliminar un nombre de la lista
          3.Leer la lista
          4.Juntar  las dos listas
          (x): """))
    match x:
        case 1:
            y = int(input("""Con cual de estos dos quiere trabajar:
                          1. Profesor
                          2. Estudiante
                          (x): """))
            if y == 1:
                agregar_profesores(lista_profesores)
            if y == 2:
                agregar(lista_estudiantes)
            else:
                print("Esta opcion no es posible")
        case 2:
            y = int(input("""
                          1. Profesor
                          2. Estudiante
                          """))
            if y == 1:
                eliminar_profesor(lista_profesores)
            if y == 2:
                eliminar_estudiante(lista_estudiantes)
            else:
                print("Esta opcion no es posible")
        case 3:
            y = int(input("""
                          1. Profesor
                          2. Estudiante
                          """))
            if y == 1:
                leer(lista_profesores)
            if y == 2:
                leer(lista_estudiantes)
            else:
                print("Esta opcion no es posible")
        case 4:
            juntar(lista_estudiantes,lista_profesores)
        case _:
            print('Esta opcion no es posible')
 