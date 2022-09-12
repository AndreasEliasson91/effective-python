class Base:
    def __init__(self) -> None:
        self.a = 'I Love Python'
        self.__c = 'I\'m Private'

    @property
    def c(self) -> str:
        return self.__c

    @c.setter
    def c(self, _c: str) -> None:
        self.__c = _c


class Derived(Base):
    def __init__(self) -> None:
        super().__init__()
        print(f'Printing private c from base: {self.c}')


obj1 = Base()
print(f'Base a: {obj1.a}')
print(f'Base c: {obj1.c}')

obj2 = Derived()
print(f'Derived a: {obj2.a}')
print(f'Derived c: {obj2.c}')

obj2.c = 'C'
print(f'Derived c after using c.setter: {obj2.c}')
