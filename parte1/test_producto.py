import unittest
from parte1.producto import Producto


class TestProducto(unittest.TestCase):
    def test_calcular_precio_total(self):
        producto = Producto("Laptop", 1200.0, 2)
        self.assertEqual(producto.calcular_precio_total(), 2400.0)

    def test_descripcion_correcta(self):
        producto = Producto("Celular", 800.0, 1)
        self.assertEqual(producto.descripcion, "Celular")

    def test_cantidad_incorrecta(self):
        with self.assertRaises(ValueError):
            Producto("TV", 500.0, -3)
