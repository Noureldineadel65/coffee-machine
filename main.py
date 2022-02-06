import data

current_ingredients = {
    "water": {
        "value": 500,
        "prefix": "ml"
    },
    "milk": {
        "value": 500,
        "prefix": "ml"
    },
    "coffee": {
        "value": 500,
        "prefix": "g"
    }
}
money_in_machine = 0


def display_report():
    for key in current_ingredients:
        print(f"{key.title()}: {current_ingredients[key]['value']}{current_ingredients[key]['prefix']}")
    print(f"Money: ${money_in_machine}")


def check_ingredients(order):
    for key in order["ingredients"]:
        if order["ingredients"][key] > current_ingredients[key]["value"]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def give_change(total_money, cost):
    # give change in pennies, dimes, nickels, and quarters
    if total_money - cost > cost:
        print(f"Here is ${round(total_money - cost, 2)} in change.")


def get_money(cost):
    global money_in_machine
    coins = {}
    money_inserted = {
        "quarter": int(input("How many quarters?: ")),
        "dime": int(input("How many dimes?: ")),
        "nickel": int(input("How many nickels?: ")),
        "penny": int(input("How many pennies?: "))

    }
    total_money = 0
    for key in money_inserted:
        total_money += money_inserted[key] * data.COINS[key]
    if cost > total_money:
        print("That's not enough money. Money Refunded.")
        return False
    money_in_machine += cost
    give_change(total_money, cost)
    return True


def process_order(chosen_item, choice):
    for key in chosen_item["ingredients"]:
        current_ingredients[key]["value"] -= chosen_item["ingredients"][key]
    print(f"Here is your {choice} ☕ Enjoy!")


print('''
                        (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /;                             ;
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
  jgs \""--..__                              __..--""/
       '._     """----.....______.....----"""     _.'
          `""--..,,_____            _____,,..--""`
                        `"""----"""`
''')
print("Welcome to Nour's Coffee Machine!")
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        display_report()
    else:
        chosen_item = data.MENU[choice]
        if check_ingredients(chosen_item) and get_money(chosen_item["cost"]):
            process_order(chosen_item, choice)
