import unittest
from agricultor import agro_decisor_tupla

class TestAgroDecisorTupla(unittest.TestCase):

    def test_prev_chuva(self):
        self.assertEqual(agro_decisor_tupla((28.0, 60.0, 1)), 'NÃO REGAR')

    def test_temp_alta_umid_baixa_sem_chuva(self):
        self.assertEqual(agro_decisor_tupla((35.0, 40.0, 0)), 'REGAR')

    def test_temp_alta_umid_alta_sem_chuva(self):
        self.assertEqual(agro_decisor_tupla((35.0, 60.0, 0)), 'NÃO REGAR')

    def test_temp_baixa_umid_baixa_sem_chuva(self):
        self.assertEqual(agro_decisor_tupla((25.0, 40.0, 0)), 'NÃO REGAR')

    def test_temp_baixa_umid_alta_sem_chuva(self):
        self.assertEqual(agro_decisor_tupla((25.0, 60.0, 0)), 'NÃO REGAR')

    def test_temp_limite_30_umid_baixa_sem_chuva(self):
        self.assertEqual(agro_decisor_tupla((30.0, 40.0, 0)), 'NÃO REGAR')

    def test_temp_maior_30_umid_limite_50_sem_chuva(self):
        self.assertEqual(agro_decisor_tupla((31.0, 50.0, 0)), 'NÃO REGAR')

    def test_temp_maior_30_umid_menor_50_sem_chuva(self):
        self.assertEqual(agro_decisor_tupla((31.0, 49.9, 0)), 'REGAR')

    def test_chuva_temp_alta_umid_baixa(self):
        self.assertEqual(agro_decisor_tupla((35.0, 20.0, 1)), 'NÃO REGAR')

    def test_chuva_temp_baixa_umid_baixa(self):
        self.assertEqual(agro_decisor_tupla((20.0, 20.0, 1)), 'NÃO REGAR')

    def test_chuva_temp_baixa_umid_alta(self):
        self.assertEqual(agro_decisor_tupla((20.0, 90.0, 1)), 'NÃO REGAR')

    def test_sem_chuva_temp_muito_alta_umid_alta(self):
        self.assertEqual(agro_decisor_tupla((40.0, 80.0, 0)), 'NÃO REGAR')

    def test_sem_chuva_temp_muito_alta_umid_muito_baixa(self):
        self.assertEqual(agro_decisor_tupla((40.0, 10.0, 0)), 'REGAR')

    def test_temp_baixa_umid_limite_50_sem_chuva(self):
        self.assertEqual(agro_decisor_tupla((25.0, 50.0, 0)), 'NÃO REGAR')

    def test_temp_exatamente_30_umid_exatamente_50_sem_chuva(self):
        self.assertEqual(agro_decisor_tupla((30.0, 50.0, 0)), 'NÃO REGAR')

    def test_temp_abaixo_30_umid_abaixo_50_sem_chuva(self):
        self.assertEqual(agro_decisor_tupla((29.0, 40.0, 0)), 'NÃO REGAR')

    def test_temp_31_umid_49_chuva(self):
        self.assertEqual(agro_decisor_tupla((31.0, 49.0, 1)), 'NÃO REGAR')

    def test_temp_negativa_com_chuva(self):
        self.assertEqual(agro_decisor_tupla((-5.0, 70.0, 1)), 'NÃO REGAR')

    def test_temp_negativa_sem_chuva_umid_baixa(self):
        self.assertEqual(agro_decisor_tupla((-5.0, 40.0, 0)), 'NÃO REGAR')

    def test_temp_extrema_umid_extrema_sem_chuva(self):
        self.assertEqual(agro_decisor_tupla((50.0, 5.0, 0)), 'REGAR')


if __name__ == '__main__':
    unittest.main()