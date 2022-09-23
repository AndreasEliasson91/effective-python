from dataclasses import dataclass, field
from lesson import Schedule


class Person:
    __slots__ = ('__id', 'name', 'birthdate', 'schedule')

    def __init__(self, _id: str, name: str, birthdate: str) -> None:
        self.__id: str = _id
        self.name: str = name
        self.birthdate: str = birthdate
        self.schedule: Schedule = Schedule()

    @property
    def id(self) -> str:
        return self.__id

    # def create_schedule(self, schedule: dict) -> None:
    #     self.schedule = schedule
    #
    # def update_schedule(self, **kwargs) -> None:
    #     for k, v in kwargs.items():
    #         for slot, lesson in self.schedule.items():
    #             if slot == k:
    #                 lesson = v


@dataclass(order=True)
class Personnel:
    staff: list[Person] = field(default_factory=list)
    students: list[Person] = field(default_factory=list)
    number_of_staff: int = 0
    number_of_students: int = 0

    def get_staff_id(self) -> str:
        self.number_of_staff += 1
        return 'STA' + str(self.number_of_staff)

    def get_student_id(self) -> str:
        self.number_of_students += 1
        return 'STU' + str(self.number_of_students)
