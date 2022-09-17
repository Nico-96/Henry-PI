import imp
from pydantic import BaseModel
from datetime import datetime 

class CarreraBase(BaseModel):
    
    id_carrera:int
    nombre:str
    round:int
    id_circuito:int
    fecha:datetime
    tiempo:str

class CarreraResponse(BaseModel):
    anio: int
    counter: int
    class Config:
        orm_mode =True 