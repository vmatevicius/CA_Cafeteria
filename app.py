from menu_class import Menu
from orders_classes import Order, Orders
from tables_class import Reservation, Tables
import helpers as helpers
from datetime import datetime
import menu as menu_dicts
import reservation_utils as res_utils
import ordering_utils as ord_utils

menu = Menu()
tables = Tables()
orders = Orders()

current_time = datetime.now().strftime("%H:%M")

print("Welcome to our cafetera!")
user_answer = res_utils.is_reservation_made()

if helpers.identify_input(user_answer):
    print(
        "We are sorry, but we have no reservations yet, there must have been an error"
    )
    user_answer = res_utils.handle_new_reservation()
    if helpers.identify_input(user_answer):
        print("Here are our free tables at the moment:")
        print("Choose the table you want from the free tables list:")
        tables.show_free_tables()
        print("We will need some information to make a new reservation")
        (
            name,
            surname,
            table_type,
            table_id,
            time,
        ) = res_utils.get_reservation_info()
        tables.reserve_table(
            name=name,
            surname=surname,
            table_type=table_type,
            table_id=table_id,
            time=time,
        )
        print(tables.show_reservation(name=name, surname=surname))
    else:
        print("Have a nice day then!")

else:
    user_answer = res_utils.handle_new_reservation()
    if helpers.identify_input(user_answer):
        print("Here are our free tables at the moment:")
        print("Choose the table you want from the free tables list:")
        tables.show_free_tables()
        print("We will need some information to make a new reservation")
        (
            name,
            surname,
            table_type,
            table_id,
            time,
        ) = res_utils.get_reservation_info()
        tables.reserve_table(
            name=name,
            surname=surname,
            table_type=table_type,
            table_id=table_id,
            time=time,
        )
        print(tables.show_reservation(name=name, surname=surname))

    else:
        print("Have a nice day then!")


user_answer = ord_utils.handle_order_now()

if helpers.identify_input(user_answer):
    print("Here is our food menu:")
    menu.show_food_menu()
    foods = {}
    while True:
        food = ord_utils.get_valid_meal_order()
        quantity = ord_utils.get_valid_meal_quantity()
        if food in foods.keys():
            foods[food] += quantity
        else:
            foods[food] = quantity
        user_answer = ord_utils.handle_extra_meal_order()
        if user_answer == "no":
            break
        else:
            continue

    user_input = ord_utils.handle_drink_orders()
    if helpers.identify_input(user_input):
        print("Here is our drinks menu: ")
        menu.show_all_drinks()
        alcohol = {}
        alc_free = {}
        while True:
            drink = ord_utils.get_valid_drink_order()
            quantity = ord_utils.get_valid_drink_quantity()
            if drink in menu_dicts.VALID_ALC_DRINKS:
                if drink in alcohol.keys():
                    alcohol[drink] += quantity
                else:
                    alcohol[drink] = quantity
            else:
                if drink in alc_free.keys():
                    alc_free[drink] += quantity
                else:
                    alc_free[drink] = quantity

            user_answer = ord_utils.handle_extra_drink_order()
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
            name=name,
            surname=surname,
            foods=foods,
            alcohol=alcohol,
            alcohol_free=alc_free,
        )
        orders.show_order_summarized(name=name, surname=surname)
    else:
        orders.make_order(name=name, surname=surname, foods=foods)
        orders.show_order_summarized(name=name, surname=surname)
else:
    ord_utils.is_ready_to_order()
    print("Here is our food menu:")
    menu.show_food_menu()
    foods = {}
    while True:
        food = ord_utils.get_valid_meal_order()
        quantity = ord_utils.get_valid_meal_quantity()
        if food in foods.keys():
            foods[food] += quantity
        else:
            foods[food] = quantity
        user_answer = ord_utils.handle_extra_meal_order()
        if user_answer == "no":
            break
        else:
            continue

    user_input = ord_utils.handle_drink_orders()
    if helpers.identify_input(user_input):
        print("Here is our drinks menu: ")
        menu.show_all_drinks()
        alcohol = {}
        alc_free = {}
        while True:
            drink = ord_utils.get_valid_drink_order()
            quantity = ord_utils.get_valid_drink_quantity()
            if drink in menu_dicts.VALID_ALC_DRINKS:
                if drink in alcohol.keys():
                    alcohol[drink] += quantity
                else:
                    alcohol[drink] = quantity
            else:
                if drink in alc_free.keys():
                    alc_free[drink] += quantity
                else:
                    alc_free[drink] = quantity

            user_answer = ord_utils.handle_extra_drink_order()
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
            name=name,
            surname=surname,
            foods=foods,
            alcohol=alcohol,
            alcohol_free=alc_free,
        )

        orders.show_order_summarized(name=name, surname=surname)
    else:
        alcohol = None
        alc_free = None
        orders.make_order(
            name=name,
            surname=surname,
            foods=foods,
            alcohol=alcohol,
            alcohol_free=alc_free,
        )
        orders.show_order_summarized(name=name, surname=surname)

user_answer = ord_utils.handle_call_waiter()

if user_answer:
    user_request = ord_utils.handle_customer_request()
    if user_request == "paycheck":
        # ADD RECEIPT LOGGING
        # ADD RECEIPT LOGGING
        # ADD RECEIPT LOGGING
        # ADD RECEIPT LOGGING
        if ord_utils.handle_tips_request():
            tip_percentage = ord_utils.handle_tip_percentage()
            order_cost = orders.get_order_cost(name=name, surname=surname)
            full_cost = order_cost / 100 * tip_percentage + order_cost
            print(f"The full cost of your order is {full_cost}")
            if ord_utils.handle_payment(full_cost):
                print("Thank you, have a nice day!")
        else:
            order_cost = orders.get_order_cost(name=name, surname=surname)
            print(f"The full cost of your order is {order_cost}")
            if ord_utils.handle_payment(order_cost):
                print("Thank you, have a nice day!")
    elif user_request == "add":
        user_input = ord_utils.handle_add_request()
        if user_input == "food":
            print("Here is our food menu:")
            menu.show_food_menu()
            foods = {}
            while True:
                food = ord_utils.get_valid_meal_order()
                quantity = ord_utils.get_valid_meal_quantity()
                if food in foods.keys():
                    foods[food] += quantity
                else:
                    foods[food] = quantity
                user_answer = ord_utils.handle_extra_meal_order()
                if user_answer == "no":
                    break
                else:
                    continue
            orders.add_to_order(name=name, surname=surname, foods=foods)
            orders.show_order_summarized(name=name, surname=surname)
        else:
            print("Here is our drinks menu: ")
            menu.show_all_drinks()
            alcohol = {}
            alc_free = {}
            while True:
                drink = ord_utils.get_valid_drink_order()
                quantity = ord_utils.get_valid_drink_quantity()
                if drink in menu_dicts.VALID_ALC_DRINKS:
                    if drink in alcohol.keys():
                        alcohol[drink] += quantity
                    else:
                        alcohol[drink] = quantity
                else:
                    if drink in alc_free.keys():
                        alc_free[drink] += quantity
                    else:
                        alc_free[drink] = quantity

                user_answer = ord_utils.handle_extra_drink_order()
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

            orders.add_to_order(
                name=name, surname=surname, alcohol=alcohol, alcohol_free=alc_free
            )
            orders.show_order_summarized(name=name, surname=surname)
    elif user_answer == "update":
        pass
        # implement this
