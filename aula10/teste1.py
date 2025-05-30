import unittest

def soma(a, b):
    return a + b

class TestSoma(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

    def test_soma_positivo_negativo(self):
        self.assertEqual(soma(-1, 1), 0)

    def test_soma_float(self):
        self.assertEqual(soma(5.5, 0.5), 6)
        
if __name__ == '__main__':
    unittest.main()
