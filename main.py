from typing import *
import cli
from cli_utility import print_header
from school import School

def main():
    print_header('Welcome to the School Manager!')
    s: School = School(input('Enter school name: '))
    while True:
        cli.cli(s)


if __name__ == '__main__':
    main()