lista1 = []
lista2 = []

def agregar(
    lista:list
)-> list:
    """
    Una funcion para agregar nombres a una lista
    
    ----------parameters--------
    
    lista(list) = Lista donde se guardan los nombres que insertemos
    
    -------output-------
    
    Listas con los nombres que ingresamos
    """
    numero = int(input('Ingrese cuantos nombres quiere agregar: '))
    for i in range(numero):
        y = input(f'Ingrese el {i+1} nombre que quiere agregar: ')
        lista.append(y)
    print(lista)
def eliminar(
    listaA:list,
    listaB:list
) -> list:
    """
    Una funcion para eliminar nombres de la lista
    
    -------parameters-------
    
    ListaA (list) = Lista donde se almacenan los nombres
    
    ListaB (list) = Lista donde se almacenan los nombres de los usuarios que queremos eliminar
    
    -----output------
    
    La listaA sin los usuarios que escogimos para eliminar
    """ 
    numero = int(input('Digite cuantos usuarios quiere eliminar: '))
    for i in range(numero): 
        x = input(f'Escribe el nombre del usuario {i+1} que quieras eliminar: ')
        listaB.append(x)
    for i in listaB:
        if i in listaA:
            listaA.remove(i)
    print(listaA)
    listaB.clear()
   
while True:    
    agregar(lista1)   
    eliminar(lista1,lista2)
    
    print('-' *50)

