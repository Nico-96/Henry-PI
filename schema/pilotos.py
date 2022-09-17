from pydantic import BaseModel
from datetime import datetime 

class PilotosBase(BaseModel):
    id_piloto:str
    nombre:str
    numero:str
    apellido:str
    fecha_nacimiento:datetime
    nacionalidad:str

class PilotosResponse(BaseModel):
    name_driver: str
    firstplace: int

    class Config:
        orm_mode = True
        

