from typing import Union


class ListOfNum(list):
    def __init__(self, _list: list[Union[int, float, complex]]) -> None:
        for item in _list:
            if not isinstance(item, (int, float, complex)):
                raise TypeError(f'Numeric value expected, got {type(item)}')

        self._obj = _list

    def __getitem__(self, index: int) -> Union[int, float, complex]:
        return self.obj[index]

    def __setitem__(self, index: int, element: Union[int, float, complex]) -> None:
        self.obj[index] = element

    def __repr__(self) -> str:
        return f'{[element for element in self.obj]}'

    @ property
    def obj(self):
        return self._obj

    @ obj.setter
    def obj(self, value: list[Union[int, float, complex]]) -> None:
        for item in value:
            if not isinstance(item, (int, float, complex)):
                raise TypeError(f'Numeric value expected, got {type(item)}')

        self._obj = value

    def append(self, element: Union[int, float, complex]) -> None:
        self.obj += [element]

    def extend(self, elements: list[Union[int, float, complex]]) -> None:
        self.obj += elements

    def insert(self, index: int, element: Union[int, float, complex]) -> None:
        self.obj = self.obj[:index] + [element] + self.obj[index:]
