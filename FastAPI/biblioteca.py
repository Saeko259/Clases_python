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


@app.get('/')
def hello_wold_check():
    {
        'titulo':'Biblioteca',
        'version':'V.1.0.3'
    }
    return 'hello world'

    
@app.get('/personas/{id}')
def id(id:int):
    return biblioteca[id]


@app.get('/personas')
def all_people():
    return biblioteca


class PersonaBiblioteca(BaseModel):
    id:int
    nombre:str
    edad:int
    libro:str
    fecha:int
    clave:int
    
@app.post('/personas')
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