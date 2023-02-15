def palabras():
    x = input('Ingrese la palabra o oracion que quiera separar: ')
    y = x.split (' ')
    diccionario = {}
    lista = []
    for i in y:
        print(i)
        j = list(i)
        z = len(j)
        lista.append(z)
        for w in lista:
            diccionario[i]= (f'Longitud: {w}')
    print(diccionario)
    lista.clear()


while True:
    palabras()
        
        