import pytest
from rutcl import calcular_dv, validar_rut, formatear_rut, limpiar_rut


class TestLimpiarRut:
    def test_con_puntos_y_guion(self):
        assert limpiar_rut("12.345.678-5") == "123456785"

    def test_sin_formato(self):
        assert limpiar_rut("123456785") == "123456785"

    def test_con_espacios(self):
        assert limpiar_rut("12.345.678 - 5") == "123456785"

    def test_dv_k_minuscula(self):
        assert limpiar_rut("12345678-k") == "12345678K"

    def test_rut_vacio(self):
        assert limpiar_rut("") == ""


class TestCalcularDv:
    def test_12345678(self):
        assert calcular_dv("12345678") == "5"

    def test_11111111(self):
        assert calcular_dv("11111111") == "1"

    def test_22222222(self):
        assert calcular_dv("22222222") == "2"

    def test_con_puntos(self):
        assert calcular_dv("12.345.678") == "5"

    def test_con_guion(self):
        assert calcular_dv("9-8765432") == "5"

    def test_ministerio_hacienda(self):
        assert calcular_dv("60803000") == "K"

    def test_digito_unico(self):
        assert calcular_dv("1") == "9"


class TestFormatearRut:
    def test_rut_largo(self):
        assert formatear_rut("123456785") == "12.345.678-5"

    def test_rut_corto(self):
        assert formatear_rut("15") == "1-5"

    def test_ya_formateado(self):
        assert formatear_rut("12.345.678-5") == "12.345.678-5"

    def test_dv_k(self):
        assert formatear_rut("12345678K") == "12.345.678-K"

    def test_cuerpo_sin_puntos(self):
        assert formatear_rut("12345678") == "1.234.567-8"

    def test_rut_7_digitos(self):
        assert formatear_rut("12345675") == "1.234.567-5"


class TestValidarRut:
    def test_rut_valido(self):
        assert validar_rut("12.345.678-5") is True

    def test_rut_valido_sin_formato(self):
        assert validar_rut("123456785") is True

    def test_rut_invalido(self):
        assert validar_rut("12.345.678-9") is False

    def test_rut_con_k_valido(self):
        assert validar_rut("60803000-K") is True

    def test_rut_con_k_invalido(self):
        assert validar_rut("60803000-0") is False

    def test_rut_vacio(self):
        assert validar_rut("") is False

    def test_rut_un_digito(self):
        assert validar_rut("5") is False

    def test_varios_ruts_validos(self):
        ruts = [
            "12345678-5",
            "60803000-K",
            "11111111-1",
            "22222222-2",
            "98765432-5",
        ]
        for rut in ruts:
            assert validar_rut(rut) is True, f"{rut} deberia ser valido"

    def test_redondeo_a_cero(self):
        assert validar_rut("10000000-8") is True
