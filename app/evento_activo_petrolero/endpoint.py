from fastapi import APIRouter

from .consultas import crear_evento_activo_petrolero_db, obtener_evento_activo_petrolero_id_db
from .modelo import EventoActivoPetroleroIn, EventoActivoPetroleroOut

router = APIRouter()


@router.get("/{id}", response_model=EventoActivoPetroleroOut)
def obtener_evento_activo_petrolero(id: str):
    evento_activo_petrolero = obtener_evento_activo_petrolero_id_db(id)
    return evento_activo_petrolero


@router.post("/", response_model=EventoActivoPetroleroOut)
def crear_activo_petrolero(nuevo_evento_activo_petrolero: EventoActivoPetroleroIn):
    evento_activo_petrolero = crear_evento_activo_petrolero_db(nuevo_evento_activo_petrolero)
    return evento_activo_petrolero
