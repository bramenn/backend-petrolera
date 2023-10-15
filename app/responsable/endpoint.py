from typing import List

from fastapi import APIRouter

from .consultas import (
    crear_responsable_db,
    obtener_responsable_id_db,
    obtener_todos_responsables_db,
)
from .modelo import ResponsableIn, ResponsableOut

router = APIRouter()


@router.get(
    "/",
    response_model=List[ResponsableOut],
    summary="Obtenga todos los responsables",
)
def obtener_todos_activos_petroleros():
    activo_petrolero = obtener_todos_responsables_db()
    return activo_petrolero


@router.get("/{id}", response_model=ResponsableOut)
def obtener_responsable(id: str):
    responsable = obtener_responsable_id_db(id)
    return responsable


@router.post("/", response_model=ResponsableOut)
def crear_responsable(nuevo_responsable: ResponsableIn):
    responsable = crear_responsable_db(nuevo_responsable)
    return responsable
