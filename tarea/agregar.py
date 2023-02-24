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
  libro = (input('Ingrese el nombre del libro que quiera prestar: '))
  
  if diccionario.get(usuario_nombe) != None:
    diccionario[usuario_nombe].append({'libro':libro,'fecha':fecha,'estado':'prestado'})
  else:
    usuario = [{}]
    
    diccionario[usuario_nombe] = usuario
    chale = usuario[0]
    chale['libro'] = libro
    chale['fecha'] = fecha
    chale['estado'] = 'prestado'
  