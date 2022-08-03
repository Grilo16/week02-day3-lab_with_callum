# Define a pub class that takes a name(string) and a till(int)
class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        # initialize drinks list which will contain dictionaries : {"drink": drink_object, "drink_name": string, "stock_count": int}
        self.drinks = []
        # initialize foods dictionary : {"food": food_object, "food_name": string,  "stock_count": int}
        self.foods = []

    # Define functions to increase and decrease money in the till where amount is an int
    def money_in(self, amount):
        self.till += amount
        
    def money_out(self, amount):
        self.till -= amount
        
    # Define a function to add drinks to stock, correcly formated
    def add_drink_to_stock(self, drink_object, amount):
        # Check if item already exists in stock
        for drink in self.drinks:
            # if it does add amount to current item stock
            if drink_object in drink.values():
                drink["stock_count"] += amount
                return
                
        # if not insert item into the drinks list
        output = {}
        # Format the dictionary from the object
        output["name"] = drink_object.name 
        output["stock_count"] = amount
        output["drink_object"] = drink_object
        self.drinks.append(output)
        
    # Function to add food to stock
    def add_food_to_stock(self, food_object, amount):
        # Check if item already exists in stock
        for food in self.foods:
            # if it does add amount to current item stock
            if food_object in food.values():
                food["stock_count"] += amount
                return
                
        # if not insert item into the foods list
        output = {}
        # Format the dictionary from the object
        output["name"] = food_object.name 
        output["stock_count"] = amount
        output["food_object"] = food_object
        self.foods.append(output)
    
    # Function that returns true if customers is > 18 and false otherwise
    def check_customer_age(self, customer_object):
        if customer_object.age >= 18:
            return True
        return False
        

    def check_customer_drunkness(self, customer_object):
        # return false if costuemr is too drunk otherwise return true
        if customer_object.drunkness >= 10:
            return False
        return True
   
    def get_item_by_type_and_name(self, type, name):
        if type == "food":
            for food in self.foods:
                if food["name"] == name:
                    return food
        elif type == "drink":
            for drink in self.drinks:
                if drink["name"] == name:
                    return drink
        else:
            return False
   
    # functions to check if customer can affort the item
    def can_afford_drink(self, customer_object, drink_name):
        if customer_object.wallet >= self.get_item_by_type_and_name("drink", drink_name)["drink_object"].price:
            return True
        return False
    
    def can_afford_food(self, customer_object, food_name):
        if customer_object.wallet >= self.get_item_by_type_and_name("food", food_name)["food_object"].price:
            return True
        return False
    
    # Function to check if the stock of the drink is > 0 
    def check_drink_available_by_name(self, drink_name):
        for drink in self.drinks:
            if drink["name"] == drink_name:
                if drink["stock_count"] > 0:
                    return True
        return False
        
    # Function to check if the stock of the food is > 0 
    def check_food_available_by_name(self, food_name):
        for food in self.foods:
            if food["name"] == food_name:
                if food["stock_count"] > 0:
                    return True
        return False
        
    # Validate if customer can buy a drink 
    def check_can_sell_drink(self, customer_object, drink):
        if not self.check_customer_age(customer_object):
            return False
        if not self.check_customer_drunkness(customer_object):
            return False
        if not self.can_afford_drink(customer_object, drink):
            return False
        if not self.check_drink_available_by_name(drink):
            return False
        return True
        
    # Check can sell food
    def check_can_sell_food(self, customer_object, food_name):
        if not self.check_food_available_by_name(food_name):
            return False
        if not self.can_afford_food(customer_object, food_name):
            return False
        return True
    
    # function to sell a drink by name and customer
    def sell_drink(self, customer_object, drink_name):
        if not self.check_can_sell_drink(customer_object, drink_name):
            return False

        # Get drink object
        drink = self.get_item_by_type_and_name("drink", drink_name)["drink_object"]
        # add drinks price to the till
        self.money_in(drink.price)
        # Take money from customer's wallet
        customer_object.give_money(drink.price)
        # Increase customer drunkness
        customer_object.drink(drink.units) 
        
    # sell food by name and customer
    def sell_food(self, customer_object, food_name):
        if not self.check_can_sell_food(customer_object, food_name):
            return False
        
        # Get food object
        food = self.get_item_by_type_and_name("food", food_name)["food_object"]
        # add foods price to the till
        self.money_in(food.price)        
        # Take money from customer's wallet
        customer_object.give_money(food.price)
        # Decrease customer drunkness
        customer_object.eat(food.sobering)
        
