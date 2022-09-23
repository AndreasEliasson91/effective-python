from person import Person


class Staff(Person):
    __slots__ = ('working_hours',)

    def __init__(self, _id: str, name: str, birthdate: str, staff_role: str) -> None:
        super().__init__(_id, name, birthdate)
        self.staff_role = staff_role
        self.working_hours = dict()

    def set_working_hours(self, **kwargs) -> None:
        for k, v in kwargs.items():
            self.working_hours[k] = v


class Teacher(Staff):
    def __init__(self, _id: str, name: str, birthdate: str, teaching_subjects: list[str]) -> None:
        super().__init__(_id, name, birthdate, staff_role='teacher')
        self.teaching_subjects = teaching_subjects


class Administration(Staff):
    def __init__(self, _id: str, name: str, birthday: str) -> None:
        super().__init__(_id, name, birthday, staff_role='administration')
