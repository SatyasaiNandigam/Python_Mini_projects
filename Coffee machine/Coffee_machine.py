# Make three hot coffee
# 1.Espresso: 50Ml water and 18g coffee
# 2.Latte: 200ml Water and 24g coffee and 150Ml milk
# 3.Cappuccino: 250Ml water and 24g coffee and 100ml Milk

# It starts with 300Ml of water and 200ml of milk and 100g of coffee

# coin operated: 1.penny 2.Nickel 3. Dime 4.Quarter

# program Requirements:
# TODO 1. Report
# TODO 2.Check Resources are sufficient
# TODO.Process coins
# TODO 4.Check transaction is successful
# TODO 5.Make Coffee

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


def report(resources, bank):
    print(f"Water: {resources['water']} Ml")
    print(f"Milk : {resources['milk']} Ml")
    print(f"coffee: {resources['coffee']} gm")
    print(f"money: ${bank}")


def sufficient(MENU, resources, choice, count):
    """ The resources to make this coffee is sufficient or not"""
    for i in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"].get(i) > resources.get(i):
            print(f"Sorry there is not enough {i}")
            flag = 1
            return flag
        else:
            count += 1
    if count == len(MENU[choice]["ingredients"]):
        for i in MENU[choice]["ingredients"]:
            resources[i] = resources.get(i) - MENU[choice]["ingredients"].get(i)


run = True
bank = 0
flag = 0
count = 0

while run:
    print(f"espresso ☕   : $ {MENU['espresso']['cost']}\n"
          f"latte ☕      : $ {MENU['latte']['cost']}\n"
          f"cappuccino ☕ : $ {MENU['cappuccino']['cost']}")
    choice = input("What would you like?(espresso/latte/cappuccino) or to check the report press 'report': ")
    if choice == 'report':
        report(resources, bank)
        option=input("Do you want coffee? type y/n: ")
        if option=='n':
            break

    else:
        flag = sufficient(MENU, resources, choice, count)
        if flag == 1:
            break
        print("*********Enter your money*********")
        quarters = int(input("How many Quarters?")) * 0.25
        dime = int(input("How many dimes?")) * 0.10
        nickel = int(input("How many nickels")) * 0.05
        pennies = int(input("How many pennies?")) * 0.01
        money = quarters + dime + nickel + pennies

        if MENU[choice]["cost"] == money:
            print("Transaction is successful")
            print(f"Your ☕ {choice} is ready")
            bank += MENU[choice]["cost"]
            option = input("Do you want to one more ? y / n: ")
            if option == 'n':
                run = False
        elif MENU[choice]["cost"] < money:
            money_change= money-MENU[choice]["cost"]
            print(f"your change: {round(money_change,2)}")
            print("Transaction is successful")
            print(f"Your ☕ {choice} is ready")
            bank += MENU[choice]["cost"]
            option = input("Do you want to one more ? y / n: ")
            if option == 'n':
                run = False
        else:
            print("Not sufficient money! Transaction is unsuccessful")
            break




