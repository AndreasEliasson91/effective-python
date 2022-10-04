from typing import Any


class AndreasList(list):
    def __init__(self, _list: list[Any]) -> None:
        self._data = _list

    def __getitem__(self, index: int) -> Any:
        return self.data[index]

    def __setitem__(self, index: int, element: Any) -> None:
        self.data[index] = element

    def __repr__(self) -> str:
        return f'{[item for item in self.data]}'

    @property
    def data(self) -> list[Any]:
        return self._data

    @data.setter
    def data(self, _list: list[Any]) -> None:
        self._data = _list

    def filter_it(self, predicate) -> list[Any]:
        return list(filter(predicate, self.for_each_item(str)))

    def for_each_item(self, func) -> list[Any]:
        return [func(item) for item in self.data]

    def join_it(self) -> str:
        return ' '.join(self.for_each_item(str))

    def map_it(self, action) -> str:
        return ' '.join(map(action, self.for_each_item(str)))
