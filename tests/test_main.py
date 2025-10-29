import pytest
from main import suma, es_par


class TestSuma:
    """Clase de pruebas para la función suma"""

    def test_suma_positivos(self):
        """Test con números positivos"""
        assert suma(5, 3) == 8.0

    def test_suma_negativos(self):
        """Test con números negativos"""
        assert suma(-5, -3) == -8.0

    def test_suma_cero(self):
        """Test con cero"""
        assert suma(0, 0) == 0.0

    def test_suma_decimales(self):
        """Test con números decimales"""
        assert suma(2.5, 3.1) == pytest.approx(5.6)

    def test_suma_tipos_mezclados(self):
        """Test con enteros y decimales"""
        assert suma(2, 3.5) == 5.5


class TestEsPar:
    """Clase de pruebas para la función es_par"""

    def test_par_positivo(self):
        """Test con número par positivo"""
        assert es_par(4) is True

    def test_impar_positivo(self):
        """Test con número impar positivo"""
        assert es_par(7) is False

    def test_par_negativo(self):
        """Test con número par negativo"""
        assert es_par(-4) is True

    def test_impar_negativo(self):
        """Test con número impar negativo"""
        assert es_par(-7) is False

    def test_cero(self):
        """Test con cero (considerado par)"""
        assert es_par(0) is True


if __name__ == "__main__":
    pytest.main()
