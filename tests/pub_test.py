import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):

    # Set up mock situation
    def setUp(self):
        # Initialize a pub with 1000 on the till
        self.pub = Pub("The King's Goat", 1000)
        
        # Initialize 4 drinks
        self.drink1 = Drink("Beer", 3, 1)
        self.drink2 = Drink("Wine", 5, 2)
        self.drink3 = Drink("Whisky", 8, 3)
        self.drink4 = Drink("Whisky 65yo", 1500, 3)
        
        # Initialize 3 foods
        self.food1 = Food("Chips", 5 , 1)
        self.food2 = Food("Burger", 10 , 5)
        self.food3 = Food("Steak", 20 , 10)
        
        # Initialize 4 customers
        self.customer1 = Customer("Tom", 100, 30)
        self.customer2 = Customer("Callum", 100, 32)
        self.customer3 = Customer("Hobo Bob", 4, 74)
        # Making hobo bob drunk
        self.customer3.drunkness = 27
        self.customer4 = Customer("Cheeky Teenager", 10, 15)
        
    
    # Test pub has a name
    def test_pub_has_name(self):
        self.assertEqual("The King's Goat", self.pub.name)

    # Test pub has a till
    def test_has_till(self):
        self.assertEqual(1000, self.pub.till)
    
    # Test adding to the till
    def test_money_in(self):
        self.pub.money_in(500)
        self.assertEqual(1500, self.pub.till)
        
    # Test removing from the till
    def test_money_out(self):
        self.pub.money_out(500)
        self.assertEqual(500, self.pub.till)

    # Test adding a drink to stock for the first time
    def test_add_new_drinks_to_stock(self):
        self.pub.add_drink_to_stock(self.drink1, 50)
        drink = self.pub.drinks[0]
        # Check first drink name is beer
        self.assertEqual("Beer", drink["name"])
        # Check first drink stock is 50
        self.assertEqual(50, drink["stock_count"])
        # Check drinks list only has 1 item
        self.assertEqual(1, len(self.pub.drinks))
    
    # Test adding to the stock of a drink item already in the list
    def test_add_repeat_drinks_to_stock(self):
        self.pub.add_drink_to_stock(self.drink1, 50)
        self.pub.add_drink_to_stock(self.drink1, 50)
        drink = self.pub.drinks[0]
        # Check list is still only one item
        self.assertEqual(1, len(self.pub.drinks))
        # Check stock count of that item has increased to 100
        self.assertEqual(100, drink["stock_count"])
        
    # Test adding a food to stock for the first time
    def test_add_new_foods_to_stock(self):
        self.pub.add_food_to_stock(self.food1, 50)
        food = self.pub.foods[0]
        # Check first food name is Chips
        self.assertEqual("Chips", food["name"])
        # Check first food stock is 50
        self.assertEqual(50, food["stock_count"])
        # Check foods list only has 1 item
        self.assertEqual(1, len(self.pub.foods))
    
    # Test adding to the stock of a food item already in the list
    def test_add_repeat_food_to_stock(self):
        self.pub.add_food_to_stock(self.food1, 50)
        self.pub.add_food_to_stock(self.food1, 50)
        food = self.pub.foods[0]
        # Check list is still only one item
        self.assertEqual(1, len(self.pub.foods))
        # Check stock count of that item has increased to 100
        self.assertEqual(100, food["stock_count"])
    
    # Check if adults appropriately return true 
    def test_check_customer_age_over18(self):
        check_result = self.pub.check_customer_age(self.customer1)
        self.assertEqual(True, check_result)

    # Check if underage kids return false
    def test_check_customer_age_underage(self):
        check_result = self.pub.check_customer_age(self.customer4)
        self.assertEqual(False, check_result)
        
    # Check returns false if too drunk
    def test_check_drunkness_drunk(self):
        self.customer1.drunkness = 15
        check_result = self.pub.check_customer_drunkness(self.customer1)
        self.assertEqual(False, check_result)
        
    # Check return True for sober
    def test_check_drunkness_sober(self):
        check_result = self.pub.check_customer_drunkness(self.customer1)
        self.assertEqual(True, check_result)
        
    # Testing a function to get a drink or a food item by name
    def test_get_item_by_type_and_name(self):
        self.pub.add_food_to_stock(self.food2, 50)
        item = self.pub.get_item_by_type_and_name("food", "Burger")
        self.assertEqual("Burger", item["name"])
        self.assertEqual(50, item["stock_count"])
        
    # test returns true when costumer can afford drinks
    def test_can_afford_drink(self):
        self.pub.add_drink_to_stock(self.drink3, 50)
        check_result = self.pub.can_afford_drink(self.customer1, "Whisky")
        self.assertEqual(True, check_result)
    
    # test returns false when customer cannot afford drinks
    def test_cannot_afford_drink(self):
        self.pub.add_drink_to_stock(self.drink3, 50)
        check_result = self.pub.can_afford_drink(self.customer3, "Whisky")
        self.assertEqual(False, check_result)

    # test returns true when costumer can afford foods
    def test_can_afford_food(self):
        self.pub.add_food_to_stock(self.food3, 50)
        check_result = self.pub.can_afford_food(self.customer2, "Steak")
        self.assertEqual(True, check_result)
    
    # test returns false when customer cannot afford foods
    def test_cannot_afford_food(self):
        self.pub.add_food_to_stock(self.food3, 50)
        check_result = self.pub.can_afford_food(self.customer3, "Steak")
        self.assertEqual(False, check_result)
       
    # Checks it returns true when drink is in stock
    def test_check_drink_available(self):
        self.pub.add_drink_to_stock(self.drink2, 10)
        check_result = self.pub.check_drink_available_by_name("Wine")
        self.assertEqual(True, check_result)

    # Check it returns false when drink not available
    def test_check_drink_not_available(self):
        check_result = self.pub.check_drink_available_by_name("Frangelico")
        self.assertEqual(False, check_result)
        
    # Checks it returns true when food is in stock
    def test_check_food_available(self):
        self.pub.add_food_to_stock(self.food2, 10)
        check_result = self.pub.check_food_available_by_name("Burger")
        self.assertEqual(True, check_result)

    # Check it returns false when food not available
    def test_check_food_not_available(self):
        check_result = self.pub.check_food_available_by_name("Banana")
        self.assertEqual(False, check_result)
    
    
    # Check if can sell drink returns true under the apropriate conditions
    def test_check_can_sell_drink(self):
        self.pub.add_drink_to_stock(self.drink3, 10)
        check_result = self.pub.check_can_sell_drink(self.customer1, "Whisky")
        self.assertEqual(True, check_result)
        
    # Check it returns false if customer is too drunk
    def test_check_can_sell_to_hobo_bob(self):
        self.pub.add_drink_to_stock(self.drink1, 10)
        check_result = self.pub.check_can_sell_drink(self.customer3, "Beer")
        self.assertEqual(False, check_result)
        
    # Check it returns false if customer is underage
    def test_check_can_sell_to_cheeky_teenager(self):
        self.pub.add_drink_to_stock(self.drink1, 10)
        check_result = self.pub.check_can_sell_drink(self.customer4, "Beer")
        self.assertEqual(False, check_result)
        
    # Check it returns false if customer doesnt have money
    def test_check_can_sell_to_omega_expensive(self):
        self.pub.add_drink_to_stock(self.drink4, 1)
        check_result = self.pub.check_can_sell_drink(self.customer2, "Whisky 65yo")
        self.assertEqual(False, check_result)
    
    # Check it returns false if item not in stock
    def test_check_can_sell_drink_not_available(self):
        self.pub.add_drink_to_stock(self.drink1, 0)
        check_result = self.pub.check_can_sell_drink(self.customer2, "Beer")
        self.assertEqual(False, check_result)
            
    # Check if can sell food returns true under the apropriate conditions
    def test_check_can_sell_food(self):
        self.pub.add_food_to_stock(self.food3, 10)
        check_result = self.pub.check_can_sell_food(self.customer1, "Steak")
        self.assertEqual(True, check_result)
    
    # Check it returns false if item not in stock
    def test_check_can_sell_food_not_available(self):
        self.pub.add_food_to_stock(self.food1, 0)
        check_result = self.pub.check_can_sell_food(self.customer2, "Chips")
        self.assertEqual(False, check_result)
        
    # Checks if drink is sold, money is taken, drunkness is increased 
    def test_sell_drink_successfull(self):
        self.pub.add_drink_to_stock(self.drink3, 10)
        self.pub.sell_drink(self.customer1, "Whisky")
        self.assertEqual(92, self.customer1.wallet)
        self.assertEqual(1008, self.pub.till)
        self.assertEqual(3, self.customer1.drunkness)
        self.assertEqual(9, self.pub.get_item_by_type_and_name("drink","Whisky")["stock_count"])
        
    # Checks if drink is not sold, money is taken, drunkness stays the same
    # failed by drink too expensive
    def test_sell_drink_unsuccessfull_too_expensive(self):
        self.pub.add_drink_to_stock(self.drink4, 10)
        self.pub.sell_drink(self.customer1, "Whisky 65yo")
        self.assertEqual(100, self.customer1.wallet)
        self.assertEqual(1000, self.pub.till)
        self.assertEqual(0, self.customer1.drunkness)
        self.assertEqual(10, self.pub.get_item_by_type_and_name("drink","Whisky 65yo")["stock_count"])
        
    # failed by drink not in stock
    def test_sell_drink_unsuccessfull_unavailable(self):
        self.pub.add_drink_to_stock(self.drink2, 0)
        self.pub.sell_drink(self.customer1, "Wine")
        self.assertEqual(100, self.customer1.wallet)
        self.assertEqual(1000, self.pub.till)
        self.assertEqual(0, self.customer1.drunkness)
        self.assertEqual(0, self.pub.get_item_by_type_and_name("drink","Wine")["stock_count"])
    
        
    # Checks if food is sold, money is taken, drunkness is decreased
    def test_sell_food_successfull(self):
        # Giving a pound to hobo bob
        self.customer3.wallet += 1
        
        self.pub.add_food_to_stock(self.food1, 10)
        self.pub.sell_food(self.customer3, "Chips")
        self.assertEqual(0, self.customer3.wallet)
        self.assertEqual(1005, self.pub.till)
        self.assertEqual(26, self.customer3.drunkness)
        self.assertEqual(9, self.pub.get_item_by_type_and_name("food","Chips")["stock_count"])
        
    # Checks if food is not sold, money is taken, drunkness stays the same
    # failed by food too expensive
    def test_sell_food_unsuccessfull_too_expensive(self):
        self.pub.add_food_to_stock(self.food3, 10)
        self.pub.sell_food(self.customer3, "Steak")
        self.assertEqual(4, self.customer3.wallet)
        self.assertEqual(1000, self.pub.till)
        self.assertEqual(27, self.customer3.drunkness)
        self.assertEqual(10, self.pub.get_item_by_type_and_name("food","Steak")["stock_count"])
        
    # failed by food not in stock
    def test_sell_food_unsuccessfull_unavailable(self):
        self.pub.add_food_to_stock(self.food2, 0)
        self.pub.sell_food(self.customer2, "Burger")
        self.assertEqual(100, self.customer2.wallet)
        self.assertEqual(1000, self.pub.till)
        self.assertEqual(0, self.customer2.drunkness)
        self.assertEqual(0, self.pub.get_item_by_type_and_name("food","Burger")["stock_count"])
    