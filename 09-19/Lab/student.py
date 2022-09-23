from person import Person


class Student(Person):
    def __init__(self, _id: str, name: str, birthdate: str, subjects: list[str], commute: str) -> None:
        super().__init__(_id, name, birthdate)
        self.subjects = subjects
        self.commute = commute
