from typing import *
from cli_utility import print_header
import sys
import pickle

def school(s):
    print_header('School!')
    options: dict = {1: s.get_details, 2: s.edit_name}
    print('1. Details')
    print('2. Edit name')
    options[int(input('Enter Option: '))]()
    return s

def school_class(s):
    print_header('Class!')
    options: dict = {1: s.get_school_class_details, 2: s.add_school_class, 3: s.edit_school_class}
    print('1. Details')
    print('2. Add Class')
    print('3. Edit Class')
    options[int(input('Enter Option: '))]()
    return s

def student(s):
    print_header('Student!')
    options: dict = {1: s.get_student_details, 2: s.add_student}
    print('1. Details')
    print('2. Add Student')
    options[int(input('Enter Option: '))]()
    return s

def cli(s):
    options: dict = {1: school, 2: school_class, 3: student}
    print_header(f'Welcome back School {s.get_name()}!')
    print('1.) School')
    print('2.) Class')
    print('3.) Student')
    print('9.) Exit')

    o: int = int(input('Enter Option: '))

    try:
        s = options[o](s)
    except Exception as e:
        print_header('Goodbye!')
        sys.exit()