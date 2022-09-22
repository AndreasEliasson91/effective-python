from dataclasses import dataclass, field
from typing import Any
from schedule import Schedule


class Person:
    __slots__ = ('_id', 'name', 'birthday', '_schedule')

    def __init__(self, name: str, birthday: str) -> None:
        self._id = None
        self.name = name
        self.birthday = birthday
        self._schedule = Schedule()

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, _id: str) -> None:
        self._id = _id

    @property
    def schedule(self) -> Schedule:
        return self._schedule

    @schedule.setter
    def schedule(self, blocks: dict) -> None:
        self._schedule.create_schedule(**blocks)


@dataclass
class Personnel:
    staff: list[Any] = field(default_factory=list)
    students: list[Any] = field(default_factory=list)
    number_of_staff: int = 0
    number_of_students: int = 0

    def get_staff_id(self) -> str:
        self.number_of_staff += 1
        return 'STA' + str(self.number_of_staff)

    def get_student_id(self) -> str:
        self.number_of_students += 1
        return 'STU' + str(self.number_of_students)

    def add_staff(self) -> None:
        pass

    def add_student(self) -> None:
        pass
