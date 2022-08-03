from itertools import filterfalse
from src.pub import Pub

class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkness = 0

    def can_afford_drink(self, drink):
        if self.wallet >= drink.price:
            return True
        else:
            return False

    def use_money(self, amount):
        if self.can_afford_drink(amount):
            self.wallet -= amount.price
            return True
        else:
            return False