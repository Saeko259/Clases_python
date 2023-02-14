
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
        usuario_viejo = str(input('Ingrese el nombre del usuario que quiere cambiar: '))
        usuario_nuevo = str(input('Ingrese el nombre del nuevo usuario: '))
        libro= str(input('Ingrese el nombre del libro que habian prestado: '))
        diccionario[usuario_nuevo] = libro
        diccionario.pop(usuario_viejo)
        return 