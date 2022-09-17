from config.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.dialects.mysql import DOUBLE

class Pilotos(Base):
    __tablename__ = "pilotos"

    
    id_piloto=Column(Integer, primary_key=True)
    nombre=Column(String, nullable=True)
    numero=Column(String, nullable=True)
    apellido=Column(String, nullable=True)
    fecha_nacimiento=Column(Date, nullable=True)
    nacionalidad=Column(String, nullable=True)
    