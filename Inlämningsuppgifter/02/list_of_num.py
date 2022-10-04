from typing import Any, Union


class ListOfNum(list):
    def __init__(self, _list: list[Union[int, float, complex]]) -> None:
        self._data = [self._check_if_numeric_value(e) for e in _list]

    def __getitem__(self, index: int) -> Union[int, float, complex]:
        return self.data[index]

    def __setitem__(self, index: int, element: Union[int, float, complex]) -> None:
        self.data[index] = element

    def __repr__(self) -> str:
        return f'{[element for element in self.data]}'

    @ property
    def data(self):
        return self._data

    @ data.setter
    def data(self, _list: list[Union[int, float, complex]]) -> None:
        self._data = [self._check_if_numeric_value(e) for e in _list]

    def append(self, element: Union[int, float, complex]) -> None:
        self.data += [self._check_if_numeric_value(element)]

    def extend(self, _list: list[Union[int, float, complex]]) -> None:
        if isinstance(_list, type(self.data)):
            self.data += _list
        else:
            temp = [self._check_if_numeric_value(e) for e in _list]
            self.data += temp

    def insert(self, index: int, element: Union[int, float, complex]) -> None:
        self.data = self.data[:index] + [self._check_if_numeric_value(element)] \
                    + self.data[index:]

    @staticmethod
    def _check_if_numeric_value(value: Any) -> Union[int, float, complex]:
        if not isinstance(value, (int, float, complex)):
            raise TypeError(f'Numeric value expected, got {type(value)}')
        return value
