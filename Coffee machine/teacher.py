MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def if_resources_sufficient(order_ingredients):
    """Returns true when the order is made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from the inserted coins"""
    print("insert coins here")
    total = int(input("How many Quarters?"))*0.25
    total += int(input("How many Dimes?")) * 0.10
    total += int(input("How many Nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    """Return true when the payment is accepted, False if money is insufficient"""
    if money_recieved >= drink['cost']:
        change= round(money_recieved-drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the ingredients form the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy")

is_on = True
profit= 0

while is_on:
    choice= input("What would you like?(espresso/latte/cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"water : {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}gm")
        print(f"money : $ {profit}")
    else:
        drink = MENU[choice]
        if if_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])


