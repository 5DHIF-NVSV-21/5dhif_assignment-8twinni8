from cli_utility import print_header

class SchoolClass:
    def __init__(self, name):
        self.name: str = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_details(self):
        print_header('Details!')
        print(f'School name: {self.name}')
        input('<Waiting for input>')

    def edit_name(self):
        print_header(f'Edit Name of {self.name}!')
        self.name = input('Name: ')
        pass

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f'{self.name}'

    def __eq__(self, other):
        return self.name == other