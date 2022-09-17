from typing import List
from fastapi import APIRouter, Depends, status

from schema.circuito import CircuitoResponse
from sqlalchemy.orm import Session
from config.db import get_db
from model.circuito import Circuito
from model.carrera import Carrera
from sqlalchemy import func



router = APIRouter(prefix="/more-circuit.racing", tags=["Circuit Name"])

@router.get("/more-circuit-racing", status_code=status.HTTP_200_OK, response_model=List[CircuitoResponse])
def get(db:Session=Depends(get_db)):
    circuitrace = (
        db.query(Circuito)
        .join(Carrera, Circuito.id_circuito == Carrera.id_circuito)
        .group_by(Circuito.nombre)
        .order_by(func.count(Carrera.id_circuito).desc())
        .limit(1)
        .with_entities(
            Circuito.nombre.label("circuitname"),
            func.count(Carrera.id_circuito).label("count"))
        .all()
    )
    return circuitrace 
