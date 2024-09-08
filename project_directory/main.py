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
money = 0


def report(user_choice):
    print(f"Water: {resources['water']} ml.")
    print(f"Milk: {resources['milk']} ml.")
    print(f"Coffee: {resources['coffee']} g.")


def money_calculation():
    quarter_price = 0.25
    dime_price = 0.10
    nickle_price = 0.05
    pennies_price = 0.01
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money = quarters * quarter_price + dimes * dime_price + nickles * nickle_price + pennies * pennies_price
    return money


final_money_result = 0


def money_deduction(user_choice, rounded_money):
    if user_choice == "espresso":
        if rounded_money >= 1.5:
            rounded_money -= 1.5
            final_money_result = round(rounded_money, 2)
            return final_money_result
    elif user_choice == "latte":
        if rounded_money >= 2.5:
            rounded_money -= 2.5
            final_money_result = round(rounded_money, 2)
            return final_money_result
    elif user_choice == "cappuccino":
        if rounded_money >= 3.0:
            rounded_money -= 3.0
            final_money_result = round(rounded_money, 2)
            return final_money_result
    else:
        return 0


def coffee_calculation(final_money_result, rounded_money, user_choice):
    if user_choice == "espresso" or final_money_result == MENU["espresso"]["cost"]:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        print(f"Here is your {user_choice} ☕ Enjoy!")
        print(f"Here is ${final_money_result} in change.")
    elif user_choice == "latte" or final_money_result == MENU["latte"]["cost"]:
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        print(f"Here is your {user_choice} ☕ Enjoy!")
        print(f"Here is ${final_money_result} in change.")
    elif user_choice == "cappuccino" or final_money_result == MENU["cappuccino"]["cost"]:
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        print(f"Here is your {user_choice} ☕ Enjoy!")
        print(f"Here is ${final_money_result} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")


def coffee():
    machine_continue = True
    while machine_continue:
        user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()
        if user_choice != "off" and user_choice != "report":
            final_money = money_calculation()
            rounded_money = round(final_money, 2)
            final_money_result = money_deduction(user_choice, rounded_money)
            print(f"Total Money: {rounded_money}")
            coffee_calculation(final_money_result, rounded_money, user_choice)
        elif user_choice == "report":
            report(user_choice)
        else:
            machine_continue = False


coffee()
