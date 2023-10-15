from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from ..aws_client import crear_tema_sns
from .modelo import ActivoPetrolero, ActivoPetroleroIn, ActivoPetroleroOut


def obtener_activo_petrolero_id_db(id: str) -> ActivoPetroleroOut:
    activo_petrolero = db.session.query(ActivoPetrolero).where(ActivoPetrolero.id == id).first()

    if not activo_petrolero:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Activo petrolero no encontrado",
        )

    return parsear_activo_petrolero(activo_petrolero)


def crear_activo_petrolero_db(
    nueva_activo_petrolero: ActivoPetroleroIn,
) -> ActivoPetroleroOut:
    # TODO Crear tema sns

    activo_petrolero = ActivoPetrolero(
        longitud=nueva_activo_petrolero.longitud,
        latitud=nueva_activo_petrolero.latitud,
        tema_sns="",
    )

    try:
        db.session.add(activo_petrolero)
        db.session.commit()
        tema_sns = crear_tema_sns(activo_petrolero.id)
        activo_petrolero.tema_sns = tema_sns
        db.session.commit()
        return parsear_activo_petrolero(activo_petrolero)
    except Exception as e:
        print("No se ha crear el activo petrolero: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado el activo petrolero",
        )


def parsear_activo_petrolero(activo_petrolero: ActivoPetrolero) -> ActivoPetroleroOut:
    return ActivoPetroleroOut(
        id=activo_petrolero.id,
        longitud=activo_petrolero.longitud,
        latitud=activo_petrolero.latitud,
        tema_sns=activo_petrolero.tema_sns,
        suscripciones=activo_petrolero.suscripciones,
    )
