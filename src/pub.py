class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_drink_to_drinks(self, drink_object):
        self.drinks.append(drink_object)

    def increase_till(self, drink_object):
        self.till += drink_object.price

    def food_sale(self, person, food_choice):
        if person.use_money(food_choice):
            self.increase_till(food_choice)
            if person.drunkness == 0:
                return
            else:    
                person.drunkness -= food_choice.sobering
            
    


