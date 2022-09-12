from collections import namedtuple


class Person:
    def __init__(self, company_website: str, mobile_number: str, area_code: str) -> None:
        Telephone = namedtuple('Telephone', ['area_code', 'mobile_number'])

        self.company_website = company_website
        self.phone_number = Telephone(mobile_number=mobile_number, area_code=area_code)

    def get_company_website_extension(self) -> str:
        result = self.company_website.replace('/', '').split('.')

        if len(result) > 1:
            return result[-1]

        print('Not a valid domain')
        return ''


class Customer(Person):
    def __init__(self, company_website: str, mobile_number: str, area_code: str) -> None:
        super().__init__(company_website, mobile_number, area_code)


class Lead(Person):
    def __init__(self, company_website: str, mobile_number: str, area_code: str) -> None:
        super().__init__(company_website, mobile_number, area_code)


class Opportunity(Person):
    def __init__(self, company_website: str, mobile_number: str, area_code: str) -> None:
        super().__init__(company_website, mobile_number, area_code)


customer = Customer('', '07xx xx xx xx', '+46')
lead = Lead('', '07xx xx xx xx', '+46')
opportunity = Opportunity('', '07xx xx xx xx', '+46')
