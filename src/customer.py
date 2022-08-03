class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkness = 0

    def give_money(self, amount):
        self.wallet -= amount
        
    def drink(self, drink_units):
        self.drunkness += drink_units
    
    def eat(self, food_sobering):
        self.drunkness -= food_sobering
        if self.drunkness < 0:
            self.drunkness = 0