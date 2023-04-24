# Coffee machine Program
# Day 15

import os
import drinks as dr


def refill(resource):

    global water, milk, coffee

    # refill all resources
    if resource.lower() == "all":
        water = 300
        milk = 200
        coffee = 100
    # refill water
    elif resource.lower() == "water":
        water = 300
    # refill milk
    elif resource.lower() == "milk":
        milk = 200
    # refill coffee
    elif resource.lower() == "coffee":
        coffee = 100
    # bad input
    else:
        print("Invalid resource.")


def print_menu():

    os.system('cls')
    print("Welcome to the Coffee Station!")
    print("Please make a choice from the following beverages: ")
    print("\nEspresso (1)\nLatte (2)\nCappuccino (3)\n")


def print_resources():

    global water, milk, coffee, money

    print("\n*******************************************")
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money:.2f}")


def get_user_choice(choice):

    if choice.lower() == "espresso" or choice == "1":
        return "espresso"
    elif choice.lower() == "latte" or choice == "2":
        return "latte"
    elif choice.lower() == "cappuccino" or choice == "3":
        return "cappuccino"
    elif choice.lower() == "off":
        return "off"
    elif choice.lower() == "report":
        print_resources()
        return "bad"
    elif choice.lower() == "refill":
        refill(input("What resource do you want to refill? "))
        return "bad"
    else:
        return "bad"


def check_resources(drink):

    global water, milk, coffee

    if dr.options[drink]["ingredients"]["water"] <= water:
        if dr.options[drink]["ingredients"]["milk"] <= milk:
            if dr.options[drink]["ingredients"]["coffee"] <= coffee:
                return True

    return False


def get_user_money(drink):

    print(f"The cost of the {drink} is ${dr.options[drink]['cost']:.2f}.")
    print("Enter the amount of each coin you'd like to enter: ")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    return (quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)


def calculate_change(coin_value, drink):

    if coin_value < dr.options[drink]["cost"]:
        return -1
    else:
        return coin_value - dr.options[drink]["cost"]


def use_resources(drink):

    global water, milk, coffee, money

    water -= dr.options[drink]["ingredients"]["water"]
    milk -= dr.options[drink]["ingredients"]["milk"]
    coffee -= dr.options[drink]["ingredients"]["coffee"]
    money += dr.options[drink]["cost"]


machineOn = True
money = 0
water = 300
milk = 200
coffee = 100

while machineOn:

    print_menu()

    # get user input, if it's bad, send back to main menu
    user_choice = get_user_choice(input("Choice: "))
    if user_choice == "bad":
        continue
    # turn machine off / exit program
    elif user_choice == "off":
        machineOn = False
        continue

    # check if required resources are available, if not, back to the main menu
    enough_resources = check_resources(user_choice)
    if not enough_resources:
        print("Not enough resources to make that drink, please refill.")
        input("Press Enter to continue...")
        continue

    # get coins and calculate total
    user_money = get_user_money(user_choice)
    # check if enough money is offered and return change
    # if not enough money, back to main menu
    enough_money = calculate_change(user_money, user_choice)
    if enough_money == -1:
        print("You did not provide enough money.")
        input("Press Enter to continue...")
        continue

    # Give coffee and subtract resources that were used
    print(f"\nHere is your {user_choice} and your change is ${enough_money:.2f}.  Enjoy and have a great day!")
    use_resources(user_choice)
