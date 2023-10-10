from pydantic import BaseModel
from sqlalchemy import Column, Integer, UniqueConstraint
from sqlalchemy.sql.schema import ForeignKey

from .. import db


class Suscripcion(db.Base):
    __tablename__ = "suscripcion"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    id_responsable = Column(Integer, ForeignKey("responsable.id"))
    id_activo_petrolero = Column(Integer, ForeignKey("activo_petrolero.id"))
    UniqueConstraint("id_responsable", "id_activo_petrolero", name="responsable_activo_petrolero"),


class SuscripcionIn(BaseModel):
    id_responsable: int
    id_activo_petrolero: int


class SuscripcionOut(BaseModel):
    id: int
    id_responsable: int
    id_activo_petrolero: int
