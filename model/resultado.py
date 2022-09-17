from config.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import DOUBLE

class Resultado(Base):
    __tablename__ = "resultado"

    
    id_resultado=Column(Integer, primary_key=True)
    puntos=Column(String, nullable=True)
    parrilla_salida=Column(Integer, nullable=True)
    numero=Column(String, nullable=True)
    laps=Column(Integer, nullable=True)
    tiempo=Column(String, nullable=True)
    duracion_milisegundo=Column(String, nullable=True)
    tiempo_lap_mas_rapido=Column(String, nullable=True)
    velocidad_lap_mas_rapido=Column(String, nullable=True)
    id_status=Column(Integer, nullable=True)
    puntos=Column(DOUBLE, nullable=True)
    ranking=Column(String, nullable=True)
    posicion=Column(Integer, nullable=True)

    id_carrera=Column(Integer, ForeignKey("carrera.id_carrera"))
    id_piloto=Column(Integer, ForeignKey("pilotos.id_piloto"))
    id_constructor=Column(Integer, ForeignKey("equipo.id_constructor"))

    