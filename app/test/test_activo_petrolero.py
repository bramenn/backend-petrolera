from app.activo_petrolero.consultas import parsear_activo_petrolero
from app.activo_petrolero.modelo import ActivoPetrolero, ActivoPetroleroOut


def test_parsear_activo_petrolero():
    activo_petrolero = ActivoPetrolero(
        id=1,
        longitud="23.6345",
        latitud="102.5528",
        tema_sns="arn:aws:sns:us-east-1:test:activo-petrolero-1",
    )

    activo_petrolero_out = ActivoPetroleroOut(
        id=1,
        longitud="23.6345",
        latitud="102.5528",
        tema_sns="arn:aws:sns:us-east-1:test:activo-petrolero-1",
    )

    assert activo_petrolero_out == parsear_activo_petrolero(activo_petrolero)
