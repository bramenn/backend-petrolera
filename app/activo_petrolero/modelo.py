from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .. import db
from ..suscripcion.modelo import Suscripcion


class ActivoPetrolero(db.Base):
    __tablename__ = "activo_petrolero"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    longitud = Column(
        "longitud",
        String(255),
    )
    latitud = Column(
        "latitud",
        String(255),
    )
    tema_sns = Column("tema_sns", String(255), unique=True)
    suscripciones = relationship(Suscripcion)


class ActivoPetroleroIn(BaseModel):
    longitud: str
    latitud: str


class ActivoPetroleroOut(BaseModel):
    id: int
    longitud: str
    latitud: str
    tema_sns: str
