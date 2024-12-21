import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Carga de pruebas
    suite.addTests(loader.discover("./parte1", pattern="test_*.py"))
    suite.addTests(loader.discover("./parte2", pattern="test_*.py"))

    # Ejecución de pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)

    # Generar puntuación
    total_tests = resultado.testsRun
    fallos = len(resultado.failures)
    errores = len(resultado.errors)

    exito = total_tests - (fallos + errores)
    puntuacion = (exito / total_tests) * 100

    print("\nResumen de la prueba técnica:")
    print(f"Total de pruebas ejecutadas: {total_tests}")
    print(f"Pruebas exitosas: {exito}")
    print(f"Pruebas fallidas: {fallos}")
    print(f"Errores en pruebas: {errores}")
    print(f"Puntuación final: {puntuacion:.2f}%")
