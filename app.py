from classes import Menu, Tables, Order, Orders
import helpers as h
from datetime import datetime

menu = Menu()
tables = Tables()

current_time = datetime.now().strftime("%H:%M")

print("Welcome to our cafetera!")
while True:
    user_answer = input("Have you made a reservation?(Yes/No): ").strip().lower()
    if user_answer != "yes" and user_answer != "no":
        print("You must type yes or no")
        continue
    else:
        break

if h.identify_input(user_answer):
    print(
        "We are sorry, but we have no reservations yet, there must have been an error"
    )
    while True:
        user_answer = (
            input("Do you want to make a new reservation?(Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            break
    if h.identify_input(user_answer):
        print("Here are our free tables:")
        tables.show_free_tables()
        print("We will need some information to make a new reservation")
        name = input("Please tell us your name: ").strip()
        surname = input("And surname: ").strip()
        table_type = h.get_valid_table_type()
        table_id = h.get_valid_table_id()
        # this part needs work
        time = h.get_valid_time()
        # this part needs work
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
    while True:
        user_answer = (
            input("Do you want to make a reservation?(Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            break
    if h.identify_input(user_answer):
        while True:
            user_answer = input("Are you going to eat now?(Yes/No): ").strip().lower()
            if user_answer != "yes" and user_answer != "no":
                print("You must type yes or no")
                continue
            else:
                break
        if h.identify_input(user_answer):
            print("Choose the table you want from the free tables list")
            print("Here are our free tables at the moment:")
            tables.show_free_tables()
            name = input("Tell us your name: ").strip()
            surname = input("And surname: ").strip()
            table_type = h.get_valid_table_type()
            table_id = h.get_valid_table_id()
            time = current_time
            tables.reserve_table(
                name=name,
                surname=surname,
                table_type=table_type,
                table_id=table_id,
                time=time,
            )
            print(tables.show_reservation(name=name, surname=surname))
        else:
            print("Choose the table you want from the free tables list")
            print("Here are our free tables at the moment:")
            tables.show_free_tables()
            name = input("Tell us your name: ").strip()
            surname = input("And surname: ").strip()
            table_type = h.get_valid_table_type()
            table_id = h.get_valid_table_id()
            time = h.get_valid_time()
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
