class TeacherType:
    def __init__(self, id: int, name: str, display_name: str):
        self.id = id
        self.name = name
        self.display_name = display_name

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, Display Name: {self.display_name}"