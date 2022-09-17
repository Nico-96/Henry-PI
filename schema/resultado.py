from pydantic import BaseModel

class ResultadoBase(BaseModel):
    id_resultado:int
    puntos:str
    parrilla_salida:int
    numero:int
    laps:int
    tiempo:int
    duracion_milisegundo:str
    tiempo_lap_mas_rapido:str
    velocidad_lap_mas_rapido:str
    id_status:int
    puntos:float
    ranking:str
    posicion:int

    id_carrera:int
    id_piloto:int
    id_constructor:int

class ResultadoResponse (BaseModel):
    drivername:str
    points:int
    class config:
        orm_mode=True