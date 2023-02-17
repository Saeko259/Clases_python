def leer_funcion(
    diccionario:dict
) -> dict: 
    """
    Funcion que lee el diccionario que se indique en los parametros
    
    diccionario(dict) = diccionario que queremos que lea
    """
    
    for i in diccionario.keys():
        j = diccionario[i]
        print(i, '=>',j)
        print( )