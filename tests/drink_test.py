import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Whisky", 5.00, 1)
        
    def test_drink_has_a_name(self):
        self.assertEqual("Whisky", self.drink.name)