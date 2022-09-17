from config.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import DOUBLE

class Equipo(Base):
    __tablename__ = "equipo"

    
    id_constructor=Column(Integer, primary_key=True)
    nombre=Column(String, nullable=True)
    nacionalidad=Column(String, nullable=True)
   