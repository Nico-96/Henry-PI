from config.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import DOUBLE

class Circuito(Base):
    __tablename__ = "circuito"

    
    id_circuito=Column(Integer, primary_key=True)
    nombre=Column(String, nullable=True)
    Ciudad=Column(String, nullable=True)
    Pais=Column(String, nullable=True)
    latitud=Column(DOUBLE, nullable=True)
    longitud=Column(DOUBLE, nullable=True)
    altitud=Column(Integer, nullable=True)