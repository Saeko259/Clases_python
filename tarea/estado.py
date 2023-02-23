def devolver(
    diccionario:dict
):
    nom = input('Como te llamas?: ')
    x = input('Haz prestado mas de un libro ?, responde con un si o un no: ')
    x = x.lower()
    if x == 'si':
        z = int(input('Cuantos libros son ? '))
        y = int(input(f'Cual de los {z} libros que has prestado quieres devolver ?, da una respuesta del 1 al {z}: '))
        est = diccionario[nom]
        est1 = est[y-1]
        est1['estado'] = 'devuelto'
    elif x == 'no':
        est = diccionario[nom]
        est1 = est[0]
        est1['estado'] = 'devuelto'
    else:
        print('la respuesta que has dado no es valida, por lo tanto, el proceso no se ha llevado a cabo.')
