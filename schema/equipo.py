from pydantic import BaseModel

class EquipoBase(BaseModel):

    id_constructor:str
    nombre:str
    nacionalidad:str