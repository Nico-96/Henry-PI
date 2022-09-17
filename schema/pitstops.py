from pydantic import BaseModel

class PitstopsBase(BaseModel):
    id_carrera:int
    id_piloto:int
    stop:int
    lap:int
    tiempo:int
    duracion_segundos:str
    duracion_milisegundos:int
    