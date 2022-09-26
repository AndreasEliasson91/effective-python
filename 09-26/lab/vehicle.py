import uuid

from abc import ABC
from enum import Enum, auto
from location import Location


class Status(Enum):
    FREE = auto()
    BUSY = auto()
    NOT_WORKING = auto()


class Vehicle(ABC):
    def __init__(self, location: tuple) -> None:
        self.__id: str = uuid.uuid1()
        self.current_position: Location = Location(*location)
        self.current_status: Status = Status.FREE


class Bike(Vehicle):
    def __init__(self, location: tuple) -> None:
        super().__init__(location)
        self.capacity = 10


class Truck(Vehicle):
    def __init(self, location: tuple) -> None:
        super().__init__(location)
        self.capacity = 100
