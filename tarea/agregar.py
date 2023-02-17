from datetime import date

def agregar(
    diccionario:dict
) ->dict:
  """
    Funcion que permite al usuario ingresar sus datos
      ---------params---------
      diccionario (dict) = el diccionario donde se guardan los datos
      -------return------
      agrega un usuario al diccionario
  """
  
  fecha = (f'{date.today()}')
  
  usuario_nombe = input("Ingrese su nombre: ")
  usuario_nombe = ('1.'+usuario_nombe)
  usuario = { }
  libro = (input('Ingrese el nombre del libro que quiera prestar: '))
  diccionario[usuario_nombe] = usuario
  usuario['libro'] = libro
  usuario['fecha'] = fecha
  usuario['estado'] = 'prestado'

  return 