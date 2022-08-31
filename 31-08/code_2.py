"""Module with animal classes"""


class Hund:
    """Dog class"""
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        """
        Speak method
        :return: str
        """
        return self.name + ' says Woof!'

    def eat(self, food: str) -> str:
        """
        Eat method
        :return: str
        """
        return self.name + ' eats the ' + food


class Cat:
    """Cat class"""
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        """
        Speak method
        :return: str
        """
        return self.name + ' says Meow!'

    def eat(self, food: str) -> str:
        """
        Eat method
        :return: str
        """
        return self.name + ' eats the ' + food


leo = Hund('Leo')
nancy = Cat('Nancy')

print(leo.speak())
print(nancy.speak())

print(leo.eat('meat'))
print(nancy.eat('fish'))
