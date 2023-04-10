import json
from typing import List
import menu as m


# app helpers:
def check_if_food_valid(food_name: str):
    if food_name not in m.VALID_FOODS:
        return False
    return True


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
            print("You must enter valid number")
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


# class helpers:
def print_menu(submenu_name: str) -> str:
    print(
        f'{json.dumps(submenu_name, indent=2).replace("{", "").replace("}", "").strip()}'
    )


def is_value_not_none(variable_name) -> bool:
    if variable_name == None:
        return False
    return True
