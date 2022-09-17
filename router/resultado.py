from typing import List
from fastapi import APIRouter, Depends, status

from schema.resultado import ResultadoResponse
from sqlalchemy.orm import Session
from config.db import get_db
from model.pilotos import Pilotos
from model.resultado import Resultado
from sqlalchemy import func , or_
from model.equipo import Equipo



router = APIRouter(prefix="/driver-most-score", tags=["Piloto con mejor puntaje"])

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ResultadoResponse])
def get(db:Session=Depends(get_db)):
    results = (
        db.query(Resultado)
        .join(Pilotos, Resultado.id_piloto==Pilotos.id_piloto)
        .join(Equipo, Resultado.id_constructor == Equipo.id_constructor)
        .filter(or_(Equipo.nacionalidad == "British", Equipo.nacionalidad=="American"))
        .group_by(func.concat(Pilotos.nombre, ' ', Pilotos.apellido))
        .order_by(func.sum(Resultado.puntos).desc())
        .limit(1)
        .with_entities(
            func.concat(Pilotos.nombre, ' ',Pilotos.apellido).label("drivername"),
            func.sum(Resultado.puntos).label("points"))
        .all()
    )
    return results
