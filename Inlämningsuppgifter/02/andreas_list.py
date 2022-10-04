from typing import Any


class AndreasList(list):
    def __init__(self, _list: list[Any]) -> None:
        super().__init__(_list)

    def __getitem__(self, index: int) -> Any:
        return super().__getitem__(index)

    def __setitem__(self, index: int, element: Any) -> None:
        super().__setitem__(index, element)

    def __repr__(self) -> str:
        return f'{[item for item in self]}'

    def filter_it(self, predicate) -> list[Any]:
        return AndreasList(filter(predicate, self.for_each_item(str)))

    def for_each_item(self, func) -> list[Any]:
        return [func(item) for item in self]

    def join_it(self) -> str:
        return ' '.join(self.for_each_item(str))

    def map_it(self, action) -> str:
        return ' '.join(map(action, self.for_each_item(str)))
