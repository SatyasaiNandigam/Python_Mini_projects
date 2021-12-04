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

# count = 0
#
# for i in MENU["espresso"]["ingredients"]:
#     if MENU["espresso"]["ingredients"].get(i) > resources.get(i):
#         print("Resources are not sufficient")
#         break
#     else:
#         count+=1
#
# if count==len(MENU["espresso"]):
#     for i in MENU["espresso"]["ingredients"]:
#         resources[i] = resources.get(i)-MENU["espresso"]["ingredients"].get(i)

quarters = int(input("How many Quarters?"))*0.25
dime = int(input("How many dimes?"))*0.10
nickel = int(input("How many nickels"))*0.05
pennies = int(input("How many pennies?"))*0.01

print(quarters+dime+nickel+pennies)




