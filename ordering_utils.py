import menu as menu


def check_if_food_valid(food_name: str) -> bool:
    if food_name not in menu.VALID_FOODS:
        return False
    return True


def check_if_drink_valid(drink_name: str) -> bool:
    if drink_name not in menu.VALID_DRINKS:
        if drink_name not in menu.VALID_ALC_DRINKS:
            return False
        return True
    return True


def get_valid_meal_order() -> str:
    while True:
        food = (
            input("What meal would you like to order?(Type one name at the time): ")
            .strip()
            .capitalize()
        )
        if check_if_food_valid(food):
            return food
        else:
            print("Wrong name")
            continue


def get_valid_meal_quantity() -> int:
    while True:
        try:
            quantity = int(input("How many of said meal?(Type a number): ").strip())
            return quantity
        except ValueError:
            print("Input must be an integer")
            continue


def handle_extra_meal_order() -> str:
    while True:
        user_answer = (
            input("Do you want to order anything else from food the menu?(Yes/No): ")
            .strip()
            .lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def handle_drink_orders() -> str:
    while True:
        user_answer = (
            input("Do you want to order any drinks?(Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def get_valid_drink_order() -> str:
    while True:
        drink = (
            input("What drink would you like to order?(Type one name at the time): ")
            .strip()
            .capitalize()
        )
        if check_if_drink_valid(drink):
            return drink
        else:
            print("Wrong name")
            continue


def get_valid_drink_quantity() -> int:
    while True:
        try:
            quantity = int(
                input("And how many of said drink?(Type a number): ").strip()
            )
            return quantity
        except ValueError:
            print("Input must be an integer")
            continue


def handle_extra_drink_order() -> str:
    while True:
        user_answer = (
            input("Do you want to order anything else from drinks menu?(Yes/No): ")
            .strip()
            .lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def handle_order_now() -> str:
    while True:
        user_answer = (
            input("Do you want to make an order right now?(Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def is_ready_to_order() -> str:
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


def handle_call_waiter() -> bool:
    while True:
        user_answer = (
            input("If you need anything else type 'call' without quotes: ")
            .strip()
            .lower()
        )
        if user_answer != "call":
            print("You must type word 'call'!!")
            continue
        else:
            return True


def handle_customer_request() -> str:
    while True:
        user_input = (
            input("How can I help you?(Choose one: paycheck/add/update): ")
            .strip()
            .lower()
        )
        valid_answers = ["paycheck", "add", "update"]
        if user_input not in valid_answers:
            print("Wrong input, please repeat")
            continue
        else:
            return user_input


def handle_tips_request() -> bool:
    while True:
        user_answer = input("Do you want to leave tips?(Type Yes/No): ").strip().lower()
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            break
    if user_answer == "yes":
        return True
    return False


def handle_tip_percentage() -> int:
    while True:
        try:
            user_answer = int(
                input(
                    "What percent you want to add to paycheck?(Must type a whole number): "
                )
            )
            return user_answer
        except ValueError:
            print("Input must be an integer")
            continue


def handle_payment(full_price) -> bool:
    while True:
        try:
            user_input = float(input("Enter amount to pay: ").strip())
            if user_input != full_price:
                print("Are you broke or something?")
            else:
                return True
        except ValueError:
            print("Input must be a number")
            continue


def handle_add_request() -> str:
    while True:
        user_answer = (
            input("What would you like to add? (Choose from drinks/food): ")
            .strip()
            .lower()
        )
        if user_answer != "drinks" and user_answer != "food":
            print("Wrong input! Try again")
            continue
        else:
            return user_answer


def handle_add_drinks() -> bool:
    while True:
        user_answer = (
            input("Do you want to add drinks too?(Type Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            break
    if user_answer == "yes":
        return True
    return False


def handle_add_food() -> bool:
    while True:
        user_answer = (
            input("Do you want to add meals too?(Type Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            break
    if user_answer == "yes":
        return True
    return False


def handle_update_request() -> str:
    while True:
        user_answer = (
            input("What would you like to update? (Choose from drinks/food): ")
            .strip()
            .lower()
        )
        if user_answer != "drinks" and user_answer != "food":
            print("Wrong input! Try again")
            continue
        else:
            return user_answer


def handle_drink_update() -> str:
    while True:
        user_answer = (
            input("What drink would you like to update?(Type one name at the time): ")
            .strip()
            .capitalize()
        )
        if check_if_drink_valid(user_answer):
            return user_answer
        else:
            print("Wrong name")
            continue


def handle_food_update() -> str:
    while True:
        user_answer = (
            input("What meal would you like to update?(Type one name at the time): ")
            .strip()
            .capitalize()
        )
        if check_if_food_valid(user_answer):
            return user_answer
        else:
            print("Wrong name")
            continue


def handle_extra_drink_update() -> str:
    while True:
        user_answer = (
            input("Do you want to update anything else from ordered drinks?(Yes/No): ")
            .strip()
            .lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def handle_extra_food_update() -> str:
    while True:
        user_answer = (
            input("Do you want to update anything else from ordered foods?(Yes/No): ")
            .strip()
            .lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def handle_update_meals() -> bool:
    while True:
        user_answer = (
            input("Do you want to update meals too?(Type Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            break
    if user_answer == "yes":
        return True
    return False


def handle_update_drinks() -> bool:
    while True:
        user_answer = (
            input("Do you want to update drinks too?(Type Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            break
    if user_answer == "yes":
        return True
    return False
