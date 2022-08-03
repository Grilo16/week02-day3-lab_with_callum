import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Whisky", 5.00, 1)