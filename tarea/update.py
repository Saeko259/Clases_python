from datetime import date
def actualizar(
        diccionario:dict
    ) -> dict:
        """
        La siguiente funcion te permite  cambiar el usuario anterior y ingresar uno nuevo
            ---------params---------
            diccionario (dict) = el diccionario donde se estan almacenando los datos

            ---------return---------
            
            va a actualizar el valor de usuario
        """
        fecha = (f'{date.today()}')
        usuarionom = input('Como se llama ?: ')
        libro = input('Que libro quieres prestar ?: ')
        x = list(diccionario[usuarionom])
        vacio ={ }
        
        if usuarionom in diccionario:
            usuarionom = (f'{x.count(usuarionom) + 2}.{usuarionom} ')
            diccionario[usuarionom] = vacio
            vacio['libro'] = libro
            vacio['fecha'] = fecha
            vacio['estado'] = 'prestado'
        return 