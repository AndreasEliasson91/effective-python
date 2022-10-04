from collections import UserList
from typing import Any


class ListOfString(list):
    def __init__(self, _list: list[Any]) -> None:
        super().__init__([str(element) for element in _list])

    def __getitem__(self, index: int) -> str:
        return super().__getitem__(index)

    def __setitem__(self, index: int, element: Any) -> None:
        super().__setitem__(index, element)

    def __repr__(self) -> str:
        return f'{[element for element in self]}'

    def __add__(self, _list: list[Any]) -> list[str]:
        self, _list, suffix_list = self._update_lists(_list)

        return ListOfString([str(element) for element in self._update_string_values(_list)]
                            + suffix_list)

    def __iadd__(self, _list: list[Any]) -> list[str]:
        self, _obj, suffix_list = self._update_lists(_list)
        self = [str(element) for element in self._update_string_values(_list)] \
            + suffix_list

        return self

    def __radd__(self, _obj) -> list[str]:
        self, _obj, suffix_list = self._update_lists(_obj)
        self = [str(element) for element in self._update_string_values(_obj)] \
            + suffix_list

        return self

    def append(self, element: Any) -> None:
        super().append(str(element))

    def extend(self, _list: list[Any]) -> None:
        super().extend([str(element) for element in _list])

    def insert(self, index: int, element: Any) -> None:
        super().insert(index, str(element))

    def _update_lists(self, _list: list[Any]) -> tuple[list[str], list[Any], list[Any]]:
        """
        Helper method to update the list and slice the suffix values,
        if the lists aren't the same length
        """
        if len(self) > len(_list):
            return ListOfString(self[:len(_list)]), _list, self[len(_list):]
        elif len(self) < len(_list):
            return self, _list[:len(self)], _list[len(self):]
        return self, _list, []

    def _update_string_values(self, _list: list[Any]) -> list[Any]:
        """
        Helper method to update the string values.
        If the both values in self and the _list is numeric,
        they converts to ints before the add
        Else the string values concatenates to a new string
        """
        temp = []

        for i, element in enumerate(self):
            if (isinstance(_list[i], (int, float)) or _list[i].isdigit()) \
                    and (element.isdigit()):
                temp.append(int(element) + int(_list[i]))
            else:
                temp.append(element + str(_list[i]))

        return temp


class ListOfUserString(UserList):
    def __init__(self, _list: list[Any]) -> None:
        super().__init__([str(element) for element in _list])

    def __getitem__(self, index: int) -> str:
        return super().__getitem__(index)

    def __setitem__(self, index: int, element: Any) -> None:
        super().__setitem__(index, element)

    def __repr__(self) -> str:
        return f'{[element for element in self]}'

    def append(self, element: Any) -> None:
        super().append(str(element))

    def extend(self, _list: list[Any]) -> None:
        super().extend([str(element) for element in _list])

    def insert(self, index: int, element: Any) -> None:
        super().insert(index, str(element))
