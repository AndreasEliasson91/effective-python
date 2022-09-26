import uuid


class Distributor:
    """Just to display sender/distributor in orders"""
    pass


class User:
    def __init__(self, name: str, address: dict,
                 phone_number: str, email: str) -> None:
        self.__id: str = uuid.uuid1()
        self.name: str = name
        self.address: dict = address
        self.phone_number: str = phone_number
        self.email: str = email

    @property
    def id(self) -> str:
        return self.__id
