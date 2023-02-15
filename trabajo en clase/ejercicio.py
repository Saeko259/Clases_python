lista1 = []
lista2 = []

def agregar(
    lista:list
):
    numero = int(input('Ingrese cuantos nombres quiere agregar: '))
    for i in range(numero):
        y = input(f'Ingrese el {i+1} nombre que quiere agregar: ')
        lista.append(y)
    print(lista)
def eliminar(
    listaa:list,
    listaaa:list
): 
    numero = int(input('Digite cuantos usuarios quiere eliminar: '))
    for i in range(numero): 
        x = input(f'Escribe el nombre del usuario {i+1} que quieras eliminar: ')
        listaaa.append(x)
    for i in listaaa:
        if i in listaa:
            listaa.remove(i)
    print(listaa)
    listaaa.clear()
   
while True:    
    agregar(lista1)   
    eliminar(lista1,lista2)
 

