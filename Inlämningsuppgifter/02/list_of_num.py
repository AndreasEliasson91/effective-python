from typing import Any, Union


class ListOfNum(list):
    def __init__(self, _list: list[Union[int, float, complex]]) -> None:
        super().__init__([self._check_if_numeric_value(e) for e in _list])

    def __getitem__(self, index: int) -> Union[int, float, complex]:
        return super().__getitem__(index)

    def __setitem__(self, index: int, element: Union[int, float, complex]) -> None:
        super().__setitem__(index, self._check_if_numeric_value(element))

    def __repr__(self) -> str:
        return f'{[element for element in self]}'

    def append(self, element: Union[int, float, complex]) -> None:
        super().append([self._check_if_numeric_value(element)])

    def extend(self, _list: list[Union[int, float, complex]]) -> None:
        super().extend([self._check_if_numeric_value(e) for e in _list])

    def insert(self, index: int, element: Union[int, float, complex]) -> None:
        super().insert(index, self._check_if_numeric_value(element))

    @staticmethod
    def _check_if_numeric_value(value: Any) -> Union[int, float, complex]:
        if not isinstance(value, (int, float, complex)):
            raise TypeError(f'Numeric value expected, got {type(value)}')
        return value
