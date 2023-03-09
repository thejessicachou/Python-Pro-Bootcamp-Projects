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


def make_coffee():
    """Deduct coffee order resources from total remaining resources"""
    resources['water'] -= order_water
    resources['milk'] -= order_milk
    resources['coffee'] -= order_coffee
    print(f"Here is your {order_name}. Enjoy!")


def payment():
    """Determine how much has been paid and if change is due."""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_payment = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)

    if total_payment < order_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif total_payment > order_cost:
        change_due = "{:.2f}".format(round((total_payment - order_cost), 2))
        print(f"Here is ${change_due} in change.")
        make_coffee()
    else:
        make_coffee()


def check_resources():
    """Check that there are enough resources to complete the order"""
    current_water = resources["water"]
    current_milk = resources["milk"]
    current_coffee = resources["coffee"]
    remaining_water = current_water - order_water
    remaining_milk = current_milk - order_milk
    remaining_coffee = current_coffee - order_coffee

    if remaining_water < 0:
        print("Sorry, there is not enough water.")
    elif remaining_coffee < 0:
        print("Sorry, there is not enough coffee.")
    elif remaining_milk < 0:
        print("Sorry, there is not enough milk.")
    else:
        payment()


machine_on = True


while machine_on:
    #Prompt user for order
    order_name = input("What would you like to order? (espresso/latte/cappuccino): ").lower()

    if order_name == "report":
        print(resources)
    elif order_name == "off":
        machine_on = False
    else:
        order = MENU.get(order_name)
        order_cost = float(order["cost"])
        order_water = int(order["ingredients"]["water"])
        # get milk if present or 0 value if not
        order_milk = int(order["ingredients"].get("milk", 0))
        order_coffee = int(order["ingredients"]["coffee"])
        check_resources()
