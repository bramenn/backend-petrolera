from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

from .. import db


class EventoActivoPetrolero(db.Base):
    __tablename__ = "evento_activo_petrolero"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    mensaje = Column(
        "mensaje",
        String(255),
    )
    id_activo_petrolero = Column(Integer, ForeignKey("activo_petrolero.id"))


class EventoActivoPetroleroIn(BaseModel):
    mensaje: str
    id_activo_petrolero: int


class EventoActivoPetroleroOut(BaseModel):
    id: int
    mensaje: str
    id_activo_petrolero: int
