from os import name, system

def print_header(text: str):
    if name == 'nt':
        system('cls')
    elif name == 'posix':
        system('clear')
    print(text)
    print('------------------------------')