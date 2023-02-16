def palabras():
    x = input('Ingrese la palabra o oracion que quiera separar: ')
    y = x.split (' ')
    diccionario = {}
    lista = []
    for i in y:
        j = list(i)
        z = len(j)
        lista.append(z)
        for w in lista:
            
            diccionario[i]= (f'Longitud: {w}')
    print(diccionario)

    lista.clear()

ciclo_repepetivo = True
while ciclo_repepetivo:
    x = int(input('''Quiere iniciar el proceso de deletreo o quiere finalizar el programa ?: 
                     1. Iniciar el proceso
                     2. Finalizar el programa
                     (x): '''))
    match x:
        case 1:
            palabras()
        case 2: 
            print('El programa se ha finalizado y no continuara ejecutandose')
            ciclo_repepetivo = False
        case _:
            print("Esta opcion no es válida")
            
    
        
        