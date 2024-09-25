from typing import List
from classes.room import Room
from classes.subject import Subject
from classes.teacher_type import TeacherType


class Teacher:
    def __init__(self, id: int, first_name: str, middle_names: str, surname: str, initials: str, teacher_type: TeacherType, subjects_taught: List[Subject], rooms_taught: List[Room]):
        self.id = id
        self.first_name = first_name
        self.middle_names = middle_names
        self.surname = surname
        self.initials = initials
        self.teacher_type_id = teacher_type.id
        self.teacher_type = teacher_type
        self.subject_taught_ids = [subject_taught.id for subject_taught in subjects_taught]
        self.subjects_taught = subjects_taught
        self.room_taught_ids = [room_taught.id for room_taught in rooms_taught]
        self.rooms_taught = rooms_taught

    def __str__(self):
        return f"Id: {self.id}, First Name: {self.first_name}, Middle Names: {self.middle_names}, Surname: {self.surname}, Initials: {self.initials}, Teacher Type Id: {self.teacher_type_id}"