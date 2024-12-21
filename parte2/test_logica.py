import unittest
from parte2.logica import calcular_factorial, es_palindromo


class TestLogica(unittest.TestCase):
    def test_calcular_factorial(self):
        self.assertEqual(calcular_factorial(5), 120)
        self.assertEqual(calcular_factorial(0), 1)
        with self.assertRaises(ValueError):
            calcular_factorial(-1)

    def test_es_palindromo(self):
        self.assertTrue(es_palindromo("ana"))
        self.assertFalse(es_palindromo("python"))
        self.assertTrue(es_palindromo("radar"))
