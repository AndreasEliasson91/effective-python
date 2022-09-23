from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, order=True)
class Lesson:
    teacher: Any
    classroom: int
    subject: str = None


@dataclass(order=True)
class Schedule:
    schedule: dict[str, Lesson] = field(default_factory=dict[str, Lesson])

    def add_lesson(self, teacher, classroom_id: int, subject: str, time_slot: str) -> None:
        lesson = Lesson(
            teacher=teacher,
            classroom=classroom_id,
            subject=subject
        )
        self.schedule[time_slot] = lesson

