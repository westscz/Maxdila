from maxdila.drug import Drug
import unittest


class TestDrug(unittest.TestCase):
    def setUp(self):
        self.obj = Drug('Hash')

    def test__drug_init(self):
        self.assertEqual(self.obj.name, 'Hash')
        self.assertEqual(self.obj.price, 0)

    def test__add(self):
        self.obj.price = 20
        self.obj.quantity = 15
        obj2 = Drug('Hash')
        obj2.price = 22
        obj2.quantity = 10
        result = self.obj + obj2
        self.assertEqual(result.quantity, 25)
