from dataclasses import dataclass


@dataclass(order=True)
class Item:
    price: float
    weight: float
    volume: tuple
