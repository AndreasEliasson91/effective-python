from person import Person


class Student(Person):
    def __init__(self, name: str, birthday: str, subjects: list[str], commute: str) -> None:
        super().__init__(name, birthday)
        self.subjects = subjects
        self.commute = commute
