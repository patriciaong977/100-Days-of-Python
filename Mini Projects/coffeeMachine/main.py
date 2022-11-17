""" Import the MENU and Resources from menuResources.py """
from menuResources import MENU, resources


# CHECK resources sufficient.
def check_resource_sufficient(order_ingredients):
    """ Return true if the resources are sufficient, false if not. """
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False

# PROCESS coins.
def process_coins():
    """ Return the total calculated from the coins inputted. """
    print("Insert amount of coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# CHECK transaction successful.
def check_transaction(total_coins, drink_cost):
    """ Return true if the payment is accepted, false if not. """
    if total_coins >= drink_cost:
        change = round(total_coins - drink_cost, 2) # Round the change to 2 decimal places.
        print(f"Here is your change: ${change}")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# MAKE COFFEE.
def make_coffee(drink_name, order_ingredients):
    """ Use the ingredients to make the coffee. """
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name} ☕. Enjoy!")


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
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${resources['money']}")
    else:
        drink = MENU[choice]
        if check_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
