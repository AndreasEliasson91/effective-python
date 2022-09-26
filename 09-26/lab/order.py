import uuid

from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum, auto
from typing import Optional

from item import Item
from user import Distributor, User


class OrderPriority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

    @classmethod
    def get_priority(cls, priority: int):
        match priority:
            case 1:
                return cls.LOW
            case 2:
                return cls.MEDIUM
            case 3:
                return cls.HIGH
            case _:
                raise ValueError('Not a valid priority input')


class OrderStatus(Enum):
    DELIVERED = auto()
    PROCESSING = auto()
    CANCELED = auto()


class PaymentMethod(Enum):
    NET_BANKING = 1
    CREDIT_CARD = 2
    DEBIT_CARD = 3

    @classmethod
    def standard_payment_method(cls):
        return cls.DEBIT_CARD


@dataclass
class PaymentDetails:
    __transition_id: str = uuid.uuid1()
    amount: float = None
    payment_method: Optional[PaymentMethod] = None
    card_number: str = None
    payment_status: str = 'UNPAID'

    @property
    def transition_id(self) -> str:
        return self.__transition_id


class Order:
    def __init__(self, priority: int, sender: Distributor, buyer: User,
                 items: list[Item], payment_method: PaymentMethod) -> None:
        self.__id: str = uuid.uuid1()
        self.order_priority: OrderPriority = OrderPriority.get_priority(
            priority)
        self.sender: Distributor = sender
        self.buyer: User = buyer
        self.courier: Vehicle = next(
            filter(lambda x: x.status == 'FREE', vehicle_list), False)
        self.current_location: Location = self.courier.location
        self.items: list[Item] = items

        self.total_weight: float = 0.0
        total = 0.0
        for item in items:
            total += item.price
            self.total_weight += item.weight

        self.payment_details: PaymentDetails = PaymentDetails(
            amount=total,
            payment_method=payment_method,
            card_number=buyer.card_number
        )

        self.order_status: OrderStatus = OrderStatus.PROCESSING
        self.order_place_time: datetime = datetime.now()
        self.delivery_time: datetime = self.order_place_time.date + \
            timedelta(weeks=2)
