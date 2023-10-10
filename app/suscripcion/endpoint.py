from fastapi import APIRouter

from .consultas import crear_suscripcion_db, obtener_suscripcion_id_db
from .modelo import SuscripcionIn, SuscripcionOut

router = APIRouter()


@router.get("/{id}", response_model=SuscripcionOut)
def obtener_suscripcion(id: str):
    suscripcion = obtener_suscripcion_id_db(id)
    return suscripcion


@router.post("/", response_model=SuscripcionOut)
def crear_suscripcion(nuevo_suscripcion: SuscripcionIn):
    suscripcion = crear_suscripcion_db(nuevo_suscripcion)
    return suscripcion
