from app.suscripcion.consultas import parsear_suscripcion
from app.suscripcion.modelo import Suscripcion, SuscripcionOut


def test_parsear_suscripcion():
    suscripcion = Suscripcion(
        id=1,
        id_responsable=1,
        id_activo_petrolero=1,
    )

    suscripcion_out = SuscripcionOut(
        id=1,
        id_responsable=1,
        id_activo_petrolero=1,
    )

    assert suscripcion_out == parsear_suscripcion(suscripcion)
