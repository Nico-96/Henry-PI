from pydantic import BaseModel

class CircuitoBase(BaseModel):

    id_circuito:int
    nombre:str
    Ciudad:str
    Pais:str
    latitud:float
    longitud:float
    altitud:int

class CircuitoResponse(BaseModel):
    circuitname:str
    count:int

    class config:
        orm_mode=True

