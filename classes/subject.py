from typing import List

from classes.room import Room
from classes.teacher import Teacher


class Subject:
    def __init__(self, id: int, subject_name: str, subject_year: int, set: str, maximum_class_size: int, teachers: List[Teacher], rooms_taught: List[Room]):
        self.id = id
        self.subject_name = subject_name
        self.subject_year = subject_year
        self.set = set
        self.maximum_class_size = maximum_class_size
        self.teachers = teachers
        self.room_taught_ids = [room.id for room in rooms_taught]
        self.rooms_taught = rooms_taught

    def __str__(self):
        return f"Id: {self.id}, Subject Name: {self.subject_name}, Subject Year: {self.subject_year}, Set: {self.set}, Maximum Class Size: {self.maximum_class_size}"