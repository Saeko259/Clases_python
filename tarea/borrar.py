def borra(
    
    diccionario:dict,
    usuario:str   
) :
 """
 La siguiente funcion te permite eliminar un usuario
 --------params--------
    diccionario (dict) = El diccionario donde se guardan los datos 
    usuario (str) = el nombre del usuario al que le prestamos el libro
 """
 usuario = str(input('Ingrese el nombre del usuario que quiera eliminar: ')) 
 
 diccionario.pop(usuario)
 return