from collection import UserList
from typing import Any


class ListOfUserString(UserList):
    def __init__(self, _list: list[Any]) -> None:
        self._data = [str(element) for element in _list]

    def __getitem__(self, index: int) -> str:
        return self.data[index]

    def __setitem__(self, index: int, element: Any) -> None:
        self.data[index] = element

    def __repr__(self) -> str:
        return f'{[element for element in self.data]}'

    @ property
    def data(self):
        return self._data

    @ data.setter
    def data(self, _list: list[Any]) -> None:
        self._data = _list

    def append(self, element: Any) -> None:
        self.data += [str(element)]

    def extend(self, _list: list[Any]) -> None:
        self.data += [str(element) for element in _list]

    def insert(self, index: int, element: Any) -> None:
        self.data = self.data[:index] + [str(element)] + self.data[index:]
