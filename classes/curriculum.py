from classes.student import Student
from classes.subject import Subject


class Curriculum:
    """
    pub id: i32,
    pub student_id: String,
    pub student: Student,
    pub subject_id: i32,
    pub subject: Subject,
    pub number_of_lessons_per_week: i32,
    """
    def __init__(self, id: int, student: Student, subject: Subject, number_of_lessons_per_week: int):
        self.id = id
        self.student_id = student.id
        self.student = student
        self.subject_id = subject.id
        self.subject = subject
        self.number_of_lessons_per_week = number_of_lessons_per_week

    def __str__(self):
        return f"Id = {self.id}, Student Id = {self.student_id}, Subject Id = {self.subject_id}, Number of Lessons Per Week = {self.number_of_lessons_per_week}"