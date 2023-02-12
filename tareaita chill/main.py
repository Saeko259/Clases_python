if __name__ == "__main__":
    from agregar import *
    from borrar import *
    from read import *
    from update import actualizar

    libros ={ 'felipe':'habitos atomicos'}
    epa = True
    y = 2 #para poder darle uso a la variable luego, el numero dos no tiene ninguna importancia, solo estamos creando una variable
    n = 2
    while epa == True:
        print ("-"*50)
        print( )
        x = int(input( """Escoge lo que quieras que suceda:
                1.Agregar a un usuario
                2.Actualizar a un usuario
                3.Eliminar un usuario
                4.Leer la lista de personas que han prestado libros
                5.No hacer nada
                (x): """))
        match x:
            case 1:
                
                agregar(libros,x,y)
            case 2:
                actualizar(libros,x,y,n)
            case 3:
                borra(libros,x,y) 
            case 4:
                leer_funcion(libros)
            case 5:
                print('\nYa finalizo el proceso, chauuu')
                epa == False
                