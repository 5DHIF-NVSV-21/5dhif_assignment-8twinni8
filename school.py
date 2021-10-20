from cli_utility import print_header
from school_class import SchoolClass
from student import Student

class School:
    def __init__(self, name):
        self.name: str = name
        self.school_classes: list = []
        self.students: list = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_details(self):
        print_header('Details!')
        print(f'School name: {self.name}')
        input('<Waiting for input>')

    def edit_name(self):
        print_header('Edit Name!')
        self.name = input('Name: ')
        pass

    def get_school_class_details(self):
        print_header('School Class Details!')
        for c in self.school_classes:
            print(c)
        input('<Waiting for input>')

    def edit_school_class(self):
        print_header('Edit School Class!')
        for i, c in enumerate(self.school_classes):
            print(f'{i+1}. {c}')
        self.school_classes[int(input('Enter Option: '))-1].edit_name()

    def add_school_class(self):
        print_header('Add Class!')
        self.school_classes.append(SchoolClass(input('Name: ')))

    def get_student_details(self):
        print_header('Students Details!')
        for s in self.students:
            print(s)
        input('<Waiting for input>')

    def add_student(self):
        print_header('Add Student')
        name = input('Name: ')
        school_class = str(input('School Class: '))
        if school_class in self.school_classes:
            sc = self.school_classes[self.school_classes.index(school_class)]
            self.students.append(Student(name, sc))
            print('Added')
        else:
            print('Class not found!')
        input('<Waiting for input>')
        pass