"""
This module contains class definitions and implementations,
for Computer, Shop and ReBuy
"""

from typing import Union, Dict, Optional
from dataclasses import dataclass


@dataclass
class Computer:
    """Dataclass containing Computer information"""
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    os: str
    made_in_year: int
    price: int


class Shop:
    """
    Represents a Shop object and
    handles its buy, sell and update inventory functionalities
    Attributes:
        shop_inventory (dict): Dictionary that represents the shops inventory
    """

    def __init__(self) -> None:
        self.shop_inventory: Dict[int, Dict[str, Union[str, int, bool]]] = {}

    def buy(self, computer: Computer) -> None:
        """
        Method to buy and store a computer.
        It takes the Computer object and converts its information to a dict
        and stores it in the lowest inventory slot
        :param computer: Computer object
        """
        item_id = len(self.shop_inventory) + 1
        self.shop_inventory[item_id] = {
            'description': computer.description,
            'processor_type': computer.processor_type,
            'hard_drive_capacity': computer.hard_drive_capacity,
            'memory': computer.memory,
            'os': computer.os,
            'made_in_year': computer.made_in_year,
            'price': computer.price,
        }

    def update_price(self, item_id: int, new_price: int) -> None:
        """
        Update the price for a computer at a certain id
        :param item_id: int
        :param new_price: int
        """
        if item_id in self.shop_inventory:
            self.shop_inventory[item_id]['price'] = new_price
        else:
            print('Cannot update price for an item that does not exist')

    def sell(self, item_id: int) -> None:
        """
        Sells a computer from its inventory id
        :param item_id: int
        """
        del self.shop_inventory[item_id]

    def print_item(self, item_id: int) -> None:
        """
        Print function based on id
        :param item_id: int
        """
        if item_id in self.shop_inventory:
            print(f'Item with id {item_id} : {self.shop_inventory[item_id]}')
        else:
            print(f'Item with id {item_id} does not exist')


class ReBuy(Shop):
    """
    Represents a ReBuy Shop object,
    that inherent the Shop class attributes and methods,
    and buys and refurbishes computers
    """

    def __init__(self):
        super().__init__()

    def refurbish(self, item_id: int, new_os: Optional[str] = None) -> None:
        """
        Takes a computer and updates it information, when it is re-bought
        :param item_id: int
        :param new_os: Optional[str], if a new os is installed
        """
        if item_id in self.shop_inventory:
            comp = self.shop_inventory[item_id]
            year = int(comp['made_in_year'])

            match year:
                case year if year < 2000:
                    comp['price'] = 0
                case year if year < 2010:
                    comp['price'] = 250
                case year if year < 2018:
                    comp['price'] = 650
                case _:
                    comp['price'] = 1000

            if new_os is not None:
                comp['os'] = new_os
        else:
            print('Cannot refurbish an item that does not exist')
