def borra(  
    diccionario:dict
) -> dict:
 """
 La siguiente funcion te permite eliminar un usuario
 --------params--------
    diccionario (dict) = El diccionario donde se guardan los datos 
    usuario (str) = el nombre del usuario al que le prestamos el libro
 """
 usuario = str(input('Ingrese el nombre del usuario que quiera eliminar: ')) 
 x = input('Esta seguro que quiere eliminar su usuario ?, responda con un si o un no: ')
 x = x.lower
 if x == 'si':
     diccionario.pop(usuario)
 else:
     print('Listico, no se ha eliminado')
 return