from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from ..activo_petrolero.consultas import obtener_activo_petrolero_id_db
from ..aws_client import suscribir_responsable
from ..responsable.consultas import obtener_responsable_id_db
from .modelo import Suscripcion, SuscripcionIn, SuscripcionOut


def obtener_suscripcion_id_db(id: str) -> SuscripcionOut:
    suscripcion = db.session.query(Suscripcion).where(Suscripcion.id == id).first()

    if not suscripcion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Suscripcion no encontrada",
        )

    return parsear_suscripcion(suscripcion)


def obtener_suscripciones_id_responsable_db(id_responsable: str) -> SuscripcionOut:

    suscripciones = db.session.query(Suscripcion).where(
        Suscripcion.id_responsable == id_responsable
    )

    if not suscripciones:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Suscripcion no encontrada",
        )

    return [parsear_suscripcion(suscripcion) for suscripcion in suscripciones]


def crear_suscripcion_db(
    nueva_suscripcion: SuscripcionIn,
) -> SuscripcionOut:
    suscripcion = Suscripcion(
        id_responsable=nueva_suscripcion.id_responsable,
        id_activo_petrolero=nueva_suscripcion.id_activo_petrolero,
    )

    responsable = obtener_responsable_id_db(nueva_suscripcion.id_responsable)
    activo_petrolero = obtener_activo_petrolero_id_db(nueva_suscripcion.id_activo_petrolero)

    try:
        db.session.add(suscripcion)
        db.session.commit()

        suscribir_responsable(
            arn_sns=activo_petrolero.tema_sns,
            protocolo="email",
            endpoint=responsable.correo_electronico,
        )
        suscribir_responsable(
            arn_sns=activo_petrolero.tema_sns,
            protocolo="sms",
            endpoint=responsable.telefono,
        )

        return parsear_suscripcion(suscripcion)
    except Exception as e:
        print("No se ha crear la suscripcion: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado la suscripcion",
        )


def parsear_suscripcion(suscripcion: Suscripcion) -> SuscripcionOut:
    return SuscripcionOut(
        id=suscripcion.id,
        id_responsable=suscripcion.id_responsable,
        id_activo_petrolero=suscripcion.id_activo_petrolero,
    )
