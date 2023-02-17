epa = True

if __name__ == "__main__":
    from agregar import *
    from borrar import *
    from read import *
    from update import actualizar
    from estado import devolver

    libros ={ }
    

    while epa == True:
        print ("-"*50)
        print( )
        x = int(input( """Escoge lo que quieras que suceda:
                1.Agregar a un usuario
                2.Actualizar a un usuario
                3.Eliminar un usuario
                4.Leer la lista de personas que han prestado libros
                5.Devolver un libro
                6.No hacer nada
                (x): """))
        match x:
            case 1: 
                agregar(libros)
            case 2:
                actualizar(libros)
            case 3:
                borra(libros) 
            case 4:
                leer_funcion(libros)
            case 5:
                devolver(libros)
            case 6:
                print('\nYa finalizo el proceso, chauuu')
                epa == False
                break
                