from typing import Union, Dict, Optional, List
import menu as menu_dict
import tables as table_dict
import helpers as helpers
from datetime import datetime


class Menu:
    current_time = int(datetime.now().strftime("%H"))

    def __init__(self) -> None:
        self.alcohol = menu_dict.DRINKS["Alcohol"]
        self.alcohol_free = menu_dict.DRINKS["Alcohol free"]
        self.breakfast = menu_dict.BREAKFAST
        self.lunch = menu_dict.LUNCH
        self.dinner = menu_dict.DINNER
        self.vegan = menu_dict.SPECIAL_MENU["Vegan"]
        self.vegetarian = menu_dict.SPECIAL_MENU["Vegetarian"]

    def show_food_menu(self) -> Dict[str, Union[float, int]]:
        helpers.print_menu(submenu_name=self.vegetarian)
        helpers.print_menu(submenu_name=self.vegan)

        if 12 < self.current_time < 18:
            helpers.print_menu(submenu_name=self.lunch)
        if 12 > self.current_time:
            helpers.print_menu(submenu_name=self.breakfast)
        if 18 < self.current_time:
            helpers.print_menu(submenu_name=self.dinner)

    def show_all_drinks(self) -> Dict[str, Union[float, int]]:
        helpers.print_menu(submenu_name=self.alcohol)
        helpers.print_menu(submenu_name=self.alcohol_free)

    def get_menu(self) -> Dict[str, Dict[str, Dict[str, Union[int, float, str]]]]:
        if 12 < self.current_time < 18:
            return dict(
                self.alcohol,
                **self.alcohol_free,
                **self.vegan,
                **self.vegetarian,
                **self.lunch,
            )
        if 12 > self.current_time:
            return dict(
                self.alcohol,
                **self.alcohol_free,
                **self.vegan,
                **self.vegetarian,
                **self.breakfast,
            )
        if 18 < self.current_time:
            return dict(
                self.alcohol,
                **self.alcohol_free,
                **self.vegan,
                **self.vegetarian,
                **self.dinner,
            )


class Reservation:
    def __init__(
        self, name: str, surname: str, time: str, table_type: str, table_id: int
    ) -> None:
        self.name = name
        self.surname = surname
        self.time = time
        self.table_type = table_type
        self.table_id = table_id


class Tables:
    def __init__(self) -> None:
        self.tables = {
            "single": table_dict.SINGLE_TABLES,
            "double": table_dict.DOUBLE_TABLES,
            "family": table_dict.FAMILY_TABLES,
        }
        self.table_reservations: List[Reservation] = []

    def check_reservation(self, name: str, surname: str) -> bool:
        if self.table_reservations == None:
            return False
        for reservation in self.table_reservations:
            if reservation.name == name and reservation.surname == surname:
                return True

    def check_if_table_free(self, table_type: str, table_id: int) -> bool:
        if self.tables[table_type][table_id] == "free":
            return True
        return False

    def reserve_table(
        self, name: str, surname: str, time: str, table_type: str, table_id: int
    ) -> Optional[str]:
        if self.check_if_table_free(table_type=table_type, table_id=table_id):
            reservation = Reservation(
                name=name,
                surname=surname,
                time=time,
                table_type=table_type,
                table_id=table_id,
            )
            self.table_reservations.append(reservation)
            self.tables[table_type][table_id] = "reserved"
        else:
            return f"Table is already reserved"

    def show_free_tables(self) -> None:
        for key, value in self.tables.items():
            for table_id, table_state in value.items():
                if table_state == "free":
                    print(f"{key}: {table_id} is {table_state}")

    def show_reserved_tables(self) -> str:
        for key, value in self.tables.items():
            for table_id, table_state in value.items():
                if table_state == "reserved":
                    print(f"{key}: {table_id} is {table_state}")

    def show_reservation(self, name: str, surname: str) -> str:
        if self.table_reservations == None:
            return f"We are sorry, reservation was not found"
        for reservation in self.table_reservations:
            if reservation.name == name and reservation.surname == surname:
                return f"{name} {surname} reserved a {reservation.table_type} type table for {reservation.time} o'clock"
            else:
                return f"We are sorry, reservation was not found"


class Order:
    def __init__(
        self,
        name: str,
        surname: str,
        foods: Dict[str, int],
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
        total_cost: Union[int, float] = 0,
        prep_time: int = 0,
    ) -> None:
        self.name = name
        self.surname = surname
        self.foods = foods
        self.alcohol = alcohol
        self.alcohol_free = alcohol_free
        self.total_cost = total_cost
        self.prep_time = prep_time


