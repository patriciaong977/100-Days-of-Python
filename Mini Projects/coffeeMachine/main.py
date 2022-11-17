""" Import the MENU and Resources from menuResources.py """
from menuResources import MENU, resources




# TODO: PROCESS coins.
# TODO: CHECK transaction successful.
# TODO: MAKE COFFEE.

IS_ON = True

while IS_ON: # while True:
    # PROMPT user by asking "What would you like? (espresso/latte/cappuccino): "
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Check the user's input and decide what to do next.
    if choice == "off":
        # TURN off the Coffee Machine by entering "off" to the prompt.
        IS_ON = False
    elif choice == "report":  # PRINT REPORT by entering "report" to the prompt.
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        drink = MENU[choice]
        # CHECK resources sufficient.
