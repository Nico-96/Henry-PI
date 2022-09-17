from typing import List
from fastapi import APIRouter, Depends, status

from schema.pilotos import PilotosResponse
from sqlalchemy.orm import Session
from config.db import get_db
from model.pilotos import Pilotos
from model.resultado import Resultado
from sqlalchemy import func



router = APIRouter(prefix="/first-place", tags=["Driver Winner"])

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[PilotosResponse])
def get(db:Session=Depends(get_db)):
    pilot = (
        db.query(Pilotos)
        .join(Resultado, Resultado.id_piloto == Pilotos.id_piloto)
        .filter(Resultado.posicion == 1)
        .group_by(func.concat(Pilotos.nombre, ' ', Pilotos.apellido))
        .order_by(func.count(Resultado.posicion).desc())
        .limit(1)
        .with_entities(
            func.concat(Pilotos.nombre, ' ',Pilotos.apellido).label("name_driver"),
            func.count(Resultado.posicion).label("firstplace"))
        .all()
    )
    return pilot
