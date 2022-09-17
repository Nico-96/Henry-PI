from typing import List
from fastapi import APIRouter, Depends, status

from schema.carrera import CarreraResponse
from sqlalchemy.orm import Session
from config.db import get_db
from model.carrera import Carrera
from sqlalchemy import func


router = APIRouter(prefix="/carrera", tags=["Año con más Carreras"])

@router.get("/year-more-race", status_code=status.HTTP_200_OK, response_model=List[CarreraResponse])

def get(db: Session = Depends(get_db)):
    first_query = (
        db.query(Carrera)
        .group_by(func.year(Carrera.fecha))
        .order_by(func.count(Carrera.id_carrera).desc())
        .limit(1)
        .with_entities(
            func.year(Carrera.fecha).label("anio"),
            func.count(Carrera.id_carrera).label("counter"))
        .all()
    )
    return first_query

