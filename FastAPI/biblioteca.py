from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

biblioteca ={ 1:{
        'nombre':'felipe',
        'edad':'23',
        'libros':{
            1:{'libro':'club 5 am',
            'fecha':'13/03/2023',
            'estado':'prestado'},
            
            2:{'libro':'apopeya',
                 'fecha':'13/03/2023',
                 'Estado':'prestado'}
        }
    }
}   


@app.get('/',tags=['Lectura de datos'])
def hello_wold_check():
    {
        'titulo':'Biblioteca',
        'version':'V.1.0.3'
    }
    return 'hello world'

    
@app.get('/personas/{id}',tags=['Lectura de datos'])
def id(id:int):
    return biblioteca[id]


@app.get('/personas',tags=['Lectura de datos'])
def all_people():
    return biblioteca


class PersonaBiblioteca(BaseModel):
    id:int
    nombre:str
    edad:int
    libro:str
    fecha:int
    clave:int
    
@app.post('/personas',tags=['Agregar datos'])
def Personas_add(request:PersonaBiblioteca):
     x = {'nombre':request.nombre,
         'edad':request.edad,
         'libros':{
             request.clave:
                {  
                'libro':request.libro,
                'fecha':request.fecha,
                'estado':'prestado'
                }
            }
        }
     biblioteca[request.id] = x 
     return 'Ya se han agregado tus datos :D'
 
 
class PersonaLoca(BaseModel):
    id:int
    nombre:str
    edad:int 
    
@app.put('/personas',tags=['Modificar datos'])
def personas_mod(request:PersonaLoca):
    
    if biblioteca[request.id]['nombre'] != request.nombre:
            biblioteca[request.id]['nombre'] = request.nombre
    elif biblioteca[request.id]['edad'] != request.edad:
            biblioteca[request.id]['edad'] = request.edad


class Juandi(BaseModel):
    id:int
   
@app.delete('/personas',tags=['Eliminar datos'])
def personas_del(request:Juandi):
    biblioteca.pop(request.id)     
