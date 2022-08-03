import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

# creating a class called TestPub thats parameters is inherited from unittest.TestCase


class TestPub(unittest.TestCase):

    def setUp(self):
        self.thomas = Customer("Thomas", 100.00, 30)
        self.callum = Customer("Callum", 1.00, 32)
        self.underage_guy = Customer("Todd", 1000, 17)
        self.drunk_guy = Customer("Hobo Bob", 5, 75)
        self.pub = Pub("The Prancing Pony", 100.00)
        random_drink = Drink("Vodka", 4.50, 1)
        self.pub.add_drink_to_drinks(random_drink)

    # the above function is called the Pub class and assinging the pub name as The Prancing Pony and the till
    # float of 100.00. setUp(self) will always reset the pub back to these initial parameters.

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_had_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(self.pub.drinks[0])
        self.assertEqual(104.50, self.pub.till)

    # this can also be written in the format below which will assign variables which are passed as arguments
    # the self asset arguments.

    # def test_add(self):
    #     self.pub.increase_till(2.50)
    #     expected = 102.50
    #     actual = self.pub.till
    #     self.assertEqual(expected, actual)

    def test_add_drink_to_drinks(self):
        self.assertEqual(1, len(self.pub.drinks))

    def test_drink_sale_successful_money(self):
        drink = self.pub.drinks[0]
        self.pub.drink_sale(self.thomas, drink)
        self.assertEqual(104.5, self.pub.till)
        self.assertEqual(1, self.thomas.drunkness)

    def test_drink_sale_unsuccessful_money(self):
        drink = self.pub.drinks[0]
        self.pub.drink_sale(self.callum, drink)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(0, self.callum.drunkness)

    def test_drink_sale_unsuccessful_underage(self):
        drink = self.pub.drinks[0]
        self.pub.drink_sale(self.underage_guy, drink)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(0, self.underage_guy.drunkness)
    
    def test_drink_sale_unsuccessful_underage(self):
        self.drunk_guy.drunkness = 12
        drink = self.pub.drinks[0]
        self.pub.drink_sale(self.drunk_guy, drink)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(12, self.drunk_guy.drunkness)

