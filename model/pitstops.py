from config.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Pitstops(Base):
    __tablename__ = "pitstops"

    
    id_carrera=Column(Integer, ForeignKey("carrera.id_carrera"))
    id_piloto=Column(Integer, ForeignKey("pilotos.id_piloto"))
    stop=Column(Integer, nullable=True)
    lap=Column(Integer, nullable=True)
    tiempo=Column(String, nullable=True)
    duracion_segundos=Column(String, nullable=True)
    duracion_milisegundos=Column(Integer, nullable=True)
    