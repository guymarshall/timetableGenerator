class Student:
    def __init__(self, id: str, first_name: str, middle_names: str, surname: str, initials: str):
        self.id = id
        self.first_name = first_name
        self.middle_names = middle_names
        self.surname = surname
        self.initials = initials

    def __str__(self):
        return f"Id: {self.id}, First Name: {self.first_name}, Middle Names: {self.middle_names}, Surname: {self.surname}, Initials: {self.initials}"