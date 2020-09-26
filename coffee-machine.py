class CoffeeMachine:
    
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.enough = 0
        self.water_add = 0
        self.milk_add = 0
        self.beans_add = 0
        self.cups_add = 0
        self.temp_input = None

    def user_input(self):
        self.temp_input = input()
    
    def action(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            self.user_input()
            if self.temp_input == "buy":
                self.action_buy()
            elif self.temp_input == "fill":
                self.action_fill()
            elif self.temp_input == "take":
                self.action_take()
            elif self.temp_input == "remaining":
                self.inventory()
            elif self.temp_input == "exit":
                break

    def action_buy(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.user_input()
        if self.temp_input == "1":
            self.coffee_check(250, 0, 16, 1)
            self.coffee_espresso()
        elif self.temp_input == "2":
            self.coffee_check(350, 75, 20, 1)
            self.coffee_latte()
        elif self.temp_input == "3":
            self.coffee_check(200, 100, 12, 1)
            self.coffee_cappuccino()
        elif self.temp_input == "back":
            pass

    def coffee_check(self, water_need, milk_need, beans_need, cups_need):
        if self.water < water_need:
            print("Sorry, not enough water!")
            print()
            self.enough = 0
        elif self.milk < milk_need:
            print("Sorry, not enough milk!")
            print()
            self.enough = 0
        elif self.beans < beans_need:
            print("Sorry, not enough coffee beans!")
            print()
            self.enough = 0
        elif self.cups < cups_need:
            print("Sorry, not enough disposable cups!")
            print()
            self.enough = 0
        else:
            print("I have enough resources, making you a coffee!")
            print()
            self.enough = 1
    
    def coffee_espresso(self):
        if self.enough == 1:
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
        else:
            pass

    def coffee_latte(self):
        if self.enough == 1:
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
        else:
            pass

    def coffee_cappuccino(self):
        if self.enough == 1:
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
        else:
            pass

    def action_fill(self):
        print()
        print("Write how many ml of water do you want to add:")
        self.user_input()
        self.water_add = int(self.temp_input)
        self.water += self.water_add
        print("Write how many ml of milk do you want to add:")
        self.user_input()
        self.milk_add = int(self.temp_input)
        self.milk += self.milk_add
        print("Write how many grams of coffee beans do you want to add:")
        self.user_input()
        self.beans_add = int(self.temp_input)
        self.beans += self.beans_add
        print("Write how many disposable cups of coffee do you want to add:")
        self.user_input()
        self.cups_add = int(self.temp_input)
        self.cups += self.cups_add
        print()
    
    def action_take(self):
        print()
        print("I gave you $" + str(self.money))
        print()
        self.money = 0

    def inventory(self):
        print()
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")
        print()


test = CoffeeMachine()
test.action()
