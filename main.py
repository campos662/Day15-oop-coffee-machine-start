from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# TODO 1 Turn off machine
game_on = True

# TODO 2 Print report

# TODO 3 Prompt user
while game_on:
    options = menu.get_items()
    choice = input(f"What do you like to drink? {options}: ")
    if choice == "off":
        game_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost) == True :
            coffee_maker.make_coffee(drink)

# TODO 4 Check resources

# TODO 5 Request payment

# TODO 6 Check payment

# TODO 7 Make coffee

