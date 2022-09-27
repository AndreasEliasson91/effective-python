import time
from item import Item
from order import Order, PaymentMethod
from user import Distributor, User


class LogisticsSystem:
    def __init(self) -> None:
        self.orders_in_progress: list[Order] = []
        self.customers: list[User] = []

    def take_order(self):
        print('Enter order information:\n')
        time.sleep(3)
        order = {
            'priority': 2,
            'sender': Distributor(),
            'buyer': User(
                name='Anna Andersson',
                address='This Is The Address 00, 112 00 Newtown',
                phone_number='112 000',
                email='aa@newtown-mail.com'
            ),
            'items': [
                Item(10.0, 26.8, (30, 30, 30)),
                Item(25.9, 12.3, (14, 15, 15))
            ],
            'payment_method': PaymentMethod.CREDIT_CARD
        }
        print('Thanks!')
        temp_order = Order(
            priority=order['priority'],
            sender=order['sender'],
            buyer=order['buyer'],
            items=order['items'],
            payment_method=order['payment_method'],
        )
        self.process_an_order()
        self.orders_in_progress.append(temp_order)
        print(f'Order number: {temp_order.id}')

    def process_an_order(self):
        print('Processing order...')

    def track_order(self, order_no: str):
        print('Track order')

    def cancel_order(self, order_no: str):
        print('Cancel Order')

    def register_new_user(self):
        print('Register USer')


class CLI_GUI:
    @staticmethod
    def print_menu() -> str:
        return """
        1. Register User
        2. Place Order
        3. Track Order
        4. Cancel Order
        5. Quit
        """

    @staticmethod
    def process_user_input(system: LogisticsSystem, _input: str) -> bool:
        _input = int(_input)
        if _input == 5:
            print('Thanks for using this service')
            return False

        match _input:
            case 1:
                system.register_new_user()
            case 2:
                system.take_order()
            case 3:
                order_no = input('Enter the order number to track:\n>> ')
                system.track_order(order_no)
            case 4:
                order_no = input('Enter the order number to cancel:\n>> ')
                system.cancel_order(order_no)
            case _:
                print('Invalid input')

        return True


def main():
    system = LogisticsSystem()
    gui = CLI_GUI()

    print(gui.print_menu())
    user_input = input('Enter a menu option:\n>> ')

    while gui.process_user_input(system, user_input):
        user_input = input('Enter a menu option:\n>> ')


if __name__ == '__main__':
    main()
