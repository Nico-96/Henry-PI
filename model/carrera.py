from config.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey,Date

class Carrera(Base):
    __tablename__="carrera"

    id_carrera=Column(Integer, primary_key=True)
    nombre=Column(String, nullable=True)
    round=Column(Integer, nullable=True)
    id_circuito=Column(Integer, ForeignKey("circuito.id_circuito"))
    fecha=Column(Date, nullable=True)
    tiempo=Column(String, nullable=True)
    