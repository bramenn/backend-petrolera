from typing import List

from fastapi import APIRouter

from .consultas import (
    crear_suscripcion_db,
    obtener_suscripcion_id_db,
    obtener_suscripciones_id_responsable_db,
)
from .modelo import SuscripcionIn, SuscripcionOut

router = APIRouter()


@router.get("/{id}", response_model=SuscripcionOut)
def obtener_suscripcion(id: str):
    suscripcion = obtener_suscripcion_id_db(id)
    return suscripcion


@router.get(
    "/responsable/{id}",
    response_model=List[SuscripcionOut],
    summary="Obtengta todas las suscripciones de un responsable dado su id",
)
def obtener_suscripciones_por_responsable(id: str):
    suscripciones = obtener_suscripciones_id_responsable_db(id)
    return suscripciones


@router.post("/", response_model=SuscripcionOut)
def crear_suscripcion(nuevo_suscripcion: SuscripcionIn):
    suscripcion = crear_suscripcion_db(nuevo_suscripcion)
    return suscripcion
