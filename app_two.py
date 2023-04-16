from classes import Menu, Tables, Order, Orders
import helpers as h
from datetime import datetime
import menu as m

menu = Menu()
orders = Orders()

temp_name = "Antanas"
temp_surname = "Fontanas"
while True:
    user_answer = (
        input("Do you want to make an order right now?(Yes/No): ").strip().lower()
    )
    if user_answer != "yes" and user_answer != "no":
        print("You must type yes or no")
        continue
    else:
        break

if h.identify_input(user_answer):
    print("Here is our food menu:")
    menu.show_food_menu()
    foods = {}
    while True:
        while True:
            food = (
                input(
                    "So what meal would you like to order?(Type one name at the time): "
                )
                .strip()
                .capitalize()
            )
            if h.check_if_food_valid(food):
                break
            else:
                continue
        while True:
            try:
                quantity = int(
                    input("And how many of said meal?(Type a number): ").strip()
                )
                foods[food] = quantity
                break
            except ValueError:
                print("Input must be an integer")
                continue

        while True:
            user_answer = (
                input("Do you want to order anything else from food menu?(Yes/No): ")
                .strip()
                .lower()
            )
            if user_answer != "yes" and user_answer != "no":
                print("You must type yes or no")
                continue
            else:
                break
        if user_answer == "no":
            break
        else:
            continue

    while True:
        user_answer = (
            input("Do you want to order any drinks?(Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
        else:
            break
    if h.identify_input(user_answer):
        print("Here is our drinks menu: ")
        menu.show_all_drinks()
        alcohol = {}
        alc_free = {}
        while True:
            while True:
                drink = (
                    input(
                        "So what drink would you like to order?(Type one name at the time): "
                    )
                    .strip()
                    .capitalize()
                )
                if h.check_if_drink_valid(drink):
                    break
                else:
                    continue
            while True:
                try:
                    quantity = int(
                        input("And how many of said drink?(Type a number): ").strip()
                    )
                    if drink in m.VALID_ALC_DRINKS:
                        alcohol[drink] = quantity
                    else:
                        alc_free[drink] = quantity
                    break
                except ValueError:
                    print("Input must be an integer")
                    continue

            while True:
                user_answer = (
                    input(
                        "Do you want to order anything else from drinks menu?(Yes/No): "
                    )
                    .strip()
                    .lower()
                )
                if user_answer != "yes" and user_answer != "no":
                    print("You must type yes or no")
                    continue
                else:
                    break
            if user_answer == "no":
                break
            else:
                continue
        if alcohol:
            pass
        else:
            alcohol = None
        if alc_free:
            pass
        else:
            alc_free = None

        orders.make_order(
            name=temp_name,
            surname=temp_surname,
            foods=foods,
            alcohol=alcohol,
            alcohol_free=alc_free,
        )

        orders.show_order_summarized(name=temp_name, surname=temp_surname)
    else:
        print("Not implemented yet")
        # add the order
        # show summarized order without any drinks
        # find out how to do everything without copy pasting
        # implement this!
        pass
else:
    while True:
        user_answer = (
            input("Tell us when you will be ready to order(Type: ready): ")
            .strip()
            .lower()
        )
        if user_answer != "ready":
            print("You must type word 'ready' when you are ready to order")
        else:
            break
    print("Not implemented yet")
    # find out how to do same things without copy pasting
    # implement this!
