import unittest
from src.food import Food


class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food("Burger", 4, 1, 10)