def agregar(
    diccionario:dict
):
  """
    Funcion que permite al usuario ingresar sus datos
      ---------params---------
      diccionario (dict) = el diccionario donde se guardan los datos
      usuario (str) = nombre del usuario
      libro (str) = nombre del libro

      guarda en una variable el nombre del usuario
      -------return------
      agrega un usuario al diccionario
  """
  
  usuario = str(input("Ingrese su nombre: "))
  
  libro = str(input('Ingrese el nombre del libro que quiere prestar: '))
  
  diccionario[usuario] = libro
  return 
