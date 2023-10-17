from app.responsable.consultas import parsear_responsable
from app.responsable.modelo import Responsable, ResponsableOut


def test_parsear_responsable():
    responsable = Responsable(
        id=1,
        nombre_completo="Brayan Alejandro Herrera Amariles",
        correo_electronico="brayan@test.com",
        telefono="+573123456789",
    )

    responsable_out = ResponsableOut(
        id=1,
        nombre_completo="Brayan Alejandro Herrera Amariles",
        correo_electronico="brayan@test.com",
        telefono="+573123456789",
    )

    assert responsable_out == parsear_responsable(responsable)
