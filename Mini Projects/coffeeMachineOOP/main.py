""" Program Requirements:
      1. Print Report (C)
      2. Check resources sufficient?
      3. Process coins.
      4. Check transaction successful?
      5. Make coffee.
"""

# Call the 4 classes.
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects.
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
IS_ON = True  #


# While coffee machine is_on.
while IS_ON:
    drink_Items = menu.get_items()  # Get the menu
    # Ask user what kind of coffee they want.
    user_Input = input(f"What would you like? ({drink_Items}): ")

    # OFF
    if user_Input == "off":
        IS_ON = False
    elif user_Input == "report":
        # Print a reports.
        money_machine.report()
        coffee_maker.report()
    else:
        drink_Choice = menu.find_drink(user_Input)

        # Check if resource is sufficient, and if transaction is successful.
        if coffee_maker.is_resource_sufficient(drink_Choice) and money_machine.make_payment(drink_Choice.cost):
            coffee_maker.make_coffee(drink_Choice)