class Orders:
    def __init__(self) -> None:
        self.orders: List[Orders] = []

    def make_order(
        self,
        name: str,
        surname: str,
        foods: Dict[str, int],
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
    ) -> None:
        if alcohol != None and alcohol_free != None:
            self.orders.append(Order(name, surname, foods, alcohol, alcohol_free))
        if alcohol != None and alcohol_free == None:
            self.orders.append(Order(name, surname, foods, alcohol))
        if alcohol_free != None and alcohol == None:
            self.orders.append(Order(name, surname, foods, alcohol_free))

    def update_order_quantities(
        self,
        name: str,
        surname: str,
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
        foods: Dict[str, int] = None,
    ) -> None:
        if helpers.is_value_not_none(alcohol):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    order.alcohol.update(alcohol)
        if helpers.is_value_not_none(alcohol_free):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    order.alcohol_free.update(alcohol_free)
        if helpers.is_value_not_none(foods):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    order.foods.update(foods)

    def remove_from_order(self, name: str, surname: str, item_to_remove: str) -> None:
        for order in self.orders:
            if order.name == name and order.surname == surname:
                if item_to_remove in menu_dict.VALID_DRINKS:
                    del order.alcohol_free[item_to_remove]
                    return
                if item_to_remove in menu_dict.VALID_FOODS:
                    del order.foods[item_to_remove]
                    return
                if item_to_remove in menu_dict.VALID_ALC_DRINKS:
                    del order.alcohol[item_to_remove]
                    return
                else:
                    print("Customer has not ordered such thing")

    def add_to_order(
        self,
        name: str,
        surname: str,
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
        foods: Dict[str, int] = None,
    ) -> None:
        if helpers.is_value_not_none(alcohol):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    for key, value in alcohol.items():
                        if order.alcohol == None:
                            order.alcohol = {}
                            order.alcohol[key] = value
                        else:
                            order.alcohol[key] = value
                else:
                    continue
        if helpers.is_value_not_none(alcohol_free):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    for key, value in alcohol_free.items():
                        if order.alcohol_free == None:
                            order.alcohol_free = {}
                            order.alcohol_free[key] = value
                        else:
                            order.alcohol_free[key] = value
                else:
                    continue
        if helpers.is_value_not_none(foods):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    for key, value in foods.items():
                        order.foods[key] = value
                else:
                    continue

    def calculate_order_cost(self, name: str, surname: str) -> None:
        full_menu = dict(
            menu_dict.VALID_ALC_DRINKS,
            **menu_dict.VALID_DRINKS,
            **menu_dict.VALID_FOODS,
        )
        for order in self.orders:
            if order.name == name and order.surname == surname:
                if order.alcohol == None:
                    full_order = dict(order.foods, **order.alcohol_free)
                if order.alcohol_free == None:
                    full_order = dict(order.foods, **order.alcohol)
                if order.alcohol_free and order.alcohol == None:
                    full_order = dict(order.foods)
                for key in full_order.keys():
                    order.total_cost += full_menu[key] * full_order[key]

    def show_order_summarized(self, name: str, surname: str) -> None:
        for order in self.orders:
            if order.name == name and order.surname == surname:
                if order.alcohol == None:
                    full_order = dict(order.foods, **order.alcohol_free)
                if order.alcohol_free == None:
                    full_order = dict(order.foods, **order.alcohol)
                if order.alcohol_free and order.alcohol == None:
                    full_order = dict(order.foods)
                self.calculate_order_cost(name, surname)
                self.calculate_prep_time(name, surname)
                print(f"Total cost is {self.get_order_cost(name, surname)} dollars")
                print("Your order is :")
                for key, value in full_order.items():
                    print(f"{key}, quantity: {value}")
                print(f"Total preparation time will be around {order.prep_time} mins")

    def get_order_cost(self, name: str, surname: str) -> Union[int, float]:
        for order in self.orders:
            if order.name == name and order.surname == surname:
                return order.total_cost

    def calculate_prep_time(self, name: str, surname: str) -> None:
        menu = Menu().get_menu()
        for order in self.orders:
            if order.name == name and order.surname == surname:
                for key, value in order.foods.items():
                    order.prep_time += (
                        int(menu[key]["prep.time"].replace("min", "")) * value
                    )
                if order.alcohol == None:
                    pass
                else:
                    for key, value in order.alcohol.items():
                        order.prep_time += (
                            int(menu[key]["prep.time"].replace("min", "")) * value
                        )
                if order.alcohol_free == None:
                    pass
                else:
                    for key, value in order.alcohol_free.items():
                        order.prep_time += (
                            int(menu[key]["prep.time"].replace("min", "")) * value
                        )


# class Payment:
#     def __init__(self) -> None:
#         pass

#     def add_tips(self) -> float:
#         pass
