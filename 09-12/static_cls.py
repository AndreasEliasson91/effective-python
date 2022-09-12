class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name: str, year: int):
        from datetime import date

        return cls(
            name=name,
            age=date.today().year - year
        )

    @staticmethod
    def is_adult(age: int) -> bool:
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.from_birth_year('mayank', 1996)

print(person1.age)
print(person2.age)

print(Person.is_adult(person1.age))
print(Person.is_adult(person2.age))
