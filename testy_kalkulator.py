import unittest
import kalkulator

class testy_kalkulator(unittest.TestCase):

    def test_dodawanie(self):
        wynik = kalkulator.dodaj(2,3)
        self.assertEqual(wynik,5)
        self.assertNotEqual(wynik, 2)

    def test_odejmowanie(self):
        wynik = kalkulator.odejmij(4, 3)
        self.assertEqual(wynik,1)
        self.assertNotEqual(wynik, 2)

    def test_mnozenie(self):
        wynik = kalkulator.pomnoz(2,3)
        self.assertEqual(wynik,6)
        self.assertNotEqual(wynik, 7)

    def test_dzielenie(self):
        wynik = kalkulator.podziel(6,3)
        self.assertEqual(wynik,2)
        self.assertNotEqual(wynik, 4)

if __name__== '__main__':
    unittest.main()
