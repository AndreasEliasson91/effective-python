from dataclasses import dataclass, field
from typing import Any, Dict

# from personnel import Teacher
#
#
# @dataclass
# class Lesson:
#     teacher: Teacher
#     classroom: int
#     subject: str = None


@dataclass
class Schedule:
    schedule: Dict[str, Any] = field(init=False, default_factory=dict)

    def create_schedule(self, **kwargs) -> schedule:
        self.schedule = kwargs
