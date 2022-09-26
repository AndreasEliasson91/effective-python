class LogisticsSystem:
    @staticmethod
    def take_an_order():
        print('Taking order')

    @staticmethod
    def take_orders():
        print('Taking orders')

    @staticmethod
    def process_an_order():
        print('Process order')

    @staticmethod
    def track_order(order_no: str):
        print('Track order')

    @staticmethod
    def cancel_order(order_no: str):
        print('Cancel Order')

    @staticmethod
    def register_new_user():
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
                system.take_orders()
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
