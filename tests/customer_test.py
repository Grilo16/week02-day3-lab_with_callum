import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.thomas = Customer("Thomas", 100.00, 30)
        self.callum = Customer("Callum", 1.00, 32)
        self.underage_guy = Customer("Todd", 1000, 17)
        self.pub = Pub("The Prancing Pony", 100.00)
        random_drink = Drink("Vodka", 4.50, 1)
        self.pub.add_drink_to_drinks(random_drink)

    def test_can_afford_drink(self):
        drink = self.pub.drinks[0]
        can_afford = self.thomas.can_afford_drink(drink)
        self.assertEqual(True, can_afford)

    def test_cannot_afford_drink(self):
        drink = self.pub.drinks[0]
        can_afford = self.callum.can_afford_drink(drink)
        self.assertEqual(False, can_afford)

    def test_use_money(self):
        drink_object = self.pub.drinks[0]
        self.thomas.use_money(drink_object)
        self.assertEqual(95.5, self.thomas.wallet)

