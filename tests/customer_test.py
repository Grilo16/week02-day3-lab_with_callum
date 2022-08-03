import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer1 = Customer("Tom", 100, 30)
        self.customer2 = Customer("Callum", 100, 32)
    
    def test_give_money(self):
        self.customer1.give_money(31)
        self.assertEqual(69, self.customer1.wallet)
        
    def test_drink(self):
        self.customer2.drink(5)
        self.assertEqual(5, self.customer2.drunkness)
    
    def test_eat(self):
        self.customer2.drink(5)
        self.customer2.eat(4)
        self.assertEqual(1, self.customer2.drunkness)
        
    def test_eat_more_than_drunkness(self):
        self.customer1.drink(5)
        self.customer1.eat(10)
        self.assertEqual(0, self.customer1.drunkness)

   