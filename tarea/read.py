def leer_funcion(
    diccionario:dict
) -> dict: 
    """
    Funcion que lee el diccionario que se indique en los parametros
    
    diccionario(dict) = diccionario que queremos que lea
    """
    for i,j in diccionario.items():
        print (f'{i} => {j}')