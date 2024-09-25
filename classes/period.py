from classes.day_of_week import DayOfWeek
from classes.room import Room
from classes.teacher import Teacher


class Period:
    def __init__(self, id: int, day_of_week: DayOfWeek, teacher: Teacher, room: Room, start_time: str, end_time: str):
        self.id = id
        self.day_of_week = day_of_week
        self.teacher = teacher
        self.room = room
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Id: {self.id}, Day Of Week: {self.day_of_week}, Teacher: {self.teacher}, Room: {self.room}, Start Time: {self.start_time}, End Time: {self.end_time}"