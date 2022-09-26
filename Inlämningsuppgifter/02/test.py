class ListOfStrings(list):
    def __init__(self, _list: Any) -> None:
        self._list = [str(item) for item in _list]

    def __repr__(self):
        return f'{[item for item in self._list]}'


def main():
    data = ListOfStrings([11, 2, 22, 4, 105])
    print(data)
