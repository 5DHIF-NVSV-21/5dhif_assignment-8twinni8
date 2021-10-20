class Student:
    def __init__(self, name, school_class):
        self.name = name
        self.school_class = school_class

    def __str__(self):
        return f'{self.name} ({self.school_class})'