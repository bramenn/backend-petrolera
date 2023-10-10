from typing import List

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .. import db
from ..suscripcion.modelo import Suscripcion


class Responsable(db.Base):
    __tablename__ = "responsable"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    nombre_completo = Column("nombre_completo", String(255), unique=True)
    correo_electronico = Column("correo_electronico", String(255), unique=True)
    telefono = Column("telefono", String(255), unique=True)
    suscripciones = relationship(Suscripcion)


class ResponsableIn(BaseModel):
    nombre_completo: str
    correo_electronico: str
    telefono: str


class ResponsableOut(BaseModel):
    id: int
    nombre_completo: str
    correo_electronico: str
    telefono: str
