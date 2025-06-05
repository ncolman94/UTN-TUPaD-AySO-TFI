import unittest
from src.calculadora import suma, resta, multiplicacion, division, potencia

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(4, 3), 12)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(10, 0), "No se puede dividir por cero")

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)
        self.assertEqual(potencia(3, 1), 3)

if __name__ == '__main__':
    unittest.main()
