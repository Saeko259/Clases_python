from pydantic import BaseModel
from datetime import date

class PersonaBiblioteca(BaseModel):
    id:int
    nombre:str
    edad:int
    libro:str
    fecha:date
    clave:int
    
    
class PersonaBibliotecaSimple(BaseModel):
    id:int
    nombre:str
    edad:int    
    
    
class PersonaBibliotecaBasica(BaseModel):
    id:int
    