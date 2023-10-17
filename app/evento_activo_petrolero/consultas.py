from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from ..activo_petrolero.consultas import obtener_activo_petrolero_id_db
from ..aws_client import enviar_evento_petrolero
from .modelo import EventoActivoPetrolero, EventoActivoPetroleroIn, EventoActivoPetroleroOut


def obtener_todos_eventos_db() -> EventoActivoPetroleroOut:
    eventos = db.session.query(EventoActivoPetrolero)

    if not eventos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Eventos no encontrados",
        )

    return [parsear_evento_activo_petrolero(evento) for evento in eventos]


def obtener_evento_activo_petrolero_id_db(id: str) -> EventoActivoPetroleroOut:
    evento_activo_petrolero = (
        db.session.query(EventoActivoPetrolero).where(EventoActivoPetrolero.id == id).first()
    )

    if not evento_activo_petrolero:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evento activo petrolero no encontrado",
        )

    return parsear_evento_activo_petrolero(evento_activo_petrolero)


def crear_evento_activo_petrolero_db(
    nuevo_evento_activo_petrolero: EventoActivoPetroleroIn,
) -> EventoActivoPetroleroOut:
    activo_petrolero = obtener_activo_petrolero_id_db(
        nuevo_evento_activo_petrolero.id_activo_petrolero,
    )

    evento_activo_petrolero = EventoActivoPetrolero(
        mensaje=nuevo_evento_activo_petrolero.mensaje,
        id_activo_petrolero=nuevo_evento_activo_petrolero.id_activo_petrolero,
    )

    try:
        db.session.add(evento_activo_petrolero)
        db.session.commit()
        enviar_evento_petrolero(
            data=evento_activo_petrolero.mensaje,
            tema_sns=activo_petrolero.tema_sns,
        )
        return parsear_evento_activo_petrolero(evento_activo_petrolero)
    except Exception as e:
        print("No se ha crear el evento activo petrolero: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado el evento activo petrolero",
        )


def parsear_evento_activo_petrolero(
    evento_activo_petrolero: EventoActivoPetrolero,
) -> EventoActivoPetroleroOut:
    return EventoActivoPetroleroOut(
        id=evento_activo_petrolero.id,
        mensaje=evento_activo_petrolero.mensaje,
        id_activo_petrolero=evento_activo_petrolero.id_activo_petrolero,
    )
