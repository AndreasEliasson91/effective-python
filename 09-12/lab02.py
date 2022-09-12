BASE_PRICING = 1.0
TAX_RATE = 1.0


class Company:
    website = ''
    size = 0
    industry = ''
    employees = []

    def email_key_employee(self, message):
        self.employees[0].notify(message)


class Employee:
    @staticmethod
    def notify(message: str) -> None:
        print(message)


class SmallMediumBusiness(Company):
    def send_notification(self, email_func) -> None:
        email_func(self.employees[0].email)

    def send_notification_delegate(self, email_func, message) -> None:
        self.email_key_employee(message)

    @staticmethod
    def get_pricing(units: float) -> float:
        base = BASE_PRICING * units * 0.8
        tax = base * TAX_RATE * 0.8
        return base * tax


smb = SmallMediumBusiness()
employee = Employee()
smb.employees.append(employee)

smb.send_notification_delegate(None, 'Hello')
