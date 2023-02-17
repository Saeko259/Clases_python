def devolver(
    diccionario:dict
):
    usuarionom = input('Como se llama el libro ?: ')
    
    usuario =diccionario[usuarionom]
    usuario['estado'] = 'devuelto'