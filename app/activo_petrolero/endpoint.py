from fastapi import APIRouter

from .consultas import crear_activo_petrolero_db, obtener_activo_petrolero_id_db
from .modelo import ActivoPetroleroIn, ActivoPetroleroOut

router = APIRouter()


@router.get(
    "/{id}",
    response_model=ActivoPetroleroOut,
    summary="Obtenga la infromación de un activo petrolero",
)
def obtener_activo_petrolero(id: str):
    activo_petrolero = obtener_activo_petrolero_id_db(id)
    return activo_petrolero


@router.post("/", response_model=ActivoPetroleroOut, summary="Cree un nuevo activo petrolero")
def crear_activo_petrolero(nuevo_activo_petrolero: ActivoPetroleroIn):
    activo_petrolero = crear_activo_petrolero_db(nuevo_activo_petrolero)
    return activo_petrolero
