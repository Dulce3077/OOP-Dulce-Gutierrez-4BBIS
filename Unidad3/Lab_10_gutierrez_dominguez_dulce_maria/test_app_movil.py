
import pytest

from app_movil import (
    PerfilMovil,
    PerfilPro,
    SuscripcionExpiradaError,
    PuntosInsuficientesError
)

@pytest.fixture
def perfil():
    return PerfilMovil("Dulce")

def test_atributos_iniciales(perfil):
    assert perfil.username == "Dulce"
    assert perfil.gemas == 50
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


@pytest.mark.parametrize("cantidad, esperado", [
    (10, 60),
    (20, 70),
    (50, 100)
])
def test_ganar_gemas(perfil, cantidad, esperado):
    assert perfil.ganar_gemas(cantidad) == esperado


@pytest.mark.parametrize("cantidad", [0, -5])
def test_ganar_gemas_invalidas(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)


def test_gastar_gemas(perfil):
    assert perfil.gastar_gemas(20) == 30


def test_gemas_insuficientes(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(100)


def test_gastar_gemas_invalidas(perfil):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(-10)


def test_gemas_negativas():
    with pytest.raises(ValueError):
        PerfilMovil("Dulce", gemas=-10)


def test_herencia():
    perfil_pro = PerfilPro("Dulce", 3)

    assert isinstance(perfil_pro, PerfilMovil)
    assert isinstance(perfil_pro, PerfilPro)
    assert perfil_pro.es_pro is True


def test_descarga_offline():
    perfil_pro = PerfilPro("Dulce", 3)

    resultado = perfil_pro.descargar_contenido_offline()

    assert resultado == "Descarga de contenido offline exitosa."


def test_suscripcion_expirada():
    perfil_pro = PerfilPro("Dulce", 1)

    perfil_pro.meses_suscripcion = 0

    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()

    assert perfil_pro.es_pro is False


def test_suscripcion_invalida():
    with pytest.raises(ValueError):
        PerfilPro("Dulce", 0)
