from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from .modelo import Responsable, ResponsableIn, ResponsableOut


def obtener_todos_responsables_db() -> ResponsableOut:
    responsables = db.session.query(Responsable)

    if not responsables:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Responsables no encontrados",
        )

    return [parsear_responsable(responsable) for responsable in responsables]


def obtener_responsable_id_db(id: str) -> ResponsableOut:
    responsable = db.session.query(Responsable).where(Responsable.id == id).first()

    if not responsable:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Responsable no encontrado",
        )

    return parsear_responsable(responsable)


def crear_responsable_db(
    nuevo_responsable: ResponsableIn,
) -> ResponsableOut:
    responsable = Responsable(
        nombre_completo=nuevo_responsable.nombre_completo,
        correo_electronico=nuevo_responsable.correo_electronico,
        telefono=nuevo_responsable.telefono,
    )

    try:
        db.session.add(responsable)
        db.session.commit()
        return parsear_responsable(responsable)
    except Exception as e:
        print("No se ha creado el responsable: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado el responsable",
        )


def parsear_responsable(responsable: Responsable) -> ResponsableOut:
    return ResponsableOut(
        id=responsable.id,
        nombre_completo=responsable.nombre_completo,
        correo_electronico=responsable.correo_electronico,
        telefono=responsable.telefono,
        suscripciones=responsable.suscripciones,
    )
