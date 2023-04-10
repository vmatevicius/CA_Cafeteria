from classes import Menu, Tables, Order, Orders
import helpers as h
from datetime import datetime
import menu as m

menu = Menu()
orders = Orders()

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
    print("Here is our menu:")
    menu.show_menus()
    foods = {}
    while True:
        food = (
            input("So what meal would you like to order?(Type one name at the time): ")
            .strip()
            .capitalize()
        )
        if h.check_if_food_valid(food):
            break
        else:
            continue
    while True:
        try:
            quantity = int(input("And how many of said meal?(Type a number): ").strip())
            break
        except ValueError:
            print("Input must be an integer")
            continue
    foods[food] = quantity

    while True:
        user_answer = (
            input("Do you want to order any drinks?(Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            break
    if h.identify_input(user_answer):
        pass
    else:
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
            continue
        else:
            break
