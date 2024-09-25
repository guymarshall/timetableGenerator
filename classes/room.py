from typing import List

from classes.subject import Subject
from classes.teacher import Teacher


class Room:
    def __init__(self, id: int, name: str, maximum_class_size: int, subjects_taught: List[Subject], teachers: List[Teacher]):
        self.id = id
        self.name = name
        self.maximum_class_size = maximum_class_size
        self.subjects_taught = subjects_taught
        self.teachers = teachers

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, Maximum Class Size: {self.maximum_class_size}"