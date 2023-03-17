from pydantic import BaseModel

class PersonaBiblioteca(BaseModel):
    id:int
    nombre:str
    edad:int
    libro:str
    fecha:int
    clave:int
    
    
class PersonaBibliotecaSimple(BaseModel):
    id:int
    nombre:str
    edad:int    
    
    
class PersonaBibliotecaBasica(BaseModel):
    id:int
    