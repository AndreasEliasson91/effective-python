from typing import Any


class ListOfString(list):
    def __init__(self, _list: list[Any]) -> None:
        self._obj = [str(element) for element in _list]

    def __getitem__(self, index: int) -> str:
        return self.obj[index]

    def __setitem__(self, index: int, element: Any) -> None:
        self.obj[index] = element

    def __repr__(self) -> str:
        return f'{[element for element in self.obj]}'

    def __add__(self, element: Any):
        if isinstance(element, list):
            return ListOfString(self.obj + [str(e) for e in element])
        else:
            return ListOfString(self.obj + [str(element)])

    def __iadd__(self, element: Any) -> list[str]:
        if isinstance(element, list):
            self.obj += [str(e) for e in element]
        else:
            self.obj += [str(element)]
        return self.obj

    def __radd__(self, _obj) -> list[str]:
        return _obj + self.obj

    @ property
    def obj(self):
        return self._obj

    @ obj.setter
    def obj(self, value: list[Any]) -> None:
        self._obj = value

    def append(self, element: Any) -> None:
        self.obj += [str(element)]

    def extend(self, elements: list[Any]) -> None:
        self.obj += [str(element) for element in elements]

    def insert(self, index: int, element: Any) -> None:
        self.obj = self.obj[:index] + [str(element)] + self.obj[index:]
