from ..app.evento_activo_petrolero.consultas import parsear_evento_activo_petrolero
from ..app.evento_activo_petrolero.modelo import EventoActivoPetrolero, EventoActivoPetroleroOut


def test_parsear_evento_activo_petrolero():
    evento_activo_petrolero = EventoActivoPetrolero(
        id=1, mensaje="Mensaje de prueba", id_activo_petrolero=1
    )

    evento_activo_petrolero_out = EventoActivoPetroleroOut(
        id=1, mensaje="Mensaje de prueba", id_activo_petrolero=1
    )

    assert evento_activo_petrolero_out == parsear_evento_activo_petrolero(evento_activo_petrolero)
