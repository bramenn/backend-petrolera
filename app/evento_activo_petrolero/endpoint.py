from typing import List

from fastapi import APIRouter

from .consultas import (
    crear_evento_activo_petrolero_db,
    obtener_evento_activo_petrolero_id_db,
    obtener_todos_eventos_db,
)
from .modelo import EventoActivoPetroleroIn, EventoActivoPetroleroOut

router = APIRouter()


@router.get(
    "/",
    response_model=List[EventoActivoPetroleroOut],
    summary="Obtenga todos los eventos regitrados",
)
def obtener_todos_activos_petroleros():
    eventos = obtener_todos_eventos_db()
    return eventos


@router.get("/{id}", response_model=EventoActivoPetroleroOut)
def obtener_evento_activo_petrolero(id: str):
    evento_activo_petrolero = obtener_evento_activo_petrolero_id_db(id)
    return evento_activo_petrolero


@router.post("/", response_model=EventoActivoPetroleroOut)
def crear_evento_activo_petrolero(nuevo_evento_activo_petrolero: EventoActivoPetroleroIn):
    evento_activo_petrolero = crear_evento_activo_petrolero_db(nuevo_evento_activo_petrolero)
    return evento_activo_petrolero
