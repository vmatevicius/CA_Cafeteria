import json


def greet_customer():
    return f"Welcome to our cafeteria!"


def identify_input(user_input: str) -> bool:
    if user_input == "yes":
        return True
    if user_input == "no":
        return False


def get_valid_table_id() -> int:
    while True:
        try:
            table_id = int(input("And the id of the table type?: ").strip())
            return table_id
        except ValueError:
            print("You must enter a single number")
            continue


def get_valid_table_type() -> str:
    while True:
        valid_table_types = ["single", "double", "family"]
        table_type = (
            input("What table would you like to reserve?(single,double,family): ")
            .strip()
            .lower()
        )
        if table_type not in valid_table_types:
            print("This table type does not exist! Choose a valid one")
            continue
        else:
            return table_type


def get_valid_time() -> str:
    while True:
        time = input("At what time would you like to reserve?(format hh:mm): ").strip()
        if ":" not in time:
            print("Wrong time format! Must be hh:mm")
            continue
        else:
            return time


def print_menu(submenu_name: str) -> str:
    print(
        f'{json.dumps(submenu_name, indent=2).replace("{", "").replace("}", "").strip()}'
    )
