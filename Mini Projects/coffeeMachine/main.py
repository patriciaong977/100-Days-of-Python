""" Import menuResources.py for MENU and resources."""
from menuResources import MENU, resources, Money, displayReport
import menuResources

def checkResources(drinkOfChoice):
    """Check if there are enough resources to make the drink of choice."""
    for item in drinkOfChoice:
        if drinkOfChoice[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def processCoins():
    """Calculate total = coins inserted - cost of drink."""
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transactionSuccess(totalCoins, drinkCost):
    """Check if the transaction was successful.
    True if successful, false if not and return change."""
    if totalCoins >= drinkCost:
        returnChange = round(totalCoins - drinkCost, 2)
        print(f"Here is ${returnChange} in change.")
        menuResources.Money += drinkCost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drinkName, drinkIngredients):
    """Subtract ingredients from resources."""
    for item in drinkIngredients:
        resources[item] -= drinkIngredients[item]
    print(f"Here is your {drinkName} ☕️. Enjoy!")

""" While program is on, ask user what they would like to do."""
IS_ON = True  # Controls the program if it is on or off.

while IS_ON:
    ask_user = input("What would you like? (espresso/latte/cappuccino): ")

    if ask_user == "off":
        IS_ON = False
    elif ask_user == "report":
        displayReport()
    else:
        drink = MENU[ask_user]
        if checkResources(drink["ingredients"]):
            total_coins = processCoins()
            if transactionSuccess(total_coins, drink["cost"]):
                make_coffee(ask_user, drink["ingredients"])
