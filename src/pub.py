
class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.fridge = []
        self.fridge_stock = {}


    def add_drink_to_drinks(self, drink_object):
        self.drinks.append(drink_object)


    def add_food_to_fridge(self, food_object, amount):
        self.fridge.append(food_object)
        self.fridge_stock[food_object.name] = amount

    def increase_till(self, drink_object):
        self.till += drink_object.price

    def drink_sale(self, person, drink_choice):
        if person.drunkness <= 10:
            if person.use_money(drink_choice) and person.age >= 18:
                self.increase_till(drink_choice)
                person.drunkness += drink_choice.units

    def food_sale(self, person, food_choice):
        if person.use_money(food_choice):
            self.increase_till(food_choice)
            if person.drunkness == 0:
                return
            else:
                person.drunkness -= food_choice.sobering
    


