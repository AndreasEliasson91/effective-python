from typing import Any


class AndreasList(list):
    def __init__(self, _list: list[Any]) -> None:
        self._obj = _list

    def __getitem__(self, index: int) -> Any:
        return self.obj[index]

    def __setitem__(self, index: int, element: Any) -> None:
        self.obj[index] = element

    def __repr__(self) -> str:
        return 'AndreasList'

    @property
    def obj(self) -> list[Any]:
        return self._obj

    @obj.setter
    def obj(self, value: list[Any]) -> None:
        self._obj = value

    def join_it(self) -> str:
        pass

    def map_it(self, action) -> Any:
        pass

    def filter_it(self, predicate) -> list[Any]:
        pass

    def for_each_item(self, func):
        pass
