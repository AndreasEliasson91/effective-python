from person import Person
from abc import ABC


class Staff(Person, ABC):
    __slots__ = ('working_hours',)

    def __init__(self, name: str, birthday: str) -> None:
        super().__init__(name, birthday)
        self.working_hours = dict()

    def set_working_hours(self, **kwargs) -> None:
        for k, v in kwargs.items():
            self.working_hours[k] = v


class Teacher(Staff):
    def __init__(self, name: str, birthday: str, teaching_subjects: list[str]) -> None:
        super().__init__(name, birthday)
        self.teaching_subjects = teaching_subjects


class Administration(Staff):
    def __init__(self, name: str, birthday: str) -> None:
        super().__init__(name, birthday,)
